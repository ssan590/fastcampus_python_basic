my_list = [10, 20, 30]

# print(my_list)

my_list = [0, 1, 2]
my_list.append(10) # 요소추가
my_list.append(15)
my_list.append(888)

# print(my_list)

# print(len(my_list)) # 리스트 길이 확인

element = my_list[2] # 특정 요소 출력

# print(element)

sliced = my_list[3:] # 3번인덱스부터 마지막 요소까지 저장

# print(sliced)

fruits = ["banana", "apple", "blueberry", "cherry"]

# 바나나가 포함되어 있을까?
is_banana_included = "banana" in fruits
# print(is_banana_included)

# 체리는 어디에 있을까?
index_cherry = fruits.index("cherry") #체리의 인덱스가 몇인가?
# print(index_cherry)

# 리스트의 정렬
numbers = [4, 2, 1, 3, 8, 6, 7]
# print("Unsorted ", numbers)

numbers.sort() # 숫자를 정렬
# print("Sorted ", numbers)

numbers.sort(reverse=True) # 내림차순 정렬
# print(numbers)

# 리스트의 요소 추가 및 제거
my_list2 = []
my_list2.append(10)
my_list2.append(11)
my_list2.append(12)
# print(my_list2)


my_list2.extend([13, 14, 15]) # 리스트 확장
# print(my_list2)

# my_list2.append([16, 17]) # 복합 리스트의 형태로 들어가게 됨
# print(my_list2)
# print(my_list2[-1])


# 리스트 연산 (+, *)
new_list = my_list2 + [0, 1, 2] # 리스트에 새 요소 추가

# print(new_list)

multi_list = [0, 1, 3] * 3 # 리스트 곱한 만큼 반복
# print(multi_list)

# del my_list2[0] # 리스트의 특정 요소 제거
# print(my_list2)

max_value = max(my_list2) # 리스트의 최대값 도출
min_value = min(my_list2) # 리스트의 최소값 도출

print(f"최대값은 {max_value}, 최소 값은 {min_value} 입니다.")