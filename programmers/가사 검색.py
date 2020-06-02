from collections import defaultdict
class Node:
    def __init__(self, char, length = None, data = None):
        self.char = char
        self.data = None
        self.children = {}
        self.length = defaultdict(int)

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head
        node.length[len(string)] += 1
        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)
            node.children[char].length[len(string)] += 1
            node = node.children[char]
        node.data = string

    def start_with(self, prefix, length):
        node = self.head
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 0
        return node.length[length]

def solution(words, queries):
    res = []
    front = Trie()
    back = Trie()
    for word in words:
        front.insert(word)
        back.insert(word[::-1])

    for query in queries:
        if query == '?'*len(query):
            res.append(front.head.length[len(query)])
        elif query[0] == '?':
            prefix = query[::-1].split('?')[0]
            res.append(back.start_with(prefix, len(query)))
        else:
            prefix = query.split('?')[0]
            res.append(front.start_with(prefix, len(query)))

    return res


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],	["fro??", "????o", "fr???", "fro???", "pro?"]))
