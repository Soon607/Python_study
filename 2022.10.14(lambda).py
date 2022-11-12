# 1. 람다(lambda) 함수
# 간단한 함수를 만들 때에 유용

def adder1(a,b):
    return a+b

adder2=lambda a,b: a+b

print(adder1(1,2))
print(adder2(1,2))
