import os 
f = open("file_handling\carBlog.txt", "r")

read_f = f.read()

splited_word = ""
for word in read_f:
    splited_word = splited_word + word + " "

# print(splited_word)

splited_letters = splited_word.split(" ")

# print(splited_letters)

removed_vowel = []
vowels_only=[]
vowels = ["a","e","i","o","u","","â"]



for letter in splited_letters:
    if letter not in vowels:
        removed_vowel.append(letter)
    else:
        vowels_only.append(letter)
        
# print(removed_vowel)
# print(vowels_only)

joined_consonants = ''.join(removed_vowel)

c = open("consonants.txt", "w")
consonant = c.write(joined_consonants)


joined_vowels = ''.join(vowels_only)

v = open("Vowels.txt", "w")
vowel = v.write(joined_vowels)