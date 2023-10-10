from .step import Step

from moviepy.editor import VideoFileClip, concatenate_videoclips

class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data: 
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video) # 將剪集下來的影片先放到[]，方便之後合併
            if len(clips) >= inputs['limit']: # 若剪集片段數量超過limit，則停止
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_outfile_path(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end) # 回傳tuple(tuple,tuple)
    
    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000 # 會自動組成tuple


    