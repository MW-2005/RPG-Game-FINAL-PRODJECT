from colorama import Fore, Back, Style
from os import system
import text
import shops

name = input('Enter your characters name: ')

money = 2000

gender = ''
while gender.lower() != 'boy' and gender.lower() != 'girl':
    gender = input('Are you a boy or girl? ')

print()
print()

print(Fore.RED + 'INTRO CHAPTER')

print()

# print(text.text1) # printing the text from the other file
print(Fore.GREEN + text.intro_text_1)

print()

input(Fore.WHITE +'click enter to continue')

print()


print( Fore.GREEN +
    'You start walking and see a strange man setting on the side of the road you try too keep walking but he calls you over.' + '\n' + '\n' +
    'Being the kind respectful person you are you go over to see what he wants.' 
)

print()

input(Fore.WHITE +'click enter to continue')

print()

print()

print(Fore.WHITE + 'He says:' + '\n')
print(Fore.CYAN + text.intro_text_2 )

print()
print()
print()

print(Fore.GREEN + 'You keep walking and find a village.')

print()

print(Fore.RED + 'END OF INTRO')
input('Click enter to continue to chapter 1')

system('clear')



#############        END OF INTRO        ##############



print(Fore.RED + 'CHAPTER 1')
print()
print()


print (Fore.GREEN + text.Chap1_text_1)


print('1). Clothes shop')
print('2). Pet shop')


print()
#you can just make this input a print
print('Do you want to go to the clothing shop? ')
answer = input ('>> (yes, no): ')

if answer == 'yes':
    money = shops.clothing(money)


print('Do you want to go to the pet shop? ')
answer = input ('>> (yes, no): ')

if answer == 'yes':
    money = shops.pet_shop(money)

# Instead of asking if they want to go to shop 1 or 2
# Ask first --> If they want to visit the clothing
#   if yes, then go to clothing shop
#   else, do nothing
# Ask second --> if they want to visit the pet shop
#   if yes, then go to pet shop
#   else, do nothing


print()
print()



#also how woold i subtract the price from the original amount of money


#do i have to make the price of whwt they are buying into a variable

#no, you don't have to, but the amount you subtract depends on their selection

#for example, if they select the dog (response == "D"), you subtract 150 (money = money-150)
#i'll be back in a moment!!

            

print(Style.RESET_ALL) # Reset Style after finished.