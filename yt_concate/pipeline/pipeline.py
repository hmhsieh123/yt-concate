from yt_concate.pipeline.steps.step import StepException

class Pipeline:
    def __init__(self, steps): # 所有的steps會丟進Pipeline所建立的class
        self.steps = steps
    
    def run(self, inputs):
        data = None # 初始化data值，一開始沒有data，值為None
        for step in self.steps:
            # print (step)
            try:
                data = step.process(data, inputs) # inputs = {'channel_id':CHANNEL_ID}
                # 將前一個step的回傳值，存到data，再傳到下一個step中
            except StepException as e:
                print('Exception happend:', e)