import random

#iter(호출가능한객체, 반복을 끝낼값)

it=iter(lambda: random.randint(0,5),2) #2-반복을 끝낼값

#print(next(it))
#print(next(it))
#print(next(it))

for i in iter(lambda: random.randint(0,5),2):
    print(i,end=' ')
