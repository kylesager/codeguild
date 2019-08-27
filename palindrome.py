def reverse(word_reversed):
  if(len(word_reversed) == 0):
    return word_reversed
  else:
    return reverse(word_reversed[1 : ]) + word_reversed[0]


word = input('Enter a word: ')
word_reversed = reverse(word)
print("Reversed:  ", word_reversed)

if(word == word_reversed):
  print("word is a palindrome")
else:
  print("no word is not a palindrome")
