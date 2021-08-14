# 数据更新（选layers/选sentence/token时直接清除svg重画太过粗暴，或许可以优化？（暂时先放一边，等link以后再返工）
# layer选8-9 9-10 8-10 8-11 时 路径绘制有问题？？？

# 目前已完成：
# tsne视图的基本功能（选取layers，绘制路径）
# tokentable视图（暂未着色，之前拿数据的时候就发现saliency score的获取有点问题，不过这个可以等大体link后再说）
# sentencetable视图（双击选取句子，对应更新tokentable，单击index/prob可对sentences排序，暂未用色标着色/滑条取值，同样属于以后再说的细节）（但是tokentable到scatterplot(tsne)的link还没做。

# 这周结束前（明天打球前）应该做好的：

# 把tokentable和tsne联动（选tokens），后续思路：
# on/emit dispatchtokentoappend/dispatchtokentoappenddelete 传递双参数（sentence的index和token的index，然后去tsne_100.json里面找）
# 注：sentencetable向tokentable传参时应补上sentence index，可以在tokentable的data中补一个sentence index参数，然后tokentable向scatterplot传参时就很自然的双参数

# 做好attr-tree的阈值动态控件与后端python的接口（阈值传给flask，flask传给attibution tree.py）（python文件的启动参数再加一个）  