
input_list = []


while True:
  user_input = input("Enter numbers until completed, once completed, enter done ")
  if user_input == "done": print(input_list)
  input_list.append(int(user_input))

print(input_list)