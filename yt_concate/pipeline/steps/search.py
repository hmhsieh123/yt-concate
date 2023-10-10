from .step import Step
from yt_concate.model.found import Found

class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions # captions是一個字典，key是字幕，value是時間
            if not captions: # 若 yt.captions = None (預設值)，表示字幕沒有下載不存在，則pass
                continue
            # 這裡不使用 for caption, time in captions.items()，同時將key及value取出
            # 原因是，可能有99%的資料找不到search_word，但卻每次都要取出caption及time，有點多餘
            for caption in captions: # 在key中搜尋(即在字幕中搜尋)
                if search_word in caption:
                    time = captions[caption]
                    # found.append((yt, caption, time))  append只能append 1個，故需用tuple包起來
                    # 但同樣的，這也有解讀是的困難，你要記得tuple的第1、2、3個值代表什麼
                    # 故可以將其改寫為字典，可增加易讀性
                    # found.append({
                    #               'yt' : yt
                    #               'caption' : caption
                    #               'time' : time})
                    # 但最好的方式，還是寫成一個model
                    f = Found(yt, caption, time)
                    found.append(f)
        print(repr(found))
        return found