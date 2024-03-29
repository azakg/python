from art import logo

print(logo)
print("Welcome to Secret Auction")

bidders_list = {}

bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bidding_amount = int(input("What is your bid?: "))
    bidders_list[name] = bidding_amount
    should_continue = input("Are there any other bidders? Type 'yes or no'")
    if should_continue == 'no':
        bidding_finished = True

winner_name = ''
winner_amount = 0
for i in bidders_list:
    if bidders_list[i] > winner_amount:
        winner_amount = bidders_list[i]
        winner_name = i

print(f"The winner's name is {winner_name} and amount is {winner_amount}")
