def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(radius):
    a = 3.14*radius*radius
    return a

radius = get_radius("원의 반지름을 입력하세요: ")
area = get_circle_area(radius)
print("반지름이",radius,"인 원의 넓이는",area,"입니다.")

