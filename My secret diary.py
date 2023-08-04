#write a method in python to write multiple line of text contents into a text file mylife.txt


#open text file entitled "mylife.txt" as write
def write():
    with open("mylife.txt", "w") as my_story:
        #Create loop function
        while True:
            #Create input for the user
            line = input("Enter a line: ")
            break
#write in mylife.txt            
#ask user to continue or not
#create if-else function
write()
