# 단일 조건 조건문
value = 30

# # 이 값이 20을 초고화는 경우, Big! 이라는 메세지를 출력
# if value > 20:
#     print("Big!")

# # 복합 조건문

# #  20보단 큰 경우 Big, 그렇지 않은 경우 Small
# value = 10
# if value > 20:
#     print("Big!")
# else:
#     print("Small")

# 50보다 큰 경우 Greate, 50보다 작거나 같고 20보단 큰 경우 Big, 그렇지 않은 경우 Small
# value = 39
# if value > 50:
#     print("Great")
# elif value > 20:
#     print("Big")
# else:
#     print("Small")



# 날씨가 흐리고, 강수확률이 70% 이상이면 -> 비가 온다.

condition = "맑음"
rain_rate = 0.70

if condition is "흐림" and rain_rate >= 0.70:
    print("비가 올 확률이 높습니다.")
elif condition is "흐림":
    print("날씨가 많이 흐립니다.")
elif condition is "맑음" and rain_rate >= 0.70:
    print("맑지만 비가 올 확률이 높습니다.")
else:
    print("날씨가 맑습니다.")