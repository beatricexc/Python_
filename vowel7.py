vowels =set('aeiou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)

# 1.Turning the list into a set with the set method
# 2.Ths allows us to check for duplicates using the intersection method on the word turned into a set
# 3.Finishing with a for loop that iterates over each vowel found by the intersection of the vowel set with the found set
