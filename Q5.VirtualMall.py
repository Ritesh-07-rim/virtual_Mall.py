class Shop:

    def __init__(self,shop_name,owner,revenue):
        self.shop_name = shop_name
        self.owner = owner
        self.revenue = revenue

    def get_revenue(self):
        return self.__revenue


class ClothingShop(Shop):

    def __init__(self,shop_name,owner,revenue,):
        super().__init__(shop_name,owner,revenue)

    def sell(self):
        print("Shop-name :",self.shop_name)
        print("Owner-name :",self.owner)
        print("Revenue :",self.revenue)
        print(self.shop_name,"is selling cloths")

class FoodShop(Shop):

    def __init__(self,shop_name,owner,revenue,):
        super().__init__(shop_name,owner,revenue)

    def sell(self):
        print("Shop-name :",self.shop_name)
        print("Owner-name :",self.owner)
        print("Revenue :",self.revenue)
        print(self.shop_name,"is selling food")

class ElecctronicShop(Shop):

    def __init__(self,shop_name,owner,revenue,):
        super().__init__(shop_name,owner,revenue)

    def sell(self):
        print("Shop-name :",self.shop_name)
        print("Owner-name :",self.owner)
        print("Revenue :",self.revenue)
        print(self.shop_name,"is selling electronic")

class JewellaryShop(Shop):

    def __init__(self,shop_name,owner,revenue,):
        super().__init__(shop_name,owner,revenue)

    def sell(self):
        print("Shop-name :",self.shop_name)
        print("Owner-name :",self.owner)
        print("Revenue :",self.revenue)
        print(self.shop_name,"is selling jewellary")



class FurnitureShop(Shop):

    def __init__(self,shop_name,owner,revenue,):
        super().__init__(shop_name,owner,revenue)

    def sell(self):
        print("Shop-name :",self.shop_name)
        print("Owner-name :",self.owner)
        print("Revenue :",self.revenue)
        print(self.shop_name,"is selling furnitures")


class ShoeShop(Shop):

    def __init__(self,shop_name,owner,revenue,):
        super().__init__(shop_name,owner,revenue)

    def sell(self):
        print("Shop-name :",self.shop_name)
        print("Owner-name :",self.owner)
        print("Revenue :",self.revenue)
        print(self.shop_name,"is selling shoes")     



shops =[
    ClothingShop("zudio","Tata","1000cr"),
    FoodShop("BBQ-nation","Rahul agarwal","2000cr"),
    ElecctronicShop("Croma","Tata","5000cr"),
    JewellaryShop("Kanika-jewellary","chourasia groups","7000cr"),
    FurnitureShop("Rajhana-furniture","siddu & Sons","500cr"),
    ShoeShop("Red-tap","Irshad Mirza","1000cr")
] 

for shop in shops:
    shop.sell()
    print()