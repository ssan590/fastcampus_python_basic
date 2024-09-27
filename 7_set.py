# empty_set = {} # 빈 중괄호 선언하면 딕셔너리로 인식한다!
empty_set = set()
my_set = {1, 2, 3, 3} # 중괄호를 사용하여 set 에 들어가는 값 지정, 중복 값은 버려진다

# print(my_set)

fruits = {"apple", "banana", "blueberry"}
fruits.add("orange") # orange 요소 추가
# print(fruits) # 출력할때마다 순서가 다르게 나옴, set은 요소의 순서를 보장하지 않는다

fruits.remove("orange") # orange 요소 제거
# print(fruits) 

fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}

# 합집합
union = fruits1.union(fruits2)
# print(union)
# print(fruits1 | fruits2) # 이 방식으로 합집합도 가능


# 교집합
intersection = fruits1.intersection(fruits2)
# print(intersection)

# 차집합(순사가 중요하다 A에서 B 차와 B에서 A 차의 값이 다르다)
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)

print("차집합 (F1 - F2): ", diff1)
print("차집합 (F2 - F1): ", diff2)