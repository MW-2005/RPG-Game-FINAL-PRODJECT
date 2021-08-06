from colorama import Fore, Back, Style
from os import system
import text
import shops

name = input('Enter your characters name: ')

money = 900

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

if answer.lower() == 'yes':
    money = shops.clothing(money)


print('Do you want to go to the pet shop? ')
answer = input ('>> (yes, no): ')

if answer.lower() == 'yes':
    money = shops.pet_shop(money)



print()
print()



print(Fore.GREEN + text.Chap1_text_2)

print()

print(Fore.RED + 'END OF CHAPTER 1')
input('Click enter to continue to chapter 2')            
system('clear')



################### CHAPTER 2 #######################



print(Fore.RED + 'CHAPTER 2')
print()
print()


print (Fore.GREEN + text.Chap2_text_1)
print()

input(Fore.WHITE +'click enter to continue')
print()


print (Fore.GREEN + text.Chap2_text_2)
print()


input(Fore.WHITE +'click enter to continue')
print()

print(Fore.Green + text.Chap2_text_3
)

print()

print(text.Chap2_text_4)
print()
print()


print(Fore.YELLOW + 'Look I\'m not sure where you\'re from but in this village to enter the bet you need to have at least 1,000 gold coins to gamble. So just leave. ')

print(Fore.BLUE + 'I don\'t know about gold coins but I do have this.')

print(Fore.GREEN + 'You take out the platinum coin and show it to him.')

print(Fore.YELLOW + 'Where did you get this coin?')

print(Fore.BLUE + 'My father gave it to me.')

print()
print()
print()

print(Fore.RED + 'END OF CHAPTER 2')
input('Click enter to continue to chapter 3')            
system('clear')

#############END OF CHAPTER 2#############

print(Fore.RED + 'CHAPTER 3')
print()
print()



('Do you know what this is?')

('I always thought it was just a normal coin')

('You need to come with me')

('Seeing as you have nothing better to do you follow him')

('Where are we going?')

('You\'ll see')

print(Style.RESET_ALL) # Reset Style after finished.