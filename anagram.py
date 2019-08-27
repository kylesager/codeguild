

def anagram_checker(word1, word2):
    if(sorted(word1) == sorted(word2)):
        print("These words are anagrams.")
    else:
        print("Not anagrams.")


user_input = input("Enter a word... ")
user_input2 = input("Enter another word... ")
word1 = user_input
word2 = user_input2
anagram_checker(word1, word2)
