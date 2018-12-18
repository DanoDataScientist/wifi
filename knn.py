import numpy as np


class Position:
    x = 0
    y = 0


db = {'loc_1': {'x': 260, 'y': 210, 'AP1': {'mean': -45.03, 'std': 2.44}, 'AP2': {'mean': -54.00, 'std': 1.65}},
      'loc_2': {'x': 510, 'y': 210, 'AP1': {'mean': -46.42, 'std': 0.81}, 'AP2': {'mean': -45.58, 'std': 2.54}},
      'loc_3': {'x': 510, 'y': 60, 'AP1': {'mean': -51.81, 'std': 1.44}, 'AP2': {'mean': -40.57, 'std': 4.68}},
      'loc_4': {'x': 260, 'y': 60, 'AP1': {'mean': -34.52, 'std': 0.59}, 'AP2': {'mean': -54.78, 'std': 2.19}}}

pos = {'AP1': {'mean': -40.00, 'std': 4.93}, 'AP2': {'mean': -44.31, 'std': 1.89}}

Euclidean_Dist = {'dist_1': 0, 'dist_2': 0, 'dist_3': 0, 'dist_4': 0}
weight = 0

for i in range(1, 5):
    for j in range(1, 3):
        Euclidean_Dist['dist_'+str(i)] += (pos['AP'+str(j)]['mean'] - db['loc_'+str(i)]['AP'+str(j)]['mean'])**2
    Euclidean_Dist['dist_'+str(i)] **= 1/2
    weight += 1/Euclidean_Dist['dist_'+str(i)]

p = Position()
for i in range(1, 5):
    p.x += 1/Euclidean_Dist['dist_'+str(i)]/weight * db['loc_'+str(i)]['x']
    p.y += 1/Euclidean_Dist['dist_'+str(i)]/weight * db['loc_'+str(i)]['y']

print(p.x, p.y)





