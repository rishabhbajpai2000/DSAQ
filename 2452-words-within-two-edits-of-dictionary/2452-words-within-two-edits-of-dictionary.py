class TrieNode:
    def __init__(self, isEOW: bool = False) -> None:
        self.isEOW: bool = isEOW
        self.children: Dict[int, "TrieNode"] = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        nextNode: "TrieNode"
        i: int = 0
        root: "TrieNode" = self.root

        while i < len(word) and ord(word[i]) in root.children:
            root = root.children[ord(word[i])]
            i += 1

        while i < len(word):
            nextNode = TrieNode()
            root.children[ord(word[i])] = nextNode
            root = nextNode
            i += 1

        root.isEOW = True
        
    def takeAll(self, l: List[str]) -> None:
        for i in l:
            self.insert(i)

    def search(self, word: str) -> bool:
        root = self.root

        for i in word:
            if ord(i) not in root.children:
                return False
            root = root.children[ord(i)]
            
        return root.isEOW
        
    def startsWith(self, prefix: str) -> bool:
        root = self.root

        for i in prefix:
            if ord(i) not in root.children:
                return False
            root = root.children[ord(i)]
            
        return True
    
    def is_present(self, word) -> bool:
        def dfs(root, i, c) -> bool:
            if c >= 3:
                return False
            
            while i < len(word) and ord(word[i]) in root.children:
                root = root.children[ord(word[i])]
                i += 1
                
            if i >= len(word):
                return root.isEOW

            return  bool(sum([1 if dfs(j, i + 1, c + 1) else 0 for j in root.children.values()]) > 0)
        
        r = []
        for k, v in self.root.children.items():
            if k == ord(word[0]): 
                r.append(1 if dfs(self.root, 0, 0) else 0)
            else:
                r.append(1 if dfs(v, 1 , 1) else 0)

        return bool(sum(r) > 0)

    
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()
        trie.takeAll(dictionary)
        
        ret = []
        
        for i in queries:
            if trie.is_present(i):
                ret.append(i)
                
        return ret