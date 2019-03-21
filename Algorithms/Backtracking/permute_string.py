"""
Python : Backtracking Algorithms
         String Permutation

Source: Geeksforgeeks
"""


def permute_string(string, word_left, word_right):

    if word_left == word_right:
        print(''.join(string))

    else:
        for i in range(word_left, word_right+1):
            string[word_left], string[i] = string[i], string[word_left]
            permute_string(string, word_left+1, word_right)
            string[word_left], string[i] = string[i], string[word_left]


if __name__ == "__main__":
    word = list("ABCD")
    permute_string(word, 0, len(word)-1)