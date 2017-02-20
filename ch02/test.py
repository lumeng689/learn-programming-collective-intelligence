#!/usr/bin/env python
# coding:utf-8

from math import sqrt
from recommendations import critics
import recommendations

# 测试字典查询
print critics['Lisa Rose']['Lady in the Water']
critics['Toby']['Snakes on a Plane'] = 4.5
print critics['Toby']

# 测试计算平方根的方法
print sqrt(pow(4.5 - 4, 2) + pow(1 - 2, 2))

reload(recommendations)

print '欧几里得距离：'
print recommendations.sim_distance(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
print '皮尔逊相关系数：'
print recommendations.sim_pearson(recommendations.critics, 'Lisa Rose', 'Gene Seymour')

print '获得最匹配者：'
print recommendations.topMatches(recommendations.critics, 'Toby', n=3)

print '获取对Toby的推荐：'
print recommendations.getRecommendations(recommendations.critics, 'Toby')
print recommendations.getRecommendations(recommendations.critics, 'Toby', recommendations.sim_distance)

movies = recommendations.transformPrefs(recommendations.critics)
print '调换人与物品：'
print movies

print '打印相似类型的电影：'
print recommendations.topMatches(movies, 'Superman Returns')
print recommendations.getRecommendations(movies, 'Just My Luck')

# import pydelicious
# print pydelicious.get_popular(tag='programming')

# print '开始填充数据：'
# from deliciousrec import *
# delusers = initializeUserDict('programming')
# delusers['tsegaran'] ={}
# fillItems(delusers)
# print delusers

itemSim = recommendations.calculateSimilarItems(recommendations.critics)
print itemSim
print '基于物品推荐：'
print recommendations.getRecommendedItems(recommendations.critics, itemSim, 'Toby')

print '电影数据：'
prefs = recommendations.loadMovieLens()
print prefs['87']
print recommendations.getRecommendations(prefs, '87')[0:30]
itemSim2 = recommendations.calculateSimilarItems(prefs, n=50)
print recommendations.getRecommendedItems(prefs, itemSim2, '87')[0:30]

