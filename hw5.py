def read_single_digit(n):
    if n == 0:
        return "영"
    elif n == 1:
        return "일"
    elif n == 2:
        return "이"
    elif n == 3:
        return "삼"
    elif n == 4:
        return "사"
    elif n == 5:
        return "오"
    elif n == 6:
        return "육"
    elif n == 7:
        return "칠"
    elif n == 8:
        return "팔"
    elif n == 9:
        return "구"

def read_number(n):
    s = str(n)
    a = read_single_digit(int(s[0]))
    b = read_single_digit(int(s[1]))
    c = read_single_digit(int(s[2]))
    return a + b + c

num = int(input("세 자리 정수 입력: "))
print(read_number(num))

