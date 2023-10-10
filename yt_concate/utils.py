import os
from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import OUTPUT_DIR

class Utils:
    def __init__(self):
        pass

    def create_dirs(self): # 為避免儲存在一個不存在的資料夾中發生錯誤，故需事先建立資料夾
        os.makedirs(DOWNLOADS_DIR, exist_ok=True) # 如果資料夾已存在，是ok的
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt') # video list的檔名定成channel id
    
    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0 # 檔案存在且大小>0
 
    def caption_file_exists(self, yt): # 在download_captions及read_caption2個step均會用到判斷字幕檔是否存在，故將caption_file_exists保留在utils裡
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0 # 檔案存在且大小>0
    
    def video_file_exists(self, yt): 
        filepath = yt.video_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0 # 檔案存在且大小>0
    
    def get_outfile_path(self, channel_id, search_word):
        filename = channel_id + '_' + search_word + '.mp4'
        return os.path.join(OUTPUT_DIR, filename)

