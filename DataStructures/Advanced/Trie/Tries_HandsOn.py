class TrieNode:
    def __init__(self):
        self.children=[None]*26
        # isLeaf is True if node represent the end of the word
        self.isLeaf=False
class Trie:
    def __init__(self):
        self.root=self.getNode()
    def getNode(self):
        return TrieNode()
    def _charToIndex(self,ch):
        #prevate helper function
        #converts 'a' through 'z' and lower case
        return ord(ch)-ord('a')
    def insert(self,key):
        #if not present , inserts key into trie
        #If the key is prefix of trie node,
        #just marks leaf node
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            #if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index]=self.getNode()
            pCrawl=pCrawl.children[index]


            #mark last node as leaf
            pCrawl.isLeaf=True
    def search(self,key):
        #search key in the trie
        #Returns true if key presents
        #in trie, else false
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._chartoIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl!=None and pCrawl.isLeaf
def main():
    #inpyt keys (use only 'a' through 'z' and lower case)
    keys=["the","a","there","anaswe","any", "by","their"]
    output=["Not present in trie", "Present in tire"]
    #Trie Object
    t=Trie()
    for key in keys:
        t.insert(key)
        
