def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        length = len(query)
        if query[0] != '?':
            prefix = query.split('?')[0]
            for word in words:
                if len(prefix) == 0 and len(word) == length:
                    cnt += 1
                elif word.startswith(prefix) and len(word) == length:
                    cnt += 1
        else:
            prefix = query.split('?')[-1]
            for word in words:
                if len(prefix) == 0 and len(word) == length:
                    cnt += 1
                elif word.endswith(prefix) and len(word) == length:
                    cnt += 1
        answer.append(cnt)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
