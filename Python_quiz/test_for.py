def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    # list1 = list(str(number))
    # res = 0
    # for i in list1:
    #     i = int(i)
    #     res += i
    # return res
    return sum([int(i) for i in str(number)])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))

# sum 함수는 리스트 원소의 합을 구해준다
# sum 함수를 공부해보자
