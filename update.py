import sqlite3
import json
import time

def update(id, data):
    '''更改请求体为
    {
    "title": "string",
    "content": "string",
    "tags": ["string"],
    "source": "string"
    }
    '''
    try:
        # 更新指定信息
        conn = sqlite3.connect('database.db')
        conn.execute("PRAGMA foreign_keys = ON")
        cur = conn.cursor()
        updated_time = int(time.time())
        data['updated_at'] = updated_time         # 更新时间也要更新
        placeholders = ', '.join(f"{col} = ?" for col in data.keys())
        sql = f"UPDATE data SET {placeholders} WHERE id = ?"
        values = list(data.values()) + [id]         # 直接将values转为列表并添加id
        cur.execute(sql, values)
        # 更新整体数据库信息
        sql = "UPDATE basic_info SET timestamp=?"   # 改变更新时间戳
        cur.execute(sql, (updated_time,))
        conn.commit()
    except Exception as e:
        print(f"数据插入失败: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
