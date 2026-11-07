import random
import time


def spin_row():
    symbols=["🍒","🍋", "🍓", "🍉", "⭐"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):

    print("**********************")
    print("   |   ".join(row))
    print("**********************")

def payout(row,bet):

    if row[0]==row[1]==row[2]:

      if row[0]=="🍒":
          return bet*10

      if row[0]=="🍋":
          return bet*20

      if row[0]=="🍓":
          return bet*30

      if row[0]=="🍉":
          return bet*50

      if row[0]=="⭐":
          return bet*100
    return 0

balance=100


print("**************************")
print()
print("Python Casino")
print("Symbol: 🍒 🍋 🍓 🍉 ⭐")
print()
print("**************************")

while balance>0:
 print(f"Current balance is ${balance:.2f}")
 print()
 bet=input("Enter your bet amount: ")

 if  bet.isalpha():
     print("Invalid amount")
     continue

 bet=float(bet)
 if bet>balance:
    print("Insufficient Balance")
    continue

 if bet<=0:
    print("The bet amount must be more than $0")
    continue


 balance-=bet
 print("Spinning.....")
 time.sleep(1)
 row= spin_row()
 print_row(row)

 pay = payout(row, bet)

 if pay > 0:
    print(f"You won ${pay:.2f}")
 else:
    print("You lost")

 balance += pay

 play_again=input("Do you want to play again?(Y/N): ").upper()

 if play_again=="Y":
     continue
 else:
     print()
     print("Thank you for playing")
     break

print()
print(f"Your balance is {balance}")

input("Press Enter to close the game...")
