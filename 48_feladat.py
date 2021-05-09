import numpy as np
import random
kep=np.random.randint(0,2,(5,20))
nulla=np.random.randint(0,1,kep.shape[1])
nulla[random.randint(0,kep.shape[1]-1)]=1
for i in range(1,kep.shape[0],2):
    husszazalek=np.array([np.random.randint(0, 2, kep.shape[1]), np.random.randint(0, 2, kep.shape[1]), np.random.randint(0, 2, kep.shape[1]), np.random.randint(0, 2, kep.shape[1]), nulla])
    np.random.shuffle(husszazalek)
    kep[i:i+1:]=husszazalek[:1:]
print(kep)

def atalakito(kep):
    for i in range(0,kep.shape[0]):
        db=0
        for j in range(0,kep.shape[1]):
            if kep[i,j]==1:
                db+=1
        if db>1:
            ind=0
            kezd=0
            for h in range(0,kep.shape[1]):
                if kep[i,h]==1:
                    kezd=h
                    break
            for l in range(0,kep.shape[1]):
                if kep[i,l]==1:
                    ind=l
            for k in range(kezd,ind):
                kep[i,k]=1
    return kep

print(atalakito(kep))