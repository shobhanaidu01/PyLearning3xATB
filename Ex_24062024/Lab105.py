letters_list = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'u']
letters_tuple = ('a', 'b', 'd', 'e', 'i', 'j', 'o', 'u')
letters_set = {'a', 'b', 'd', 'e', 'i', 'j', 'o', 'u'}


# Filter the vowels
# a,e,i,o,u


def vowel_giver(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


# result  = filter_vowel('p')
# print(result)

filtered_words = filter(vowel_giver,letters_list)
print(list(filtered_words))

######################
#Define a function to check if a character is a vowel

string = "Hello, how are you today?"

def vowel_char(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return words in vowels

filtered_vowels = filter(vowel_char, string)
print(list(filtered_vowels))