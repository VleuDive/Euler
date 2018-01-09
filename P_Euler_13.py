import numpy as np
f=open("P_13.txt",'r')
numlist=[]
numlist=np.loadtxt('P_13.txt', dtype=float,delimiter='\n')
f.close()
def get_sum(list):
    sum=0
    for num in list:
        sum+=int(num)
    return str(sum)

res=get_sum(numlist)
print(res[:10])