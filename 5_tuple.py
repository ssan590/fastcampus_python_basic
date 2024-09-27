# 빈 튜플 생성
my_tuple = (1,) # 하나의 값만 넣을때 콤마를 넣어서 이 내용이 튜플이라는걸 정의

# 과일 바구니
fruits  = ("apple", "banana", "blueberry")
first = fruits[0]
# print(first)

# 패킹과 언패킹
# tp = 1, 2, 3 # 콤마로 연결해 바로 튜플 생성 가능
# print(tp)

# v1, v2, v3 = tp # 독립된 변수에 언패킹 가능
# print(f"{v1}, {v2}, {v3}")

a = 10
b = 20

a, b = b, a # a와 b의 값을 변경 (자바처럼 a, b, temp를 써서 할당 할 필요가 없음)
# print("a: ", a)

tp = (1, 2, 3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals, _ = tp # 순서대로 1,2,3 저장 되다가 vals에서 나머지 값들이 list로 저장됨 ("_" 는 해당 값 안넣겠다는 뜻)
print(vals)

vals.append(9) #append 연산 가능
print(vals)