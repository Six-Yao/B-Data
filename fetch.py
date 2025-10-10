import sqlite3
import json

def fetch_all():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row      # 使用字典格式存储数据
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, source, created_at, updated_at FROM data")
    results = []
    for row in cur.fetchall():
        row_dict = dict(row)
        results.append(row_dict)
    cur.execute("SELECT * FROM basic_info")
    data={"timestamp": cur.fetchone()[0], "data": results}
    cur.close()
    conn.close()
    return data

def fetch_by_id(id):
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT id, title, content, tags, source, created_at FROM data WHERE id={id}")
    results = []
    for row in cur.fetchall():
        row_dict = dict(row)
        results.append(row_dict)
    cur.execute("SELECT * FROM basic_info")
    data={"timestamp": cur.fetchone()[0], "data": results}
    cur.close()
    conn.close()
    return data
