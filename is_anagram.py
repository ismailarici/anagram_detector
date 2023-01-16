
is_anagram = True

def anagrams(word1, word2):

    word1_list = []
    for char in word1:
        word1_list += char
    word2_list = []
    for char in word2:
        word2_list += char
    word1_list.sort()
    word2_list.sort()

    if len(word1_list) == len(word2_list):
        if word1_list == word2_list:
            if word1 != word2:
                print(bool(is_anagram))
            else:
                print(bool(not is_anagram))
        else:
            print(bool(not is_anagram))
    else:
        print(bool(not is_anagram))

word1 = input("Enter the first word ")
word2 = input("Enter the second word ")

anagrams(word1, word2)
