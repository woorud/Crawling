def solution(m, musicinfos):
    answer = ''
    m = m.replace('A#', 'H')
    m = m.replace('C#', 'I')
    m = m.replace('D#', 'J')
    m = m.replace('F#', 'K')
    m = m.replace('G#', 'L')
    answer = ''
    dic = {}
    res = None
    for i in musicinfos:
        start, end, song, melody = i.split(',')
        h1, m1 = start.split(':')
        h2, m2 = end.split(':')
        playing = (int(h2)-int(h1))*60 + (int(m2)-int(m1))
        melody = melody.replace('A#', 'H')
        melody = melody.replace('C#', 'I')
        melody = melody.replace('D#', 'J')
        melody = melody.replace('F#', 'K')
        melody = melody.replace('G#', 'L')
        melody = melody*(playing//len(melody)) + melody[0:playing%len(melody)]
        dic[melody] = song

    for melody in dic.keys():
        if m in melody:
            if res == None:
                res = melody
            else:
                if len(res) < len(melody):
                    res = melody
    if res != None:
        return dic[res]
    else:
        return "(None)"

print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00, 03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))