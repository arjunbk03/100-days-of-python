#Learning about printing, commenting and others! 
#We will be making band name generator
print("Hello World!\nHello World!") #using the print function
#concatanate strings
print("Hello " + "Angela") 
#It is extremely important to be careful about spaces in python (check for indentation errors)

#Ask the use to enter some data - use input function
input("What is your name?")

#combining print and input function
print("Hello " + input("What is your name? ") + "!")

#========================================================
#calculate the characters in the name
name =  input("What is your name? ")
print(len(name))

#Another way to calculate the characters using variables
username = input("What is your name? ")
length = len(username)
print(length)

#==========================================================
#Creating the band name generator
print("Welcome to the Band Name Generator.")
name = input("Which city did you grow up in?\n")
city = input("What is your pet's name?\n")
print("Your band name could be " + name + " " + city)








