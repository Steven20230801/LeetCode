class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    # 新增一個畫出 Trie 結構的 function
    def draw(self, node=None, prefix=""):
        if node is None:
            node = self.root
        for char, child in node.children.items():
            # 如果 child.word 為 True，則在節點後標記 (word)
            marker = " (word)" if child.word else ""
            print(prefix + "|-- " + char + marker)
            # 遞迴呼叫以畫出子節點，prefix 增加縮排以呈現層次結構
            self.draw(child, prefix + "    ")


# Your Trie object will be instantiated and called as such:
word = "cat"
obj = Trie()
obj.insert("cat")
obj.insert("can")
obj.insert("cow")
obj.draw()
param_2 = obj.search(word)
param_3 = obj.startsWith("ca")
