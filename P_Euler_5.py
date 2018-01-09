"""
해당 범위 내 모든 수의 최소공배수
: 범위 내에 나열된 숫자가 많으므로, 2개만 있을 때와는 다른 방법 필요
재귀는 깊이가 깊어질수록 효율성이 급하락. 다른 방법?
"""
def gcd(num1,num2):
    while(num2!=0):
        temp=num1%num2
        num1=num2
        num2=temp
    return abs(num1)
    
def find_partial_lcm(num1,num2):
    mul=num1*num2
    div=gcd(num1,num2)
    part_lcm=mul/div
    return part_lcm

#lcm을 첫 2개 수에 대해 구하고, 그 lcm과 다음 수의 lcm을 구하고...

def find_total_lcm(range_limit):
    lcm=0
    num_list=[]
    for i in range(1,range_limit+1):
        num_list.append(i)
    lcm=find_partial_lcm(num_list[0],num_list[1])
    for i in range(2,len(num_list)):
        lcm=find_partial_lcm(lcm,num_list[i])
    return lcm

print(find_total_lcm(20))
