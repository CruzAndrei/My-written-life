#write a method in python to write multiple line of text contents into a text file mylife.txt


#open text file entitled "mylife.txt" as write
def write():
    with open("mylife.txt", "w") as my_story:
        #Create loop function
        while True:
            #Create input for the user
            line = input("Enter a line: ")
            #write in mylife.txt  
            my_story.write(line)
            #ask user to continue or not
            more_line = input("Are there more lines? Enter Y for yes and N for no: ")            
            #create if-else function
            if more_line == "N":
                break
write()
