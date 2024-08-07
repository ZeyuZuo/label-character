import datetime
import json
from collections import Counter
import mysql.connector
from neo4j import GraphDatabase

import config


# 标签名称和内容
class Tag:
    def __init__(self, id, name, content):
        self.id = id
        self.name = name
        self.content = content
        self.subTags = []


# 人节点的定义，以及一级标签
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tags = []


# 观测的定义，包含哪些Tag
class Watch:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.persons = []


# 返回数据
class ReturnObj:
    def __init__(self, data):
        self.code = 0
        self.msg = "success"
        self.data = data


'''
mysql数据库
'''


def add_inference_tags(tags, live_place) -> dict:
    """
    添加推断标签
    """
    tags['推断特征'] = {}
    one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    two_month_ago = datetime.datetime.now() - datetime.timedelta(days=60)
    three_month_ago = datetime.datetime.now() - datetime.timedelta(days=90)

    # 近三个月离开常住地频率
    leave_home_frequency = 0
    for tag, content in json.loads(tags['活动区域轨迹']).items():
        if (datetime.datetime.strptime(content['时间'], "%Y-%m-%d") > three_month_ago
                and content['地点'] != live_place):
            leave_home_frequency += 1
    if leave_home_frequency > 10:
        tags['推断特征']['近一个月离开常住地频率'] = '高'
    elif leave_home_frequency > 5:
        tags['推断特征']['近一个月离开常住地频率'] = '中'
    else:
        tags['推断特征']['近一个月离开常住地频率'] = '低'

    # 近一个月社交媒体活跃度
    social_media_activity = 0
    for tag, content in json.loads(tags['社交媒体痕迹']).items():
        if datetime.datetime.strptime(content['时间'], "%Y-%m-%d") > one_month_ago:
            social_media_activity += 1
    if social_media_activity > 10:
        tags['推断特征']['近一个月社交媒体活跃度'] = '高'
    elif social_media_activity > 5:
        tags['推断特征']['近一个月社交媒体活跃度'] = '中'
    else:
        tags['推断特征']['近一个月社交媒体活跃度'] = '低'

    # 近期健康状态，看近三个月医疗记录
    hospital_frequency = 0
    for tag, content in json.loads(tags['医疗记录']).items():
        if datetime.datetime.strptime(content['时间'], "%Y-%m-%d") > three_month_ago:
            hospital_frequency += 1
    if hospital_frequency > 5:
        tags['推断特征']['近期健康状态'] = '不佳'
    elif hospital_frequency > 2:
        tags['推断特征']['近期健康状态'] = '良好'
    else:
        tags['推断特征']['近期健康状态'] = '健康'

    # 近期关注内容，看近两个月书籍阅读记录，网络痕迹记录
    recent_books = []
    recent_webs = []
    recent_focus = ''
    for tag, content in json.loads(tags['书籍阅读记录']).items():
        if datetime.datetime.strptime(content['时间'], "%Y-%m-%d") > two_month_ago:
            recent_books.append(content['内容'])
    for tag, content in json.loads(tags['网络痕迹记录']).items():
        if datetime.datetime.strptime(content['时间'], "%Y-%m-%d") > two_month_ago:
            recent_webs.append(content['内容'])
    books_counter = Counter(recent_books)
    webs_counter = Counter(recent_webs)
    book_focus = books_counter.most_common(1)
    web_focus = webs_counter.most_common(1)
    if book_focus:
        recent_focus += book_focus[0][0] + ','
    if web_focus:
        recent_focus += web_focus[0][0]
    tags['推断特征']['近期关注内容'] = recent_focus

    # 近期经济状况，看近三个月贷款记录
    loan_frequency = 0
    for tag, content in json.loads(tags['贷款记录']).items():
        if datetime.datetime.strptime(content['时间'], "%Y-%m-%d") > three_month_ago:
            loan_frequency += 1
    if loan_frequency > 4:
        tags['推断特征']['近期经济状况'] = '不佳'
    elif loan_frequency > 2:
        tags['推断特征']['近期经济状况'] = '良好'
    else:
        tags['推断特征']['近期经济状况'] = '稳定'

    return tags


class TagUtils:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(**config.db_config)
        self.cursor = self.conn.cursor()

    def is_tag_exist(self, tag_name) -> bool:
        """
        判断标签是否存在
        """
        sql = 'select * from sys_label where name = "' + tag_name + '"'
        self.cursor.execute(sql)
        return self.cursor.fetchone() is not None


tagUtils = TagUtils()

'''
neo4j数据库
'''
driver = GraphDatabase.driver(config.NEO4J_URI)
