from neo4j import GraphDatabase
import json

# 读取JSON文件
with open('./李四/personInfo.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 连接到Neo4j数据库
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)


def create_person(tx, person_data):
    # 创建Person节点
    tx.run("""
    CREATE (p:Person {
        身份证号码: $身份证号码,
        姓名: $姓名,
        曾用名: $曾用名,
        绰号: $绰号,
        联系电话: $联系电话,
        性别: $性别,
        年龄: $年龄,
        身高: $身高,
        体重: $体重,
        血型: $血型,
        民族: $民族,
        重点人员类型: $重点人员类型,
        教育程度: $教育程度,
        职业: $职业,
        工作单位: $工作单位,
        出生地: $出生地,
        户籍所在地: $户籍所在地,
        常住地: $常住地,
        家庭人口: $家庭人口,
        思想倾向: $思想倾向,
        兴趣爱好: $兴趣爱好,
        政治面貌: $政治面貌,
        宗教信仰: $宗教信仰,
        祖籍: $祖籍,
        特殊经历: $特殊经历,
        特殊外表与标记: $特殊外表与标记,
        犯罪技能: $犯罪技能,
        婚姻状况: $婚姻状况
    })
    """, person_data)


def create_tags(tx, person_id, tags):
    for tag, content in tags.items():
        tx.run("""
        MATCH (p:Person {身份证号码: $person_id})
        CREATE (t:Tag {
            name: $tag,
            content: $content
        })
        CREATE (p)-[:HAS_TAG]->(t)
        """, person_id=person_id, tag=tag, content=json.dumps(content, ensure_ascii=False))


def main():
    person_data = data["个人信息"]
    tags = {key: value for key, value in data.items() if key != "个人信息"}

    with driver.session() as session:
        session.write_transaction(create_person, person_data)
        session.write_transaction(create_tags, person_data["身份证号码"], tags)


if __name__ == "__main__":
    main()
