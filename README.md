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
        <td rowspan="6">data</td><td rowspan="6">[list[dict[str,any]]]</br>右表为字典键值对参数</td><td>platform</td><td>JW/ AMA/ WCOA/ YuQue</td><td>WCOA指微信公众号</td>
    </tr>
    <tr>
        <td>property</td><td>Recruit/ Event/ Announcement/ Share/ Change/ [etc]</td><td>显然不能涵盖全部，待补充</td>
    </tr>
    <tr>
        <td>tag</td><td>[list[str]]</td><td></td>
    </tr>
    <tr>
        <td>creator</td><td>[str]</td><td></td>
    </tr>
    <tr>
        <td>content</td><td>[str]</td><td>建议用markdown格式上报，统一用渲染器渲染</td>
    </tr>
    <tr>
        <td>timestamp</td><td>[int]</td><td>上面那个是更新时间，这个是信息发出时间</td>
    </tr>
    <tr><td colspan="5" style="text-align: center"><b>欢迎补充！</b></td></tr>
</table>

## 函数的功能

### insert(data: dict)
传入一个字典格式的数据，存储于`database.db`中
```
{
    'timestamp': 1145141919,
    'platform': 'YuQue',
    'property': 'Event',
    'tag': '["Nova", "Python", "SQLite"]',
    'creator': 'CAC',
    'content': 'Nova某组本周任务：学习SQLite语法并尝试用Python操作',
}
```

### fetch()
返回一个字典
```
{
    'timestamp': 1145141919,
    'data':[
        {
        'timestamp': 1145141919,
        'platform': 'YuQue',
        'property': 'Event',
        'tag': '["Nova", "Python", "SQLite"]',
        'creator': 'CAC',
        'content': 'Nova某组本周任务：学习SQLite语法并尝试用Python操作',
        },
    ]
}
```
