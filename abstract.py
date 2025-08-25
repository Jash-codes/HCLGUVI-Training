from abc import ABC,abstractmethod
class demo(ABC):
    @abstractmethod
    def disp(self):
        pass
    class demo1(demo):
        def disp(self):
            print("abstract method")

    obj = demo1()
    obj.disp()