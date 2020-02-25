from DB.DBHelp import DBHelpMgr
from InitScript import InitDB
from Network import NetworkMgr

__author__ = 'Administrator'


def main():
    # 初始化db
    check_db()
    global network
    if not network:
        network = NetworkMgr.NetworkMgr()
    network.start_listen()
    while True:
        if not network.is_run:
            break
        network.loop()


def check_db():
    # 收集要创建的表
    need_create = {}
    for name in dir(InitDB):
        value = getattr(InitDB, name)
        database = getattr(value, "DATABASE", None)
        if not database:
            continue
        arr_table = need_create.get(database)
        if not arr_table:
            arr_table = need_create[database] = []
        arr_table.append(value)

    # 判断表是否创建
    for database, need_create_table in need_create.items():
        arr_table = []
        con_don = DBHelpMgr.get_database_connection(database)
        with con_don as cur:
            cur.execute("show tables;")
            result = cur.fetchall()
            for name in result:
                arr_table.append(str(name[0], encoding='utf8'))
            for value in need_create_table:
                if value.__name__ in arr_table:
                    continue
                value.execute(cur)



if __name__ == "__main__":
    network = None
    #main()
    check_db()
