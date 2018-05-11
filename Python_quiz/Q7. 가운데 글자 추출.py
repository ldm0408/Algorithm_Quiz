'''getMiddle메소드는 하나의 단어를 입력 받습니다. 단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요. 단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.
'''


def string_middle(str):
    if len(str) % 2 == 0:
        return str[len(str) // 2-1: len(str) // 2+1]
    else:
        return str[len(str) // 2]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("powerk"))
print(string_middle("powe"))

# 나누기를 할 때 '/' 연산자는 소숫점을 포함하지만 '//'는 소숫점 이하를 버린다
# 문자열의 인덱스에는 정수만 가능하다
# 6 / 2 = 3.0    -->   6 // 2 = 3   --> 전자는 소수점이하가 존재하여 인덱스 값으로 사용 불가
