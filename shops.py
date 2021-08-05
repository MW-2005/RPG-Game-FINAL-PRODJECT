# buy
#   --> get info about item
# sell
# conversation with vendor (tips/info)

# okay
# good
# great


def clothing():
    def buy_clothing():

        print('FC >> Fur Coat - 100gc')
        print('FBS >> Full Body Suit - 300gc')
        print('SR >> Silk Robes - 20gc')



        Response = input('What do you want to buy?  ')

    def conversation():
        print(
            'It\'s cold out there you might want somthing warm to wear if you haven\'t already, or maybe a little somthing stylish'
        )

    def Exit():
        return

    print('Welcome to the Clothing shop!')
    print('B --> Buy Clothing'
          '\n'
          'C --> Conversation'
          '\n'
          'E --> Exit the Clothing shop'
          '\n')

    response = input('What will you do? ')

    #check to see if response == "B"
    if response.upper() == 'B':
      buy_clothing()

    elif response.upper() =='C':
      conversation()

    elif response.upper() == 'E':
       Exit()


    #finally, make another elif and check to see if the user entered "E". under that, call Exit()
    #i'll be back tomorrow to help you more if you need it!


def pet_shop():
    def buy_pets():
        print('D >> Dog - 150gc')
        print('BP >> Baby Pig - 150gc')
        print('C >> Cat - 150gc')

        Response = input('What do you want to buy?  ')

    print('Welcome to the Pet shop!')
    print('B --> Buy Pets'
          '\n'
          'C --> Conversation'
          '\n'
          'E --> Exit the Pet shop'
          '\n')

    response = input('What will you do? ')


    buy_pets()

def Exit():
    return

def conversation():
    print(
        'You know pets don\'t realy do much but there nice to have tag along on your journey'

            )

    
