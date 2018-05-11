def water_melon(n):
    string = ''
    for i in range(1,n+1):
        if i % 2 != 0:
            string = string + "수"
        else:
            string = string +"박"

    return string
   


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(9))
print("n이 4인 경우: " + water_melon(4))

