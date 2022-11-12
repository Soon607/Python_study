# iter는 객체의 _iter_ 메서드를 호출해주고, next는 객체의 _next_메서드를 호출해줌
# iter는 반복가능한 객체에서 이터레이터를 반환하고, next는 이터레이터에서 값을 차례대로 꺼냄

it=iter(range(3)) 
print(next(it))
print(next(it))
print(next(it))
print(next(it))

