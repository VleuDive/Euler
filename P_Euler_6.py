def find_sum_of_square(range_limit):
    sum=0
    for i in range(1,range_limit+1):
        sum+=i**2
    return sum

def find_square_of_sum(range_limit):
    sum=0
    for i in range(1,range_limit+1):
        sum+=i
    return sum**2

print(find_square_of_sum(100)-find_sum_of_square(100))
