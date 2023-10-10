from .step import Step

class ReadCaption(Step):
    def process(self, data, inputs,utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}          
            with open(yt.caption_filepath, 'r', encoding = 'UTF-8') as f:       
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            yt.captions = captions
        # print(data)
        return data # 進來data，還是回傳data，只是身上的屬性有被改變 (yt.captions = captions)

