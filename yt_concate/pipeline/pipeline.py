# pipeline.py
# 新增data參數，來存放每一個step要接收的資料

from yt_concate.pipeline.steps.step import StepException

class Pipeline:
    def __init__(self, steps): # 所有的steps會丟進Pipeline所建立的class
        self.steps = steps
    
    def run(self, inputs, utils):
        data = None # 初始化data值，一開始沒有data，值為None
        for step in self.steps:
            # print (step)
            try:
                data = step.process(data, inputs, utils) # inputs = {'channel_id':CHANNEL_ID}
            except StepException as e:
                print('Exception happend:', e)