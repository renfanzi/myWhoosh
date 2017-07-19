#!/usr/bin/env python
# -*- coding:utf-8 -*-

from whoosh.filedb.filestore import FileStorage
from whoosh.index import exists_in, open_dir
from whoosh.qparser import MultifieldParser

# 这个代码需要更正了增量索引以后，由于多个索引文件前面重复而造成的数据重复．
def app():
    indexdir = "indexdir"
    storage = FileStorage(indexdir)

    fname = storage.list()  # ['dinosaur.db_loh0qsax01wwdijy.seg', 'dinosaur.db_WRITELOCK', 'mmorpg.db_1mwe4pojwea459cm.seg', 'mmorpg.db_WRITELOCK',
    print("fname", fname)
    indices = []  # [FileIndex(FileStorage('indexdir'), 'dinosaur.db'), FileIndex(FileStorage('indexdir'), 'mmorpg.db'), FileIndex(FileStorage('indexdir'), 'superfamicom.db')]
    # for f in fname:
    #     if not f.endswith(".seg"):
    #         continue
    #     ind = f.split('_')[0]
    #     print(ind)
    #
    #     if exists_in(indexdir, indexname=ind):
    #         indices.append(open_dir(indexdir, ind))
    indList = ["metaproject", "metaquestionnaire", "metavariable"]
    for ind in indList:
        indices.append(open_dir(indexdir, ind))
    print(indices)
    search(indices)


def search(indices):
    inpval = 2
    # ----------》以上就是得到按照哪种分类搜索
    qparsers = []

    print("全文索引")
    categories = []
    for ix in indices:  # to be able to search through all the keys
        categories.extend(list(ix.schema._fields.keys()))
        qparsers.append(MultifieldParser(categories,
                                         ix.schema))  # let user search through multiple fields with multifield parser

    print("你要查询的内容:")
    inp = input("--->")

    data = inp.split('<==>')
    queries = [qparsers[i].parse(data[0].strip()) for i in range(0, len(qparsers))]

    if len(data) > 1:
        limits = int(data[1].strip())
        limits = 10

    # limits 为显示结果的数量
    results = []
    stats = {}

    for i in range(0, len(indices)):
        # indices: [FileIndex(FileStorage('indexdir'), 'dinosaur.db'),
        searcher = indices[i].searcher()
        res = searcher.search(queries[i], limit=None)

        if len(res) != 0:
            # ix.indexname--> superfamicom.db
            stats[indices[i].indexname] = len(res)
        else:
            continue
        results.extend(res)

    # print(results)
    my_result = []
    for i in results:
        my_result.append(dict(i))

    print(my_result)



if __name__ == '__main__':
    app()
