#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# 関数定義
# 引数は隣接リスト(list)，表示するノード数(int)，ノードの大きさを決める関数(func)，ノード間の反発力(float:0~1.0), 保存するファイル名,保存しない場合は'NONE'(char)
def OutputNGraph(network_list, max_size, weight_func, dist, file_name):
    # ネットワークの大きさ
    network_size = len(network_list)

    # グラフの宣言
    TestGraph = nx.Graph()

    # ノードの追加．属性はなしなのでリストによる番号指定．
    TestGraph.add_nodes_from(np.arange(network_size))

    # リスト内のエッジ情報を追加
    for i in np.arange(network_size):
        for j in network_list[i]:
            TestGraph.add_edge(i, j)

    # max_size個のノードを取り出しそのグラフを取得する
    # 今回はネットワーク成長からmax_size個のグラフとしている
    sample_list = range(max_size, network_size)
    for item in sample_list:
        TestGraph.remove_node(item)

    # ネットワークの大きさを更新
    network_size = max_size

    # 各ノードの次数を格納するリスト
    node_degree = []
    for i in range(network_size):
        node_degree.append(TestGraph.degree(i))

    # ノードの重みを格納するリスト
    node_weight = weight_func(np.array(node_degree))
    # print(node_weight)
    node_weight = np.ndarray.tolist(node_weight)

    # グラフ定義．大きさは適宜変更可能
    plt.figure(figsize=(10,10))

    # ノードの位置決定.kでノードごとの反発力
    pos = nx.spring_layout(TestGraph, k = dist)

    # ノードを描画.色，透明度は適宜調整
    nx.draw_networkx_nodes(TestGraph, pos, alpha = 0.7,node_size=node_weight)
    # エッジを描画.色，透明度は適宜調整
    nx.draw_networkx_edges(TestGraph, pos, width=1, alpha = 0.7, edge_color = 'b')
    plt.axis("off")

    if file_name != 'NONE':
        plt.savefig(file_name)
    plt.show()
