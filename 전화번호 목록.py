def solution(phone_book):
    phone_book.sort()

    for i in range(1, len(phone_book)) :
        if phone_book[i-1] in phone_book[i]:
            return False
        else:
            return True

print(solution(["123", "456", "789"]))
print(solution(['12','123','1235','567','88']))
print(solution(['119', '97674223', '1195524421']))