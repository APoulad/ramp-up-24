#Write a program that takes a string as input,
# reverses it, and counts the number of vowels in it.

def reverse_and_vowels(word: str):
    vowels = sum(1 for letter in word if letter.lower() in 'aeiou')
    return word[::-1], vowels




print(reverse_and_vowels("Hello"))