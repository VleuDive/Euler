def get_next_hail(num):
    if num%2==0:
        return num/2
    else:
        return 3*num+1

count=0
max_count=0
max_seed=1
for seed in range(1,1000001):
    hail=get_next_hail(seed)
    while hail!=1:
        count+=1
        hail=get_next_hail(seed)
    if max_count<count:
        max_count=count
        max_seed=seed
print(max_seed)

