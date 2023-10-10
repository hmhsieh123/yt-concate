import sys
import urllib.request
import json
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils): # inputs 是一個字典，從main傳進來，內容為channel id、keyword...
        channel_id = inputs['channel_id']

        if utils.video_list_file_exists(channel_id): # 若檔案存在，則讀取它
            print('Found existing video list file for channel id:', channel_id)
            return self.read_file(utils.get_video_list_filepath(channel_id))


        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break

        print(video_links)  
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links
    
    def write_to_file(self, video_links, filepath): # 將影片清單寫到檔案，至於寫到哪個檔案，可以由utils中取得path
        with open(filepath, 'w', encoding='UTF-8') as f:
            for url in video_links:
                f.write(url + '\n')


    def read_file(self, filepath): # 若影片清單已存在，則讀取此檔案
        video_links = []
        with open(filepath, 'r') as f:
            for url in f:
                video_links.append(url.strip()) # 去掉url前後的換行符號及空格
        return video_links
                


        