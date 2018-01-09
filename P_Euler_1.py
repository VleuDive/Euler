def ifMultOfThree(num):
    if(num%3)==0:
        return True
    else:
        return False

def ifMultOfFive(num):
	if(num%5)==0:
		return True
	else:
		return False

sum=0
for n in range(1000):
    if(ifMultOfThree(n) or ifMultOfFive(n)):
        sum+=n
print(sum)
