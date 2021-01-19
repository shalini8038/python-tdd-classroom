def reverse_list(input_list):
    input_list.reverse()
    return input_list

def reverse_string(input_str):
    return input_str[::-1]

def is_english_vowel(character):
    all_vowels = 'aeiouAEIOU'
    return character in (all_vowels)

def find_longest_word(sentence):
    longest = max(sentence.split(), key=len)
    return longest

def get_word_lengths(text):
    li = list(map(len, text.split()))
    return li
