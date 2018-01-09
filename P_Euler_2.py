def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def ifEven(num):
    if(num%2==0):
        return True
    else:
        return False

def ifUnderLimit(num,limit):
    if(num<=limit):
        return True
    else:
        return False

fiblist=[]
idx=0
sum=0
while True:
    print(idx)
    num=fib(idx)
    if(ifUnderLimit(num,4000000)):
        if(ifEven(num)):
            fiblist.append(num)
        idx+=1
    else:
        break

for i in fiblist:
    sum+=i

print("The sum is: ",sum)
    
    
    
