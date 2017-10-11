#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os.path
from whoosh.filedb.filestore import FileStorage
from whoosh.index import FileIndex
from whoosh.writing import AsyncWriter


def incremental_index(indexdir, indexname):
    """
    注意这里，　每次增加索引都会产生一个新的ｓｅｇ文件，　会占用空间，　所以这里需要注意
    :param indexdir:
    :param indexname:
    :return:
    """
    # print(indexdir)

    storage = FileStorage(indexdir)
    ix = FileIndex(storage, indexname=indexname)

    writer = AsyncWriter(ix)

    writer.add_document(content="人在塔在", ID="hik")

    writer.commit()


if __name__ == '__main__':
    indexname = "test"
    indexdir = "indexdir"
    incremental_index(indexdir, indexname)
