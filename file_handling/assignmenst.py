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
        
print(removed_vowel)
# print(vowels_only)

joined_vowels = ''.join(removed_vowel)

n = open("vowels.txt", "w")
written = n.write(vowels_only)

# if 

# def rmVowel():
#     sorted_list = splited_letters.sort()
#     print(sorted_list)



# listVersionofg.remove('a')
# print(listVersionofg)



# for word in listVersionofg:
    # print(word)