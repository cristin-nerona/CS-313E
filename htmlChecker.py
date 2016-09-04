#  File: htmlChecker.py
#  Description: Checks whether or not the html code given is valid; takes in txt file named "html.txt" and returns analysis of tags using a stack data type
#  Student's Name: Christina Nerona
#  Student's UT EID: cmn845
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 03/01/16
#  Date Last Modified: 03/04/16


class Stack(): #Creating a stack class
    def __init__(self): # Create stack
        self.myList=[]
        
    def push(self,item): # method to push item onto stack
        self.myList.append(item)

    def pop(self): # method to remove item from stack
        self.myList.pop(-1)

    def __str__(self): # method to tell stack how to print self
        return(str(self.myList))

    def peek(self): # method to look at last item on stack
        return(self.myList[-1])

    def isEmpty(self): # method to check if stack is empty 
        return(self.myList==[])

def filterString(file): # Function to filter through text once and remove tags
    brackets="<>" # defining brackets
    string="" # string for creating individual tag
    output=[] # output list for appending list of tags
    
    for line in file:
        for i in range(len(line)): #iterate through each line and gets tags
            if line[i] in brackets:
                string+=line[i]
                if line[i]==">": #indicates the end of a tag and appends to output
                    output.append(string)
                    string=""
            elif i!=0 and len(string)!=0: #for text in-between < and >
                if string[-1]!=">":
                    string+=line[i]
                else: # end of tag safety
                    output.append(string)
                    string=""
                    
    for i in output: #code for double checking "saved for this file location (not an actual tag)"
        if "<!-- saved from url=" in i:
            output.remove(i)
            
    return(output) #returns list

def main(): #main function

    #Debugging Purposes - sample
    #################################################################################
    #sample="<ol> <li>First item</li> <li>Second item</li> <li>Third item</li> </ol>"
    #################################################################################

    file=open("html.txt")
    stack=Stack() #Create instance of stack
    tagList=(filterString(file)) #Filter string
    exceptions=["<br />","<meta>","<hr>","<br>"] #List exceptions
    validTags=[] #initiate list of valid tags

    for i in tagList: #iterate through list
        
        if not (i in validTags): #enstantiate list of valid tags
            validTags.append(i)
            print("Tag " + i + " not recognized. Adding to list.") #print confirmation of action

        if "meta" in i: #ignore meta -- special case: not uniform
            print("Tag is "+ i + " : pushed: stack is now " + str(stack) + ".") #print confirmation of action
            
        if not ("/" in i) and not (i in exceptions): #Beginning tags added to stack
            stack.push(i)
            print("Tag is "+ i + " : pushed: stack is now " + str(stack) + ".") #print confirmation of action
            
        elif i in exceptions: #Ignore exceptions
            print("Tag is " + i + " : does not need to match:  stack is still:" + str(stack)) #print confirmation of action
            
        else:
            #Clean up end tag for comparison
            i=i.replace("</","")
            i=i.replace(">","")
            i="<"+i+">"
            
            if i == stack.peek(): #Compare end tag to last item in stack and pop stack if match
                stack.pop()
                i=i.replace("<","/")
                i=i.replace(">","")
                print("Tag is " + i + " : matches: stack is now" + str(stack) + ".") #print confirmation of action
                
            else: #If end tag does not match stack's last time
                print("Error: tag is "+ i +" but top of stack is " + str(stack.peek())) #print confirmation of action
                
    print("") #Spacing for clarity

    if stack.isEmpty(): #Stack is empty
        print("Processing complete.  No mismatches found.") #Print statement if valid
        
    else: #Stack is not empty
        print("Processing complete.  Unmatched tags remain on stack:" + str(stack) +".") #Print statement if invalid

    print("") #Spacing for clarity
    print("Valid tags = " +str(validTags)) #Print list of valid tags
    print("With exceptions = " + str(exceptions)) #Print list of exceptions
main()
