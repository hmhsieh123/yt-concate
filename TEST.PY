# ABMeta 可用來竄改pyton內建的type，來左右後面建立的class，使其成為真正的abstract class
from abc import ABCMeta, abstractclassmethod

class Product(metaclass=ABCMeta):
    # 不是用內建的type來生成class，改成以ABCMeta來生成class
    # 此時pytho就知道這是一個abstract class
    # abstract method
    @abstractclassmethod  # python才知道，下面的是一個abstract method
    def hi(self):
        pass # 這裡不是一定只能寫pass，也可以定義一個function，但後面一定會被覆寫，所以沒差
    @abstractclassmethod
    def hi2(self):
        pass

class Drink(Product):
    def hi(self):
        print("hi")
    def hi2(self):
        print("hi2")
Drink.hi()
# 所以abstract method都被寫上內容了，這樣就不會出錯