

# myWhoosh = MySQL + Python + whoosh + jieba
python版本的搜索引擎  
属于python的搜索引擎  
# 注意：  
这个代码有点老， 可以看一下链接：https://github.com/renfanzi/myTornadoWhoosh  
就在上面， 也可以直接过去看， 其实那里边路径 common/myWhoosh/.... 的代码是myWhoosh代码的优化  
而且已经应用上线， tornado + whoosh + jieba + mysql 做的一个webserver的搜索引擎  

首先声明，　Whoosh的使用与Python的任何框架无关．  

# 存在可优化  
1. writer.add_document()... 这里先是字符串拼接， 然后exec， 有点little short  
2. 更新不应该继续用add_document(), 而是应该改用update_document()...有一天忽然看了眼源码猜想起来，但由于没有时间测试，所以没改，做一次笔记  


### 学习的思路：  
1. 创建搜索引擎结构， 有点类似于创建表结构， Schema(ID=ID(stored=True, unique=True), content=TEXT(stored=True, analyzer=analyzer))  
注意：  
a. 上面ID(stored=True, unique=True) 表示唯一的意思， unique=True， 关联到更新数据问题。  如果不唯一， 更新数据时候会多出一条数据  
b. 注意， 通常都会有个indexname， 这个就类似于sql的表名， 通过这个倒是还要搜索数据  

2. 写入数据， 有点类似于sql，writer.add_document(content="撸啊撸啊德玛西亚", ID="abc")  
3. 更新数据(删除数据一般也是伪删除)  
4. 查看数据  这个就是搜索的关键了  
注意:  
a. 全文索引  
b. 分类索引  


由于公司需求，加上搜索框，　选择搜索引擎，　由于我是写Ｐｙｔｈｏｎ的所以选择了ｗｈｏｏｓｈ．  
下面是学习方法和参考网站  

### 1. github上找代码，　然后学习
    参考网址：
        ｀｀｀
        https://github.com/spangatvir/Whoosh
        https://whoosh.readthedocs.io/en/latest/indexing.html#incremental-indexing
        https://mr-zhao.gitbooks.io/whoosh/content/%E5%A6%82%E4%BD%95%E7%B4%A2%E5%BC%95%E6%96%87%E6%A1%A3.html

        ｀｀｀

### 2. 简化案例代码

### 3. 查看官方文档

###
    总共历时10天解决搜索引擎问题

    做次记录, 防止以后忘记
