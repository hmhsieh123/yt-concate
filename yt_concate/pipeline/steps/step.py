# 寫抽象類別，做為介面，之後的子孫繼承它，都是用這個介面來操作
# 抽象類別，裡面至少要有一個abstract method
from abc import ABC
from abc import abstractclassmethod
a = 100
class Step(ABC):
    def __init__(self): # 因子孫不用改寫__init__，故__init__不用變成abstractmethod
        pass

    @abstractclassmethod
    def process(self, data,  inputs): # 子孫要改寫 process
        #  inputs 是一個字典，從main傳進來，內容為channel id、keyword...
        pass

class StepException(Exception): 
    # 此例外用於，當任何一個step觸發exception，即停止，例如：當下載youtube影片時下載不到，就不用再繼續往下執行
    pass