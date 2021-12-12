# Python program to read
# image using matplotlib
import math
# importing matplotlib modules
import matplotlib.image as mpimg
import sys
import matplotlib.pyplot as plt
import numpy as np
# Read Images

img = mpimg.imread('Lena.png')
iter=100
TamImagen=128
Division=4
Ri=[]
imgPrueba=img[0:TamImagen,0:TamImagen]


for i in range(int(TamImagen/Division)):
    for j in range(int(TamImagen/Division)):
        parteImagen=img[i*Division:(i+1)*Division,j*Division:(j+1)*Division]
        Ri.append(parteImagen)

Di=[]

for i in range(TamImagen-2*Division+1):
    for j in range(TamImagen-2*Division+1):
        parteImagen=img[i:(i+2*Division),j:(j+2*Division)]
        Di.append(parteImagen)

Fi=[]

for i in range(TamImagen-2*Division+1):
    for j in range(TamImagen-2*Division+1):
        parteImagen=(img[i:(i+Division),j:(j+Division)]+img[i+Division:(i+2*Division),j:(j+Division)]+img[i:(i+Division),j+Division:(j+2*Division)]+img[i+Division:(i+2*Division),j+Division:(j+2*Division)])/4
        Fi.append(parteImagen)

sumFi=[]
sumFi2=[]
for arr in Fi:
    normales=0
    for i in range(Division):
        for j in range(Division):
            normales += arr[i][j][0]
    sumFi.append(normales)
    cuadrados=0
    for i in range (Division):
        for j in range (Division):
            cuadrados+=arr[i][j][0]**2
    sumFi2.append(cuadrados)


Diopt=[]
Siopt=[]
Oiopt=[]
for arr in Ri:
    min = float('inf')
    minelem=0
    k=0
    sumRi = 0
    sitemp=0
    oitemp=0
    for i in range(Division):
        for j in range(Division):
            sumRi += arr[i][j][0]
    sumRi2 = 0
    for i in range(Division):
        for j in range(Division):
            sumRi2 += arr[i][j][0] ** 2
    for arr2 in Fi:
        arrab=arr+arr2
        sumab=0
        for i in range(Division):
            for j in range(Division):
                sumab += arr[i][j][0] + arr2[i][j][0]
        s=(Division*sumab-(sumRi*sumFi[k]))/(Division*sumFi2[k]-(sumFi[k]**2))
        o=1/Division*(sumRi-s*sumFi[k])
        R=1/Division*(sumRi2+s*(s*sumFi2[k]-2*sumab+2*o*sumFi[k])+o*(8*o-2*sumFi[k]))

        if(R<min):
            min=R
            minelem=k
            sitemp=s
            oitemp=o
        k+=1
    Diopt.append(minelem)
    Siopt.append(sitemp)
    Oiopt.append(oitemp)

values, counts = np.unique(Diopt, return_counts=True)
print(counts)

def w(i,z):
    return(Siopt[i]*z+Oiopt[i])

fk=np.zeros((TamImagen, TamImagen))

print("Siopt="+str(len(Siopt)))
print("Oiopt="+str(len(Oiopt)))
print("TAM/DIv="+str(TamImagen/Division))
for k in range(iter):
    for i in range(TamImagen):
        for j in range(TamImagen):
            fk[i][j]=w((math.floor(i/int(Division)))+(int(TamImagen/Division)*math.floor(j/int(Division))),fk[i][j])
# Output Images

plt.imshow(fk, cmap='gray')
plt.show()