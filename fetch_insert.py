import sqlite3
import json
import time


# 设想是当另一个程序检测到有需要输入的数据时调用一次这个函数，或许可以避免反复开关数据库带来的麻烦
def insert(json_data: dict):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    '''
    希望获得的数据形如：
    {
        'timestamp': 1145141919,
        'platform': 'YuQue',
        'property': 'Event',
        'tag': '["Nova", "Python", "SQLite"]',
        'creator': 'CAC',
        'content': 'Nova某组本周任务：学习SQLite语法并尝试用Python操作',
    }
    '''
    update_time = int(time.time())
    columns = list(json_data.keys())                # 获取JSON中的所有键，这些键应与表的列名对应
    placeholders = ', '.join(['?'] * len(columns))  # 根据列的数量构造参数占位符
    sql = f"INSERT INTO data ({', '.join(columns)}) VALUES ({placeholders})"   # 构造完整的SQL语句
    values = [json_data[col] for col in columns]    # 从JSON数据中提取值，确保顺序与列名顺序一致
    try:
        cur.execute(sql, values)
        sql = "UPDATE basic_info SET timestamp=(?)"   #改变更新时间戳
        cur.execute(sql, (update_time,))
        conn.commit()   # 5. 执行SQL语句并提交
        print(f"数据插入成功，ID: {cur.lastrowid}")
    except sqlite3.IntegrityError as e:
        print(f"数据插入失败，违反完整性约束 (如唯一性约束): {e}")
        conn.rollback()
    except Exception as e:
        print(f"数据插入失败: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def fetch():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row     # 将自定义的row_factory函数应用到Connection对象
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    results = []
    for row in cur.fetchall():
        row_dict = dict(row)
        results.append(row_dict)
    cur.execute("SELECT * FROM basic_info")
    data={"timestamp": cur.fetchone()[0], "data": results}
    return data