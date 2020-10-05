# 데이터 쓰기
f = open("test.txt", "w", encoding="utf-8")
f.write("Hello, World!\n")

for i in [1, 2, 3, 4, 5]:
    f.write("{}번째 줄입니다.\n".format(i))
f.close()

'''
# 데이터 읽기
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
'''

text = ""
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line
print(text)
