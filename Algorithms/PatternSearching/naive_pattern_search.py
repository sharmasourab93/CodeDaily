"""
Python: Pattern Searching Algorithms
        Naive Pattern Searching Algorithm

Time Complexity:
    Worst Case Complexity O(n * m)
    Best Case Complexity O(n)
         where n - Size of the pattern
               m - Size of the text
               
Number of comparisons in worst case O(m*(n-m+1))
"""


# Naive Pattern Searching
def search(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    
    for iter_i in range(pattern_len - text_len + 1):
        
        iter_j = 0
        
        while iter_j < pattern_len:
            
            if text[iter_i + iter_j] != pattern[iter_j]:
                break
            iter_j += 1
            
        if iter_j == pattern_len:
            print("Pattern found at index ", iter_i)
            
            
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
