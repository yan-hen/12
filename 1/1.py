class Z :
    def _init_(self,product_name,product_price,purchaser):
            self.__product_name= product_name
            self.__product_price= product_price
            self.__purchaser= purchaser

#商品名稱的建構值
    def get_product_name(self):
        return self.__product_name

#商品價格的建構值
    def get_product_price(self) :
        return self.__product_price

#購買商品的人
    def get_purchaser(self):
        return self.__purchaser


    d1=Z("book")
    d2=Z("456")
    d3=Z("lyh")

    print("商品名稱:",d1.get_product_name())
    print("商品價格:",d2.get_product_price())
    print("購買人:",d3.get_purchaser())
