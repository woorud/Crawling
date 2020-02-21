def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
    return answer
print(solution(['119', '97674223', '1195524421']))