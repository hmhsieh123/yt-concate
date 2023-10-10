import os
import time

from pytube import YouTube
from bs4 import BeautifulSoup
from .step import Step
from .step import StepException
# from yt_concate.pipeline.steps.step import Step
# from yt_concate.pipeline.steps.step import StepException

from youtube_transcript_api import YouTubeTranscriptApi

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        output = ''                                    # 輸出的內容
        num = 0                                      # 每段字幕編號
        for yt in data: # 前面傳來的data是一連串的yt物件
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):         # 若檔案已下載，則跳下一run
                print('found existing caption file')
                # break # 加上break，測試用，後面程式不會執行
                continue
            try:
                x = YouTubeTranscriptApi.get_transcript(yt.id, languages=['en'])  
            except Exception as e:
                print('Error when downloading caption for:', yt.url)
                print("Error:", e)
                continue
            for i, p in enumerate(x):
                num = num + 1                      # 每段字幕編號加 1
                text = p['text']                    # 取出每段文字
                t = int(float(p['start'])*1000)                    # 開始時間 (轉成毫秒)
                d = int(float(p['duration'])*1000)                  # 持續時間 (轉成毫秒)      
                
                h, tm = divmod(t,(60*60*1000))     # 轉換取得小時、剩下的毫秒數
                m, ts = divmod(tm,(60*1000))       # 轉換取得分鐘、剩下的毫秒數
                s, ms = divmod(ts,1000)            # 轉換取得秒數、毫秒

                t2 = t+d  # 根據持續時間，計算結束時間
                try:  # 當i已到最後一個，則i+1會出現indexerror，需另外處理                         
                    if t2 > int(float(x[i+1]['start']*1000)): t2 = int(float(x[i+1]['start']*1000))  # 如果時間算出來比下一段長，採用下一段的時間
                    h2, tm = divmod(t2,(60*60*1000))   # 轉換取得小時、剩下的毫秒數
                    m2, ts = divmod(tm,(60*1000))      # 轉換取得分鐘、剩下的毫秒數
                    s2, ms2 = divmod(ts,1000)          # 轉換取得秒數、毫秒     
                except IndexError:
                    pass
                
                output = output + str(num) + '\n'  # 產生輸出的檔案，\n 表示換行
                output = output + f'{h:02d}:{m:02d}:{s:02d},{ms:03d} --> {h2:02d}:{m2:02d}:{s2:02d},{ms2:03d}' + '\n'          
                output = output + text + '\n'
                output = output + '\n' 
            with open(yt.caption_filepath,'w', encoding='UTF-8') as f1:
                f1.write(output)    # 儲存為 srt
                output = ""
            
        end = time.time()      
        print('took', end - start, 'seconds')  

        return data 
