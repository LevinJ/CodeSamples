# def printme( str):
#     "This prints a passed string inot this function"
#     print(str)
#     return
# 
# 
# printme("vow")
# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")


# Pass by reference vs value

# Function definition is here
def changeme( mylist ):
    "This changes a passed list into this function"
    mylist.append([1,2,3,4]);
    print("Values inside the function: ", mylist)
    return
# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)