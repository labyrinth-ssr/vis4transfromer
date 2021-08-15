# 数据更新（选layers/选sentence/token时直接清除svg重画太过粗暴，或许可以优化？（暂时先放一边，等link以后再返工）
# layer选8-9 9-10 8-10 8-11 时 路径绘制有问题？？？

# 8.14 21:00更新：
# tsne视图的基本功能（选取layers，绘制路径）
# tokentable视图（暂未着色，之前拿数据的时候就发现saliency score的获取有点问题，不过这个可以等大体link后再说）
# sentencetable视图（双击选取句子，对应更新tokentable，单击index/prob可对sentences排序，暂未用色标着色/滑条取值，同样属于以后再说的细节）（但是tokentable到scatterplot(tsne)的link还没做。

# 8.15 17:00更新：已完成ABC三个视图的基本link，tokentable到tsne用单击事件管理

# 待解决的问题：
# 当绘制多条曲线时，有时会出现第一条曲线起点偏移的情况（只选择一个token时绘制不会）
# 要给line增加arrow/在末端增加一直显示的文字标识以方便阅读