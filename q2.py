

#not finish

#
# from typing import Callable, Any
# from sys import maxsize
# from itertools import permutations
# V = 4
# answer = []
#
# def partition(algorithm: Callable, graph: list, s, path):
#         return algorithm(graph, s, path)
#
#
# def NaivTSP(graph, s):
#     # store all vertex apart from source vertex
#     vertex = []
#     for i in range(V):
#         if i != s:
#             vertex.append(i)
#
#     # store minimum weight Hamiltonian Cycle
#     min_path = maxsize
#     next_permutation = permutations(vertex)
#     for i in next_permutation:
#
#         # store current Path weight(cost)
#         current_pathweight = 0
#
#         # compute current path weight
#         k = s
#         for j in i:
#             current_pathweight += graph[k][j]
#             k = j
#         current_pathweight += graph[k][s]
#
#         # update minimum
#         min_path = min(min_path, current_pathweight)
#
#     return min_path
#
#
# def BackTrackingTSP(graph, nodes, currPos, n, count, cost):
#     if (count == n and graph[currPos][0]):
#         answer.append(cost + graph[currPos][0])
#         return
#     for i in range(n):
#         if (nodes[i] == False and graph[currPos][i]):
#             # Mark as visited
#             nodes[i] = True
#             BackTrackingTSP(graph, nodes, i, n, count + 1,
#                             cost + graph[currPos][i])
#
#             # Mark ith node as unvisited
#             nodes[i] = False