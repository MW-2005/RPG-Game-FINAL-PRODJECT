from colorama import Fore, Back, Style
from os import system




# buy
#   --> get info about item
# sell
# conversation with vendor (tips/info)

# okay
# good
# great


def clothing(money):
    def buy_clothing(money):

        print('FC >> Fur Coat - 100gc')
        print('FBS >> Full Body Suit - 300gc')
        print('SR >> Silk Robes - 20gc')

        print()
        Response = input('What do you want to buy?  ')
       
        if Response.upper() == 'FC':
            money = money - 100

        if Response.upper() == 'FBS':
            money = money - 300

        if Response.upper() == 'SR':
            money = money - 20
        
        print()
        print()
        print('You have', money, 'gold coins left. Come again soon.')
        return money

    def conversation():
        print(
            'It\'s cold out there you might want somthing warm to wear if you haven\'t already, or maybe a little somthing stylish'
        )

    def Exit():
        return 

    print()
    print()
    print(Fore.MAGENTA + 'Welcome to the Clothing shop!')
    print('B --> Buy Clothing'
          '\n'
          'C --> Conversation'
          '\n'
          'E --> Exit the Clothing shop'
          '\n')

    response = input('What will you do? ')

    #check to see if response == "B"
    if response.upper() == 'B':
      money = buy_clothing(money)
      return money

    elif response.upper() =='C':
      conversation()

    elif response.upper() == 'E':
       Exit()


    #finally, make another elif and check to see if the user entered "E". under that, call Exit()
    #i'll be back tomorrow to help you more if you need it!


def pet_shop(money):
    def buy_pets(money):  
        print('D >> Dog - 150gc')
        print('BP >> Baby Pig - 150gc')
        print('C >> Cat - 150gc')

        print()
        Response = input('What do you want to buy?  ')
        print()
        print()
       
        if Response.upper() == 'D':
            money = money - 150

        if Response.upper() == 'BP':
            money = money - 150

        if Response.upper() == 'C':
            money = money - 150
        
        
        print('You have', money, 'gold coins left. Thank you for shopping with us!!')
        return money




    print()
    print()
    print(Fore.BLUE + 'Welcome to the Pet shop!')
    print('B --> Buy Pets'
          '\n'
          'C --> Conversation'
          '\n'
          'E --> Exit the Pet shop'
          '\n')

    response = input('What will you do? ')
    print()
    print()



    buy_pets(money)

def Exit():
    return

def conversation():
    print(
        'You know pets don\'t realy do much okay they dont do anything at all but there nice to have tag along on your journey'
        )

    
