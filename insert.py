import sqlite3
import json
import time

def insert(data: dict):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    '''
    希望获得的数据形如：
    {
    'author': 'CAC',
    'title': '某组活动安排',
    'tags': '["Nova", "Python", "SQLite"]',
    'source': 'yuque',
    'property': 'event',
    'content': 'Nova某组本周任务：学习SQLite语法并尝试用Python操作',
    }
    '''
    updated_time = int(time.time())
    data['created_at'] = updated_time
    data['updated_at'] = updated_time
    columns = list(data.keys())                     # 获取data中的所有键，这些键应与表的列名对应
    placeholders = ', '.join(['?'] * len(columns))  # 根据列的数量构造参数占位符
    sql = f"INSERT INTO data ({', '.join(columns)}) VALUES ({placeholders})"  # 构造完整的SQL语句
    values = [data[col] for col in columns]         # 从数据中提取值，确保顺序与列名顺序一致
    try:
        cur.execute(sql, values)
        cur.execute("UPDATE basic_info SET timestamp=?", (updated_time,))   #改变更新时间戳
        conn.commit()   # 执行SQL语句并提交
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
