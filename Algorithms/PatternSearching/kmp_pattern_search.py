"""
Python: Pattern Searching Algorithm
        KMP Pattern Searching Algorithm
"""


# Preprocessing Algorithm
def compute_lps(pattern, pattern_len, lps):
    # length of the previous
    # longest prefix & suffix
    length = 0
    lps[0], iter_i = 0, 1
    
    while iter_i < pattern_len:
        if pattern[iter_i] == pattern[length]:
            length += 1
            lps[iter_i] = length
            iter_i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[iter_i] = 0
                iter_i += 1
                
                
def kmp_search(pattern, text):
    
    pat_len, text_len = len(pattern),  len(text)
    lps, i, j = [0] * pat_len, 0, 0
    compute_lps(pattern, pat_len, lps)
    
    while i < text_len:
        
        if pattern[j] == text[i]:
            i, j = i + 1, j + 1
        if j == pat_len:
            print("Found pattern at index", str(i-j))
            j = lps[j-1]
        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmp_search(pat, txt)
