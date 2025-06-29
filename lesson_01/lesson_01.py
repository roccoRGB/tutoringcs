#create a list with 4 random names
name00 = "charles"
name01 = "rocco"
name02 = "drake" 
name03 = "josh"
lest00 = [name00, name01, name02, name03]

#turn your 5 lines of code into 1 line
lest01 = ["name00", "name01", "name02", "name03"]

#print your first list of names
print(lest00)

#remove the last name in lest01
lest01.pop()
print(lest01)

#replace the first name in your list with "Donald Trump"
lest01[0] = "Donald Trump"
print(lest01)

#function that prints variables
def printVar(x):
    print(x)

printVar(name00)