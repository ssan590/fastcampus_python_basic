# # 사용자로부터 두 개의 값을 입력 받는다.
# var1 = input("첫 번쨰 값을 입력해주세요: ")
# var2 = input("두 번쨰 값을 입력해주세요: ")

# # 입력값을 숫자로 변환
# num_var1 = int(var1)
# num_var2 = int(var2)

# # 첫 번째 값이 크다면 "Win", 두 번쨰 값이 크다면 "Lose"를 출력한다.
# # 두 값이 같다면, "Draw"를 출력한다.
# if num_var1 > num_var2:
#     print("Win")
# elif num_var1 < num_var2:
#     print("Lose")
# else:
#     print("Draw")




# 점수를 입력 받는다.
score_str = input("점수를 입력해주세요: ")
score = int(score_str)

# # 점수가 비정상 범위이면, 아무것도 실행하지 않는다.
# if score > 99 or score < 1:
#     print("잘못된 입력 값입니다.")
# # 점수의 각 등급에 따른 결과를 출력한다. (A: 90~99, B: 80~89, C:70~79, D:60~69, F: ~59)
# else:
#     if score >= 90:
#         print("등급은 A입니다.")
#     elif score >= 80:
#         print("등급은 B입니다.")
#     elif score >= 70:
#         print("등급은 C입니다.")
#     elif score >= 60:
#         print("등급은 D입니다.")
#     else:
#         print("등급은 F입니다.")

if score <= 99 and score >= 90: # A
    grade = "A"
elif score <=89 and score >= 80: # B
    grade = "B"
elif score <=79 and score >= 70: # C
    grade = "C"
elif score <=69 and score >= 60: # D
    grade = "D"
elif score <=59 and score >= 1: # F
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"등급은 {grade}입니다.")