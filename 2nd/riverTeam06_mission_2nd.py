from multiprocessing.shared_memory import ShareableList
from xml.sax.handler import feature_validation

from numpy import full_like


class Score:
    def __init__(self, mid_term : int, final_term : int):
        self.__mid_term = mid_term
        self.__final_term = final_term
    @ property
    def mid(self) -> int:
        return self.__mid_term
    @ property
    def final(self) -> int:
        return self.__final_term

score=Score(50,75)
print((score.mid+score.final)/2)

class Car():
    """Super Class"""
    def __init__(self, fuel, wheels):
        self.fuel =fuel
        self.wheels=wheels

class Bike(Car):
    """Sub Class"""
    def __init__(self,fuel,wheels,size):
        super().__init__(fuel,wheels)
        self.size=size
bike=Bike("gas","2","small")

print(bike.fuel,bike.wheels,bike.size)

        


