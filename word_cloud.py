from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.font_manager as fm

text = ""
with open("talk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[2:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('내일', '').replace('근데', '').replace('진짜', '').replace('오늘', '').replace('ㅠ', '').replace('ㅜ', '').replace('이모티콘\n', '').replace('사진\n', '').replace('삭제된 메시지 입니다', '')

# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

wc = WordCloud(font_path="C:/Users/82102/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicLight.ttf", background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

mask = np.array(Image.open("cloud.png"))
wc = WordCloud(font_path="C:/Users/82102/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicLight.ttf", background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")