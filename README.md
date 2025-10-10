# B-Data

针对NOVA所需“统一信息平台”制定的数据存储规范草案
以及简单的数据读写函数

## 规范

<table>
    <tr>
        <th>属性(Key)</th><th colspan="3">可选参数(Value)</th><th>备注</th>
    </tr>
    <tr>
        <td>timestamp</td><td colspan="3">[int]</td><td></td>
    </tr>
    <tr>
        <td rowspan="9">data</td><td rowspan="9">[list[dict[str,any]]]</br>右表为字典键值对参数</td><td>id</td><td>int</td><td>张润程给出的是[str]但是sqlite自动生成的是[int]</br>或许要后续协商一下</td>
    </tr>
    <tr>
        <td>source</td><td>yuque|wechat|qq|web</td><td>显然不能涵盖全部，待补充</td>
    </tr>
    <tr>
        <td>property</td><td>recruit|event|announcement|share|change|[etc]</td><td>显然不能涵盖全部，待补充</br>个人认为有这个词条可以使推送更准确，所以加上了</td>
    </tr>
    <tr>
        <td>created_at</td><td>[int]</td><td></td>
    </tr>
    <tr>
        <td>updated_at</td><td>[int]</td><td></td>
    </tr>
    <tr>
        <td>title</td><td>[str]</td><td></td>
    </tr>
    <tr>
        <td>tags</td><td>[list[str]]</td><td>SQLite无法存储[list], 需要转化一下</td>
    </tr>
    <tr>
        <td>content</td><td>[str]</td><td>具体形式待议</td>
    </tr>
    <tr>
        <td>author</td><td>[str]</td><td></td>
    </tr>
    <tr><td colspan="5" style="text-align: center"><b>欢迎补充！</b></td></tr>
</table>

## 函数的功能

### insert(data: dict)
传入一个字典格式的数据，存储于`database.db`中
```
{
    'author': 'CAC',
    'title': '某组活动安排',
    'tags': '["Nova", "Python", "SQLite"]',
    'source': 'yuque',
    'property': 'event',
    'content': 'Nova某组本周任务：学习SQLite语法并尝试用Python操作',
}
```

### fetch_all()
返回一个字典, 获取所有信息的概况
```
{
    'timestamp': 1145141919,
    'data':[
        {
        'id': 1
        'title': '某组活动安排',
        'author': 'CAC',
        'source': 'yuque',
        'created_at': 1145141919,
        'updated_at': 1145141919
        },
    ]
}
```

### fetch_by_id(id)
返回一个字典, 获取指定信息的具体内容
```
{
    'timestamp': 1145141919,
    'data':[
        {
        'id': 1
        'title': '某组活动安排',
        'content': 'Nova某组本周任务：学习SQLite语法并尝试用Python操作',
        'tags': '["Nova", "Python", "SQLite"]',
        'source': 'yuque',
        'created_at': 1145141919,
        },
    ]
}
```

### update(id, data)
更新指定信息的部分内容

请求体, 传入`data`内：
```
{
    "title": "string",
    "content": "string",
    "tags": ["string"],
    "source": "string"
}
```

### delete(id)
删除指定信息