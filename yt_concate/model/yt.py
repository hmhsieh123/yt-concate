import os

from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None # 是一個字典(key=字幕，value=時間)


    @staticmethod # 用不到self時，可以用staticmethod，其不需要寫self
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]
    
    def get_caption_filepath(self): # 因為會用到 self，故不可以用staticmethod
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')
    
    def get_video_filepath(self): # 因為會用到 self，故不可以用staticmethod
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')
    
    def __str__(self):
        return '<YT(' + self.id + ')>'
    
    def __repr__(self):
        content = ' : '.join(['id=' +str(self.id), # class yt 的str function尚未定義，故會印出object
                              'caption_filepath=' + str(self.caption_filepath),
                              'video_filepath=' + str(self.get_video_filepath)
                              ])
        return '<YT(' + content + ')>'