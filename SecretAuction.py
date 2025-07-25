print("Welcome to Secret Auction , this auction is for a rare pokemon card")
print("Lets,start the bids")

game_over=True
bids={}

while game_over:
    name=input("Enter you name: ")
    price=int(input("Enter your bid: $"))

    bids[name]=price
    Maximum=0

    for keys in bids:
        value=bids[keys]
        if Maximum<value:
            Maximum=value

    winner=max(bids,key=bids.get)
    choice=input("Are you the last person of the auction :").lower()
    print("\n" * 100)
    if choice=="no":
        continue
    else:
        game_over=False
    print(f"The winner is {winner} with the bid of: ${Maximum}")



