class Productmanager:
    def init(self):
        self.products = {}

    def add_update_product(self, name, price):
        self.products[name] = price

    def remove_products(self, name):
        if name in self.products:
            del self.products[name]

    @staticmethod
    def show_all(self):
        print(f"--현재 메뉴 상태")
        for key in self.products.keys():
            print(f" {key.name}: {key.price}원")

    shop = ProductManager(self)
    shop.add_update_product("커피", 3000)
    shop.add_update_product("케이크", 5000)
    shop.show_all()

    shop.remove_product("커피", 3000)
    shop.show_all()

이 코드는 메뉴관리를 위한 클래스의 정의와 함께 이를 사용하는 주 프로그램부를 포함하고 있다
이 클래스는 상품 추가 수정 삭제 및 전체 메뉴 보기 기능을 포함한다
하지만 제대로 동작하지 않는데 어느 부분들이 고쳐져야 제대로 동작할 수 있는지 알려줘
    
    
