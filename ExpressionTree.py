#  File: ExpressionTree
#  Description: Makes expression tree, evaluates, converts infix to pre and post
#  Student's Name: Christina Nerona
#  Student's UT EID: cmn845
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 04/22/16
#  Date Last Modified: 04/29/16

import operator #import operator library
import math #import math library

class Stack(): #Creating a stack class
    def __init__(self): # Create stack
        self.myList=[]

    def push(self,item): # method to push item onto stack
        self.myList.append(item)

    def pop(self): # method to remove item from stack
        return(self.myList.pop(-1))

    def __str__(self): # method to tell stack how to print self
        return(str(self.myList))

    def peek(self): # method to look at last item on stack
        return(self.myList[-1])

    def isEmpty(self): # method to check if stack is empty 
        return(self.myList==[])

class BinaryTree: #Class Binary Tree

    def __init__ (self,initVal): #Initiate Tree
        self.data = initVal
        self.left = None
        self.right = None
        
    def insertLeft(self,newNode): #Insert Left
        if self.left == None:
         self.left = BinaryTree(newNode)
        else:
         t = BinaryTree(newNode)
         t.left = self.left
         self.left = t
    
    def insertRight(self,newNode): #Insert Right
        if self.right == None:
         self.right = BinaryTree(newNode)
        else:
         t = BinaryTree(newNode)
         t.right = self.right
         self.right = t

    def __str__(self): #How to print
        return("[Data:] " + str(self.data) + "     [Left:] " +str(self.left) + "      [Right:] " +str(self.right))
    
    def setRootVal(self,value): #Get root val
        self.data = value

    def getLeftChild(self): #Get left
        return self.left

    def getRightChild(self): #Get right
        return self.right

    def getRootVal(self):
        return self.data

    def createTree (self, expr): #Create Tree
        self.tree = helper_makeTree(self,expr)
        return(self.tree)
    
    def evaluate (self): #Evaluate tree
        return(helper_evaluate(self.tree))

    def preOrder (self, input_string): #Reorder in prefix
        reverse_string=input_string[::-1]
        rev_tokes = reverse_string.split(" ")
        helper_stack=Stack()
        string=""
        for i in rev_tokes: #Reverse tokens
            if i == ")":
                helper_stack.push(i)
            if i.isdigit() or "." in i: #Check if operand
                string+=i+" "
            if i == "(": #Deal with parentheses
                while (helper_stack.peek()!=")"): #Pop until matching parentheses is found
                    string+=helper_stack.pop()+" "
                helper_stack.pop()
            elif i in ["*","/","+","-"] and (helper_stack.isEmpty() or helper_stack.peek()==")"): #Add first operator to stack
                helper_stack.push(i)
            elif i in ["*","/"] and (helper_stack.peek() == "*" or helper_stack.peek() == "/"): #Precedence of operators
                helper_stack.push(i)
            elif i in ["-","+"] and helper_stack.peek() in ["-","+"]: #Precedence of operators
                helper_stack.push(i)
            elif i in ["+","-"] and helper_stack.peek() in ["*","/"]: #Precedence of operators
                while helper_stack.peek() in ["*","/"]:
                    string+=helper_stack.pop()+" "
                helper_stack.push(i) #Pop until lower one or empty
            elif i in ["*","/"] and helper_stack.peek() in ["-","+"]: #Precedence of operators
                helper_stack.push(i)
            
        while not(helper_stack.isEmpty()): #Pop remaining operators
            string+=helper_stack.pop()+" "
        string = string[::-1] #reverse string
        return(string)

    def postOrder (self, tokens):
        string=""
        helper_stack=Stack()
        for i in tokens:
            if i.isdigit() or "." in i: #Check if token is number
                string+=i+" "
            if i in ["+","-","*","/"] and (helper_stack.peek() == "(" or helper_stack.isEmpty()): #Deal with operators, etc
                helper_stack.push(i)
            if i == "(":
                helper_stack.push(i) #parentheses
            if i == ")":
                while helper_stack.peek()!="(": #parentheses
                    string+=helper_stack.pop()+" "
            if (i == "*" or i == "/") and (helper_stack.peek() == "+" or helper_stack.peek() == "-"): #Precedence of operators
                while (i == "*" or i == "/") and (helper_stack.peek() == "+" or helper_stack.peek() == "-"):
                    string+=helper_stack.pop()+" "
                helper_stack.push(i)
        while not(helper_stack.isEmpty()): #pop remaining operators
            string+=helper_stack.pop()+" "
        string=string.replace("(","") #Replace parentheses
        string=string.replace(")","")
        return(string)

def helper_evaluate(tree): #Helper for evaluation
    if tree.getLeftChild(): #check left
        if tree.getRightChild(): #check if right child
            #Perform evaluation using operators
            return ({ '-':operator.__sub__, '/':operator.__truediv__, '*':\
                      operator.__mul__,'+':operator.__add__,}\
                    [tree.getRootVal()](helper_evaluate(tree.getLeftChild()),\
                                        helper_evaluate(tree.getRightChild()))) #Perform recursive evaluation using left and right branches
        #Perform on the root of the tree
    else:
        root=tree.getRootVal() #else return root
        return (root)

def helper_makeTree(node,input_string): #Tree maker helper
    stack=Stack()
    current = node
    tokens = input_string.split(" ") #split tokens
    for i in tokens:
        if i == "(": #Dealing with left parenthesis
            current.insertLeft(None)
            stack.push(current)
            current = current.left
        if i.isdigit() or "." in i: #Check if number
            current.setRootVal(float(i))
            current = stack.pop()
        if i == ")": #Dealing with right parenthesis
            if not(stack.isEmpty()):
                current = stack.pop()
        if i in ["*","+","-","/"]: #Check operators
            current.setRootVal(i)
            current.insertRight(None)
            stack.push(current)
            current = current.right #Adjust current position
    return(current)
    
def main(): #Main program
    file=open("treedata.txt","r") #open file
    for line in file:
        input_string = line.strip()
        tokens = input_string.split(" ") #Get tokens

        #Formatting and printing
        print("Infix expression:  " + str(input_string))
        
        #Instance of tree
        node = BinaryTree(None)
        node.createTree(input_string)

        #Evaluate, and convert to pre and post order
        print("   Value:   "+str(node.evaluate()))
        print("   Prefix expression:   " +str(node.preOrder(input_string)))
        print("   Postfix expression:   " +str(node.postOrder(tokens)))
        print()
        
    file.close() #close file

main()
