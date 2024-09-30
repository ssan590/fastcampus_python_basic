# for loop
# for i in range(1, 5):
#     print(i)

# for 문이 끝나고 else 실행
# for i in range(1, 5):
#     print(i)
# else:
#     print("반복이 완료되었습니다.")

# fruits = ["사과", "딸기", "복숭아", "참외"]

# for fruit in fruits:
#     if fruit == "사과":
#         print(f"사과는 맛있습니다.")
#     1
#     print(f"{fruit}가 과일 바구니에 있습니다.")

# while
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1

# 상황에 따라 무한루프를 만들필요가 있으며 항상 무한 루프를 빠져 나올수 있는 식을 넣어야 한다
# while True:
#     user_input = input("명령어를 입력해주세요: ")
#     if user_input == "exit":
#         break
#     else:
#         pass # TODO: 차후 개발 에정

# 구구단 프로그램
# 1단~9단, n * 1 ~ n * 9
# for x in range(1, 10):
#     for y in range(1, 10):
#         print(f"{x} * {y} = {x * y}")

# enumerate 활용하기
fruits = ["Apple", "Banana", "Blueberry", "Peach"]

# index = 1
# for fruit in fruits:
#     print(f"{index}번째 과일은 {fruit} 입니다.")
#     index = index + 1

# 위 예시를 enumerate 활용하여 변경

# for index, fruit in enumerate(fruits, start = 1):
#     print(f"{index}번째 과일은 {fruit} 입니다.")

# 팩터리얼 구하기
# n! = n * (n - 1) * ... * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
num = 10
result = 1

for i in range(1, num + 1):
    result = result * i

print(f"{num}! 은 {result} 입니다.")