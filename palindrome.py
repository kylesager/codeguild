def reverse(word_reversed):
  if(len(word_reversed) == 0):
    return word_reversed
  else:
    return reverse(word_reversed[1 : ]) + word_reversed[0]

## after looking back i see how confusing my naming was 
#word is the users input
#word reversed is the user's input spelled backwards
#reverse is the function that takes the length of the words (user's word, and reversed version) and checks to see if they are equal


word = input('Enter a word: ')
word_reversed = reverse(word)
print("Reversed:  ", word_reversed)

if(word == word_reversed):
  print("word is a palindrome")
else:
  print("no word is not a palindrome")
