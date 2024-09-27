my_dict = {}
my_dict["key"] = "value"

# print(my_dict)

person = {"name" : "홍길동", "age" : "30", "city" : "서울"}

name = person["name"]
# print(name)

# print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.") #쌍따옴표 안에는 홀따옴표 사용

# country = person["country"]

# print(country) # 존재하지 않은 키를 불러서 키 에러 발생

country = person.get("country", "알 수 없음") #get을 사용하여 없을 경우 에러없이 실행 할 수 있다
# print(country)

person["age"] = 35 # 기존 키 값 수정

person["country"] = "대한민국" # 신규 키 값 추가

person_detail = {"country" : "대한민국", "married" : True}

person.update(person_detail) # 기존 딕셔너리에 신규 딕셔너리 병합

country = person.get("country", "알 수 없음")

# print(f"국젹은 {country} 입니다.")

# print(person.keys()) #person 딕셔너리가 가지고 있는 키 들 확인

del person["married"] # 특정 키 삭제

print(person.keys())