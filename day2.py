#Today I will be building the Tip calculator but at the same time I will also be learning the foundation that I will need
#to build the Tip calculator 

#==========================================================================================
#First lets learn about various data types:
# In general we have 4 data types: String, Interger, Float and Boolean

print("Hello"[-1])  #this is called subscripting 

#Integer = Whole number 
print(123 + 345) #will give 468 i.e. it adds
print(123_345_678)

#Float: Floating Point Number, when numbers have decimal points
print(3.1415)

#Boolean: True or False; We use this to test whether or not our program is working in a way we want 
##=================================================================================================

#how to identify what type of datatype a piece of data is
print(type(4648)) #type checking

print(type("Hello"))
print(type(3.1415))
print(type(123456))
print(type(True))

#what i did above here is esetnialy printed all the data types

#======================================================================================

#Lets do typecasting: changing the format of data types
print(type(int("123.9")))  #but be careful while type conversion: we might get value error

# to use them: int(), float(), str(), bool()
# challenge: 
print("Number of letters in your name: " + str(len(input("Enter your name "))))

#######: Now let us learn about the mathematical operators: 
print(7-3)
print(3*19)
print(132//12) #gives us 11.0 (implicit type casting ---> gives us float automatically)
print(5//3) # // removes the decimals 
print(3**3) # i.e. 3 to the power of 3

##    use round fuction to round up the digits

#f strings = f""" --> you can add various values {}


#=====================================================================================

#Let's build a tip calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bil? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
total_cost = total_bill + total_bill * (tip/100)

print(f"Each person should pay: ${round(total_cost/total_people, 2)}")

















