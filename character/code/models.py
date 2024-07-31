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
