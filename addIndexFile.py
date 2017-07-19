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
    print(indexdir)

    a = os.path.exists(indexdir)
    print(a)

    storage = FileStorage(indexdir)
    ix = FileIndex(storage, indexname=indexname)

    writer = AsyncWriter(ix)

    writer.add_document(OrderNum="116", VarStatus="1", OriginQuestion="Null", VarWidth="5",
                        VarValues="{\'1.0\': \'是\', \'2.0\': \'否\'}", VarNote="Null",
                        ReviseTime="2017-07-16 14:07:22", VarMeasure="", DeriveFrom="Null", VarType="INT",
                        VarLabel="德玛西亚",
                        VarVersion="1", OtherLangLabel="Null", VarTopic="Null", VariableID="10051",
                        OriginFormats="F5.0", VarDecimals="0", DataFrom="",
                        DataTableID="2017071614072101732838504760", ReviseFrom="", VarName="Q34R54",
                        VarMissing="Null", ReviseUserID="", VarRole="")

    writer.commit()


if __name__ == '__main__':
    indexname = dbname = "metavariable"
    indexdir = "indexdir"
    incremental_index(indexdir, indexname)
