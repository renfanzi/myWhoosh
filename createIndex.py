#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
import pymysql
import os
from whoosh.index import create_in
from jieba.analyse import ChineseAnalyzer
from decimal import Decimal
from whoosh.fields import Schema, TEXT, ID

analyzer = ChineseAnalyzer()


#  创建索引文件


def parse_db(indexname, schema, indexdir):
    """
    注意， 如果更新数据，在创建和添加的时候， 某个字段必须唯一， 才OK， 同是在更新的时候， 也要有那个唯一字段
    :param indexname: 这里的indexname  ==》 当分类搜索的时候就是根据这个indexname来的
    :param schema: # 初始空字符， 然后进来拼接
    :param indexdir: 索引目录
    :return:
    """
    keys = {"ID": "abc", "content": "撸啊撸啊德玛西亚"}  # 表示从数据库得到的模拟数据
    s = "Schema("
    for key in keys:
        if key == "ID":
            s += key.replace('\n', '').replace('/r', '').replace('\t', '').replace(' ',
                                                                                   '') + '=ID(stored=True, unique=True), '
        else:
            s += key.replace('\n', '').replace('/r', '').replace('\t', '').replace(' ',
                                                                                   '') + '=TEXT(stored=True, analyzer=analyzer), '
            # TEXT(stored=True, analyzer=analyzer) 其实就是结合分词了

    s = s.rstrip(", ")
    s += ")"
    # print(s) # Schema(ID=TEXT(stored=True, analyzer=analyzer), content=TEXT(stored=True, analyzer=analyzer))
    schema = eval(s)
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)

    ix = create_in(indexdir, schema=schema, indexname=indexname)  # from whoosh.index import create_in 创建索引文件

    writer = ix.writer()  # 写入变成索引文件

    docline = """writer.add_document("""
    for key in keys:
        val = keys[key]

        if not val:
            val = ""
        elif isinstance(val, (Decimal,)):
            val = str(val)

        else:
            val = pymysql.escape_string(str(val))
        docline += key + '="' + val + '", '
    docline = docline.rstrip(", ")
    docline += """)"""
    # print(docline) # writer.add_document(content="撸啊撸啊德玛西亚", ID="abc")
    exec(docline)
    writer.commit()


def escape(s, obj="’"):
    ret = ''
    for x in s:
        if x == obj:
            ret += '\\'
        ret += x
    return ret


def app():
    indexdir = "indexdir"
    dbname = 'test'
    parse_db(indexname=dbname, schema="", indexdir=indexdir)


if __name__ == '__main__':
    app()

