from vpython import sphere, vector

L = 5
R = 0.3
for i in range(5):
    for j in range(5):
        for k in range(5):
            sphere(radius=R, pos=vector(i, j, k))