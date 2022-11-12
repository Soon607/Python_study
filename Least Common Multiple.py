a=10
b=12

for i in range(max(a,b),(a*b)+1):
    if i%a==0 and i%b==0:
        print(i)
        break
    
# a,b 중 더 큰 숫자부터 a*b의 수까지 for문 실행
# 더 큰 숫자부터 실행하는 이유: a,b의 공통부분을 찾는 것이기 때문에 작은 수부터 시작하게 되면 큰 수에 도달할때까지 for문이 헛돌게 된다.
# 공통 배수들 중 가장 작은 것을 구하는 것이므로 for문을 주어진 수부터 +1을 하였다.

# 유클리드 호제법

def GCD(x,y):
    while(y): 
        x,y=y,x%y
        
    return x
    
def LCM(x,y):
    result=(x*y)/GCD(x,y)
    return result

print(LCM(10,12)) #60

 # x*y를 최대공약수로 나눈 몫이 최소공배수이다.       