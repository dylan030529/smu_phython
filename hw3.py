def get_fixed_price(discount, price):
    money = price / (1 - discount / 100)
    return money

discount = int(input("할인율은? "))
A = int(input("A 상품의 할인된 가격은? "))
B = int(input("B 상품의 할인된 가격은? "))

a = get_fixed_price(discount, A)
b = get_fixed_price(discount, B)

print("A 상품의 정가는 ",a,"원입니다.")
print("B 상품의 정가는 ",b,"원입니다.")
