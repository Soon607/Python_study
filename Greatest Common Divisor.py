# for 문으로 구하기

a=10
b=12

for i in range(min(a,b),0,-1): # min(a,b)에서 1까지 역순으로 숫자 생성
    if a%i==0 and b%i==0:      # 값이 모두 딱 떨어지면 i 는 a와 b의 최대 공약수이다.
        print(i)
        break
    
# 공통 약수들 중 가장 큰 것을 구하는 것이므로 for문을 주어진수 ~1까지 -1히면서 돌렸다.

# 최대공약수 함수

def GCD(X,Y):
    if X<Y:
        min=X
        
    else:
        min=Y
        
    for i in range(min+1,1,-1):
        if X%i==0 and Y%i==0:
            res=i
            break
    return res
        

# 유클리드 호제법

def GCD(x,y):
    while(y): #y가 참일 동안=자연수일 때: a%b!=0
        x,y=y,x%y
        
    return x

print(GCD(10,12)) #2 

# while(y)==True 일 경우 (y가 0 초과일 경우) x 자리에는 y값 y자리에는 x%y(r)의 값을 넣는다.
# y가 0이 될때 (x를 y로 나누어 떨어질 때) 그 y의 값은 x,y의 최대공약수이다.