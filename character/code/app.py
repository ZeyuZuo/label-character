from flask import Flask, request, jsonify
from models import Person, Tag, tagUtils, driver, ReturnObj, add_inference_tags
from config import tag_class
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def create_response(data=None, msg='success', code=200):
    response = {
        "msg": msg,
        "data": data
    }
    return jsonify(response), code


def result2p(result, persons):
    for record in result:
        person_node = record["p"]
        # Convert the Node to a dictionary with only the desired fields
        person_data = {
            "id_card": person_node.get("身份证号码"),
            "name": person_node.get("姓名"),
            "age": person_node.get("年龄"),
            "gender": person_node.get("性别"),
            "address": person_node.get("户籍所在地")
        }
        persons.append(person_data)


def get_all_persons():
    print("search all persons")
    persons = []
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p")
        result2p(result, persons)
    print(persons)

    return create_response(data=persons)


# 定义查询特定 Person 节点的路由，根据身份证id或者姓名
@app.route('/persons', methods=['GET'])
def get_person():
    id_card = request.args.get('id_card')
    name = request.args.get('name')

    # print('search persons where id_card is ' + id_card + ', name is ' + name)

    if id_card:
        query = "MATCH (p:Person {身份证号码: $id_card}) RETURN p"
        param = {'id_card': id_card}
    elif name:
        query = "MATCH (p:Person) WHERE p.姓名 CONTAINS $name RETURN p"
        param = {'name': name}
    else:
        return get_all_persons()

    print("query : " + query)
    persons = []
    with driver.session() as session:
        result = session.run(query, param)
        result2p(result, persons)
    print(persons)

    return create_response(data=persons)


def get_info(id_card):
    person = {}

    with driver.session() as session:
        result = session.run("""
            MATCH (p:Person {身份证号码: $id_card})
            RETURN p
        """, id_card=id_card)
        for record in result:
            person_node = record["p"]
            for key in person_node.keys():
                # print(key, person_node[key])
                person[key] = person_node[key]

    print(person)
    return person


"""
获取所有个人信息
"""


@app.route('/person/info', methods=['GET'])
def get_person_info():
    id_card = request.args.get('id_card')
    if id_card is None:
        return create_response(msg='id_card is required', code=400)

    return create_response(data=get_info(id_card))


# 定义查询特定 Person 节点及其关联的所有 Tag 节点的路由，根据身份证id获取各个tag内容
@app.route('/person/tags', methods=['GET'])
def get_person_tags():
    id_card = request.args.get('id_card')
    tags = {}
    with driver.session() as session:
        result = session.run("""
            MATCH (p:Person {身份证号码: $id_card})-[:HAS_TAG]->(t:Tag)
            RETURN t.name AS name, t.content AS content
        """, id_card=id_card)
        for record in result:
            tags[record['name']] = record['content']

    print(tags)
    live_place = get_info(id_card)['常住地']
    # 添加推断特征
    tags = add_inference_tags(tags, live_place)
    return create_response(data=tags)


@app.route('/person/tag', methods=['GET'])
def get_person_tag():
    id_card = request.args.get('id_card')
    tag_num = request.args.get('tag_num')

    if tag_num == None:
        return create_response(msg='tag_num is required', code=400)
    if tag_num not in tag_class:
        return create_response(msg='tag_num is invalid', code=400)
    if tag_num in ['1', '2', '3']:
        return create_response(msg='tag_num is invalid', code=400)

    tag_name = tag_class[int(tag_num)]

    names = tag_name.split(',')
    tag_names = []
    for name in names:
        if tagUtils.is_tag_exist(name):
            tag_names.append(name)

    tags = {}

    with driver.session() as session:
        result = session.run("""
            MATCH (p:Person {身份证号码: $id_card})-[:HAS_TAG]->(t:Tag)
            WHERE (t.name IN $tag_names)
            RETURN t.name AS name, t.content AS content
        """, id_card=id_card, tag_names=tag_names)

        for record in result:
            tags[record['name']] = record['content']

    print(tags)
    return create_response(data=tags)


# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=12345)
