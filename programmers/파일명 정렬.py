import re
def solution(files):
    file = [re.split('([0-9]+)', i) for i in files]
    file = sorted(file, key = lambda x : (x[0].lower(), int(x[1])))
    res = []
    for i in file:
        res.append(''.join(i))
    return res

print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))

# re: 정규 표현식
# [0-9]: 모든 숫자, [a-zA-z]: 모든 문자