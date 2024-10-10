#My goal for today is to build a treasure island where users decide the outcome of the games but in order to do that
# we will start with foundational knowledge on conditional statements:

#=======================================================================================

height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("can ride")
    age = int(input("What is your age"))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age < 18:
        bill = 7
        print("Print(Please $7")
    elif age <= 45 and age >= 55:
        print("Everything is going to be okay, please have a free ride!")
    else:
        bill = 12
        print("Please pay $12")
    
    want_photo = input("Do you want a photo ticket? Y/N ")
    if want_photo == 'Y':
        bill += 3
    print(f'Your total was ${bill}')

else:
    print("cannot ride")



############ check whether or not a number is odd or even
number =  int(input("Type a number: "))
if number % 2 == 0:
    print("Its even")
else:
    print("its odd")
#===============================================
#goal: create python pizza delivery program:

print("Welcome to the Python Pizza Deliveries")
price = 0

size = input("What size pizza do you want? S, M or L:  ")
if size == 'S':
    price = 15
elif size == 'M':
    price = 20
else:
    price = 25
pepporoni = input("Do you want pepporoni on your pizza? Y or N:  ")
if pepporoni == 'Y' and size == 'S':
    price += 2
elif pepporoni == 'Y' and size != 'S':
    price += 3
extra_cheese =  input("Do you want extra cheese on your pizza? Y or N:  ")
if extra_cheese == 'Y':
    price += 1
print(f'Your total is ${price}')

#========================================================================


# .
#                  __                                        __ 
#                 |--|                                      |--|
#      .._       o' o'                     (())))     _    o' o'
#     //\\\    |  __                      )) _ _))  ,' ; |  __  
#    ((-.-\)  o' |--|  ,;::::;.          (C    )   / /^ o' |--| 
#   _))'='(\-.  o' o' ,:;;;;;::.         )\   -'( / /     o' o'
#  (          \       :' o o `::       ,-)()  /_.')/                 .
#  | | .)(. |\ \      (  (_    )      /  (  `'  /\_)    .:izf:,_  .  |
#  | | _   _| \ \     :| ,==. |:     /  ,   _  / 1  \ .:q568Glip-, \ |
#  \ \/ '-' (__\_\____::\`--'/::    /  /   / \/ /|\  \-38'^"^`8k='  \L,
#   \__\\[][]____(_\_|::,`--',::   /  /   /__/ <(  \  \8) o o 18-'_ ( /
#    :\o*.-.(     '-,':   _    :`.|  L----' _)/ ))-..__)(  J  498:- /]
#    :   [   \     |     |=|   '  |\_____|,/.' //.   -38, 7~ P88;-'/ /
#    :  | \   \    |  |  |_|   |  |    ||  :: (( :   :  ,`""'`-._,' /
#    :  |  \   \   ;  |   |    |  |    \ \_::_)) |  :  ,     ,_    /
#    :( |   /  )) /  /|   |    |  |    |    [    |   \_\      _;--==--._ 
# MJP:  |  /  /  /  / |   |    |  |    |    Y    |CJR (_\____:_        _:
#    :  | /  / _/  /  \   |lf  |  |  CJ|mk  |    | ,--==--.  |_`--==--'_|
#                                                          "   `--==--'  



print("Welcome to Treasure Island\n")
print("You mission is to find the treasure\n")
cross_road = input('You are at a cross road. Where do you want to go? Type "left" or "right" ')
if cross_road == 'right':
    print("You fell into a hole. Game over. Try again!")
else:
    lake = input('You have come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.')
    if lake == "swim":
        print("You were attacked by a trout. Game Over")
    else:
        island = input('You have arrived at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour would you choose? ')
        if island =='red':
            print("You were burnt by fire. Game Over")
        elif island == "blue":
            print("You were eaten by beasts")
        else:
            print("YOU WIN!")





