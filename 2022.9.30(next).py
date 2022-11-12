# next

# 기본값을 지정할 수 있음
# 기본값을 지정하면 반복이 끝나더라도 Stopiteration이 발생하지 않고 기본값을 출력함
# 반복할 수 있을 때는 해당 값을 출력하고, 반복이 끝났을 때는 기본값을 출력함
# 예시는 range(3)으로 0,1,2 세번 반복하는데 next에 기본값으로 지정함

it=iter(range(3))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))
