#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

    writer.update_document(content="人在塔在===加了修改", ID="hik")
    # Because "path" is marked as unique, calling update_document with path="/a"
    # will delete any existing documents where the "path" field contains "/a".
    # writer.update_document(path=u"/a", content="Replacement for the first document")
    writer.commit()

if __name__ == '__main__':
    indexname = "test"
    indexdir = "indexdir"
    incremental_index(indexdir, indexname)
