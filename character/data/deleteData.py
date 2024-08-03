from neo4j import GraphDatabase
import json

# 连接到Neo4j数据库
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri)


def main():
    with driver.session() as session:
        # 删除所有节点和关系
        session.run("MATCH (p:Person)-[r]-(t:Tag) DELETE r")
        session.run("MATCH (p:Person) DELETE p")
        session.run("MATCH (t:Tag) DELETE t")


if __name__ == "__main__":
    main()
