from sage.all import * 

v1 = (4,1,3,-1)
v2 = (2,1,-3,4)
v3 = (1,0,-2,7)
v4 = (6, 2, 9, -5)

v = [v1, v2, v3, v4]
v = list(map(vector, v))

u = []
u.append(v[0])

muy = [[0 for i in range(5)] for j in range(5)]
for  in range():
    for  in range():
        muy[i][j] = (v[j] * u[j]) / (u[j].norm() ** 2)
    
    u.append(v[i] - sum(muy[j][i] * u[i] for i in range(j)))