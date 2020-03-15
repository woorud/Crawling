def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    answer = True
    for i, phone1 in enumerate(phone_book):
        hash_map = {}
        for phone2 in phone_book[i+1:]:
            hash_map[phone2[:len(phone1)]] = phone2
        if phone1 in hash_map:
            answer = False
            break
    return answer



print(solution(["123", "456", "789"]))
print(solution(['12','123','1235','567','88']))
print(solution(['119', '97674223', '1195524421']))
print(solution(['119', '11119']))