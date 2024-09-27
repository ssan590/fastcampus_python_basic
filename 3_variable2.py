# 문자열 변수 선언
str_var = "This is my python code."
mulit_line = """I'm a developer
I use python.
Thank you."""

# print(str_var)
# print(mulit_line)

# 문자열 더하기
inum1 =12
inum2 =34
# print(inum1 + inum2) # 46

snum1 = "12"
snum2 = "34"
# print(snum1 + snum2) #1234
# print(snum1 * 3 ) #121212

# 인덱싱
# print(str_var[11]) # p
# print(str_var[-1]) # .
# print(str_var[-5]) # c

# 슬라이싱
# print(str_var[11:17]) # python
# print(str_var[11:-6]) # python
# print(str_var[:10]) # This is my

# print(str_var.isalpha()) # 알파벳으로만 구성되어있는가?(공백, 마침표가 있기 때문에 False)
str_var2 = "Thisismypythoncode"
# print(str_var2.isalpha()) # True

num_var = "12"
# print(num_var.isdecimal()) # True

# print(str_var.upper()) # 대문자로 변경

# print(str_var.swapcase()) # 대문자는 소문자로, 소문자는 대문자로 변경

# print(str_var.replace("my", "your")) # 기존 문자(my)롤 지정 문자(your)로 변경

## Format String
weather = "흐림"
temp = 15.8
# % code (%s, %d, %f)
# res = "[%s / %f도] 오늘의 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp) # 똑같은 변수를 재사용 할시 불필요한 중복 넣어야함
# print(res)

# .format()
res = "[{0} / {1}도] 기온은 {1}도 입니다. 오늘의 날씨는 {0} 입니다. ".format(weather, temp)
# print(res)

# f"""
# print(f"오늘 날씨는 {weather} 입니다. 기온은 {temp}도 입니다.")

# 사용자로부터 값을 입력받기
# print("숫자를 입력해주세요.")
inp = input("숫자를 입력해주세요.")
print("입력받은 숫자는" + inp)

# 받은 값을 1 더해서 출력하기
num = int(inp) + 1

print(f"입력받은 값에 1을 더하면, {num} 입니다")