#!/usr/bin/env python
# -*- coding:utf-8 -*-


from whoosh.filedb.filestore import FileStorage
from whoosh.index import exists_in, open_dir
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser


def selectApp(clientContent, indexflag=2):
    """

    :param clientContent:  客户端搜索的数据
    :param quesID:
    :param indexflag:
    :return:
    """
    indexdir = "/opt/code/my_code/myPythonTest/indexdir"

    # storage = FileStorage(indexdir)  # 这两句话在源码里面和open_dir是一样的, 故此注释掉
    # fname = storage.list()

    indices = []
    indList = ["test"]
    for ind in indList:
        indices.append(open_dir(indexdir, ind))

    ret = search(indices, indexflag, clientContent)
    return ret


def search(indices, indexflag, clientContent):
    inpval = indexflag
    qparsers = []
    if inpval == 1:
        categories = []
        for ix in indices:
            cat = list(ix.schema._fields.keys())
            for val in cat:
                if val in categories:
                    val = val + " - " + ix.indexname
                categories.append(val)

        for i in range(0, len(indices)):
            # qparsers.append(QueryParser(categories[inpval], indices[i].schema))
            qparsers.append(QueryParser("VarLebel", indices[i].schema))
    else:

        categories = []
        for ix in indices:
            categories.extend(list(ix.schema._fields.keys()))
            qparsers.append(MultifieldParser(categories,
                                             ix.schema))
    inp = clientContent

    data = inp.split('<==>')
    queries = [qparsers[i].parse(data[0].strip()) for i in range(0, len(qparsers))]

    if len(data) > 1:
        limits = int(data[1].strip())
        limits = 10

    results = []
    stats = {}  # 这个里面有几条数据 {'test': 1}

    for i in range(0, len(indices)):
        searcher = indices[i].searcher()
        res = searcher.search(queries[i], limit=10)
        if len(res) != 0:
            stats[indices[i].indexname] = len(res)
        else:
            continue
        results.extend(res)
    return results


if __name__ == '__main__':
    results = selectApp("hik")
    my_result = []
    for i in results:
        my_result.append(dict(i))
    print(my_result)
