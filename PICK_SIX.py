import random

def create_ticket():
    user_numbers = []
    for i in range(6):
        user_numbers.append(random.randint(1, 99))
    return user_numbers

winning_ticket = create_ticket()
ticket = create_ticket()

print (winning_ticket)
print(ticket)

def formula(ticket, winning_ticket):

    match = 0
    for i in range(6):
      if ticket[i] == winning_ticket[i]:
        match += 1
    reward = [0, 4, 7, 100, 1000000, 25000000]
    return reward[match]

def game():
  winning_ticket = create_ticket()
  winnings = 0
  costs = 0
  for i in range(100000):
    ticket = create_ticket
    costs += 2
    winnings += formula(ticket, winning_ticket)
    total = winnings-costs

    print(winnings)
    print(costs) 
    print(total)

game()
