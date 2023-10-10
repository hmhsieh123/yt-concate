from .step import Step
from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR
class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set= set([found.yt for found in data])
        print('videos to download=',len(yt_set))
        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            try:
                print('downloading ', url)
               
                youtube = YouTube(url)
                 # 篩選 progressive 類型的 MP4 影片格式
                progMP4 = youtube.streams.filter(progressive=True, file_extension='mp4')
                # 找出解析度最好的 MP4 影片
                progMP4.order_by('resolution').desc().first().download(output_path=VIDEOS_DIR, filename=yt.id+'.mp4')
            except:
                pass

        return data