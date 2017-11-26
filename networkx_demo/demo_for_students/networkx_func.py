#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# 関数定義
# 引数は隣接リスト(list)，表示するノード数(int)，ノードの大きさを決める関数(func)，ノード間の反発力(float:0~1.0), 保存するファイル名保存しない場合は'NULL'(char)
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
    # 今回はネットワーク成長開始からmax_size個のグラフとしている
    sample_list = range(max_size, network_size)
    for item in sample_list:
        TestGraph.remove_node(item)

    # ネットワークの大きさを更新
    network_size = max_size

    # 各ノードの次数を格納するリスト
    node_degree = []
    for i in range(network_size):
        node_degree.append(TestGraph.degree(i))

    DrawGraph(TestGraph, node_degree, weight_func, dist, file_name)



# 次数が大きい順にグラフにかき出す関数
def OutputNGraphDescend(network_list, max_size, weight_func, dist, file_name):
    # ネットワークの大きさ
    network_size = len(network_list)
    #print(network_size)
    #print(max_size)
    # グラフの宣言
    TestGraph = nx.Graph()

    # ノードの追加．属性はなしなのでリストによる番号指定．
    TestGraph.add_nodes_from(np.arange(network_size))

    # リスト内のエッジ情報を追加
    for i in np.arange(network_size):
        for j in network_list[i]:
            TestGraph.add_edge(i, j)

    # 次数リスト作成
    # 各ノードの次数を格納するリスト
    node_degree = []
    for i in range(network_size):
        node_degree.append(TestGraph.degree(i))


    # 削除するノードを決める．
    # if (network_size != max_size):
    if (network_size > max_size):
        count = 1
        delite_node = []
        while True:
            for j in np.arange(network_size):
                if count == node_degree[j]:
                    delite_node.append(j)
                    if len(delite_node) == network_size - max_size:
                        break
            else:
                count = count + 1
                continue
            break

        # ノード削除
        for item in delite_node:
            TestGraph.remove_node(item)

        # 次数リスト整形
        #dellist(node_degree, delite_node)

        # 各ノードの次数を格納するリスト
        node_degree = []
        for item in TestGraph.nodes():
            node_degree.append(TestGraph.degree(item))


    DrawGraph(TestGraph, node_degree, weight_func, dist, file_name)


# 次数が小さい順にグラフにかき出す関数
def OutputNGraphAscend(network_list, max_size, weight_func, dist, file_name):
    # ネットワークの大きさ
    network_size = len(network_list)
    #print(network_size)
    #print(max_size)
    # グラフの宣言
    TestGraph = nx.Graph()

    # ノードの追加．属性はなしなのでリストによる番号指定．
    TestGraph.add_nodes_from(np.arange(network_size))

    # リスト内のエッジ情報を追加
    for i in np.arange(network_size):
        for j in network_list[i]:
            TestGraph.add_edge(i, j)

    # 次数リスト作成
    # 各ノードの次数を格納するリスト
    node_degree = []
    for i in range(network_size):
        node_degree.append(TestGraph.degree(i))


    # 削除するノードを決める．
    # if (network_size != max_size):
    if (network_size > max_size):
        count = np.max(node_degree)
        delite_node = []
        while True:
            for j in np.arange(network_size):
                if count == node_degree[j]:
                    delite_node.append(j)
                    if len(delite_node) == network_size - max_size:
                        break
            else:
                count = count - 1
                continue
            break

        # ノード削除
        for item in delite_node:
            TestGraph.remove_node(item)

        # 次数リスト整形
        #dellist(node_degree, delite_node)

        # 各ノードの次数を格納するリスト
        node_degree = []
        for item in TestGraph.nodes():
        # 重み0に対応するため+1するよ
            node_degree.append(TestGraph.degree(item)+1)

    DrawGraph(TestGraph, node_degree, weight_func, dist, file_name)



def DrawGraph(Graph, node_degree, weight_func, dist, file_name):
    # ノードの重みを格納するリスト
    node_weight = weight_func(np.array(node_degree))
    # print(node_weight)
    node_weight = np.ndarray.tolist(node_weight)

    # グラフ定義．大きさは適宜変更可能
    plt.figure(figsize=(10,10))

    # ノードの位置決定.kでノードごとの反発力
    pos = nx.spring_layout(Graph, k = dist)

    # ノードを描画.色，透明度は適宜調整
    nx.draw_networkx_nodes(Graph, pos, alpha = 0.7,node_size=node_weight)
    # エッジを描画.色，透明度は適宜調整
    nx.draw_networkx_edges(Graph, pos, width=1, alpha = 0.7, edge_color = 'b')
    plt.axis("off")

    if file_name != 'NULL':
        plt.savefig(file_name)
    plt.show()



def dellist(items, indexes):
    for index in sorted(indexes, reverse=True):
        del items[index]
