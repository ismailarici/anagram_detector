import re
read_text = open("sample_text.txt").read()
only_alphabetical = re.sub(r'[^a-zA-Z\s]', '', read_text)
each_word = only_alphabetical.split()

as_set = set(each_word)

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
                print(f'{word1} and {word2} are anagrams')
            else:
                return
        else:
            return
    else:
        return
for item1 in as_set:
    for item2 in as_set:
        anagrams(item1, item2)

