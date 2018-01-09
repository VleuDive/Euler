import math as m

def findPrimeList(limit):
    prime_list=[2]
    if_prime=True
    for num in range(3,limit+1):
        if_prime=True
        for div in range(2,m.ceil(num**0.5)+1): #분모 range 설정 주의!
            if(num%div==0):
                if_prime=False
                break #여기서 break가 안되고 끝까지 훑고 지나가야만 소수!
        if if_prime:
            prime_list.append(num)
    return prime_list

def findFractList(num):
    fract_list=[]
    prime_list=findPrimeList(m.ceil(num**0.5)+1)
    for div in prime_list:
        if(num%div==0):
            fract_list.append(div)
    return fract_list

target_number=600851475143
fract_of_target=findFractList(target_number)
print(max(fract_of_target))
