def is_anagram(w_1, w_2):
    letters_1 = dict()
    letters_2 = dict()

    if len(w_1) != len(w_2): 
        return "NO"
    else: 
        for letter in w_1:
            letters_1[letter] = w_1.count(letter)
            letters_2[letter] = w_2.count(letter)
        for key in letters_1:
            if letters_1.items() != letters_2.items():
                return "NO"
    
    return "YES"
    

word_1 = input()
word_2 = input()
print(is_anagram(word_1, word_2))