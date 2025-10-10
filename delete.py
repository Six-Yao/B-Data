import sqlite3
import json
import time

def delete(id):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM data WHERE id=?", (id,))   #删除数据
        updated_time = int(time.time())
        sql = "UPDATE basic_info SET timestamp=(?)"         #改变更新时间戳
        cur.execute(sql, (updated_time,))
        conn.commit()
    except Exception as e:
        print(f"数据插入失败: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
