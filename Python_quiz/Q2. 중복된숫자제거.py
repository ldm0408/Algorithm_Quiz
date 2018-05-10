def no_continuous(s):
    # 함수를 완성하세
    # a = []
    # for i,v in enumerate(s):
    #     if i == 0:
    #         a.append(s[i])
    #     elif s[i-1] == v:
    #         continue
    #     else:
    #         a.append(s[i])
    # return a
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        print(a)
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(no_continuous("133303"))
