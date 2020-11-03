from random import seed
from random import randint
import math


#6x3 Grid representing StateofDespair
row_num = int(6)
col_num = int(3)
SoD = [[0 for col in range(col_num)] for row in range(row_num)]

#Randomly populate cells with 1s or 0s
for row in range(row_num):
    for col in range(col_num):
        SoD[row][col]= randint(0,1)

#print StateofDespair
print("State of Despair")
i = 0
while i < len(SoD):
    print(SoD[i])
    i += 1

#Divide StateofDespair into 6 districts [list of coordiante pairs, each pair represents a member cell and must be adjacent to one another]
#Ensure every cell is assigned a district & balance distric sizes
#Easiest approach - each row is a district
d = 0
while d < len(SoD):
    d1 = SoD[d]
    districtNumber = d + 1
    v = SoD[d][0] + SoD[d][1] + SoD[d][2]
    if  v >= 2:
        r = 1
    else:
        r = 0
    txt = "District {}: {} - candidate {} wins"  
    print(txt.format(districtNumber, d1, r))
    d += 1
      
