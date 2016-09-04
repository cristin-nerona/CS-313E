#  File: sorting.py
#  Description: Tests the efficiency of various sort methods on different types of lists
#  Student's Name: Christina Nerona
#  Student's UT EID: cmn845
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 04/22/16
#  Date Last Modified: 04/22/16

#Import needed libraries
import random
import time
import sys
sys.setrecursionlimit(10000)


#Sorting Methods - Already Provided
def bubbleSort(alist): #Bubble Sort
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist): #Selection Sort
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

def insertionSort(alist): #Insertion Sort
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist): #Shell Sort
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap): #Helper for Shell sort
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist): #Merge Sort
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist): #Quick Sort
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last): #Helper for Quick Sort
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last): #Partition Helper
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def TestSorting(listLength,sort_type,list_type): #Sort testing code
    totalTime=0 #Initiate total time
    
    for t in range(5): #Repeat for 5 trials
        myList = [i for i in range(listLength)] #Make ordered list

        #Find and make list according to type
        if list_type == "random":
            random.shuffle(myList)
        if list_type == "sorted":
            list_type="sorted"
        if list_type == "reverse":
            myList.sort(reverse=True)
        if sort_type == "almost": #For an almost sorted list
            for i in range(0.1*listLength): #Get 10% of list length

                #Get two random integers in list
                randomIndex = random.randint(0,len(myList))
                randomIndex2 = random.randint(0,len(myList))

                #Swap values
                a=myList[randomIndex]
                b=myList[randomIndex2]
                myList[randomIndex]=b
                myList[randomIndex]=a
                
        startTime = time.perf_counter() #Start Counter

        #Get sort type
        if sort_type == "bubble":
            bubbleSort(myList)   
        if sort_type == "selection":
            selectionSort(myList)
        if sort_type == "insertion":
            insertionSort(myList)
        if sort_type == "shell":
            shellSort(myList)
        if sort_type == "merge":
            mergeSort(myList)
        if sort_type == "quick":
            quickSort(myList)
            
        endTime = time.perf_counter() #End Counter
        
        elapsedTime = endTime - startTime #Calculate elapsed time
        totalTime+=elapsedTime #Add to total time
        
    avgTime=totalTime/5 #Get average time
    avgTime=format(round(avgTime,6),"f") #Format average time to 6 decimals
    
    return(avgTime)

def main():

    ####Random####
    print("Input type = Random") #Header

    #Bubble Sort 3 trials: n=10,100,1000
    bubble_10=(TestSorting(10,"bubble","random"))
    bubble_100=(TestSorting(100,"bubble","random"))
    bubble_1000=(TestSorting(1000,"bubble","random"))

    #Selection Sort 3 trials: n=10,100,1000
    selection_10=(TestSorting(10,"selection","random"))
    selection_100=(TestSorting(100,"selection","random"))
    selection_1000=(TestSorting(1000,"selection","random"))

    #Insertion Sort 3 trials: n=10,100,1000
    insertion_10=(TestSorting(10,"insertion","random"))
    insertion_100=(TestSorting(100,"insertion","random"))
    insertion_1000=(TestSorting(1000,"insertion","random"))

    #Shell Sort 3 trials: n=10,100,1000
    shell_10=(TestSorting(10,"shell","random"))
    shell_100=(TestSorting(100,"shell","random"))
    shell_1000=(TestSorting(1000,"shell","random"))

    #Merge Sort 3 trials: n=10,100,1000
    merge_10=(TestSorting(10,"merge","random"))
    merge_100=(TestSorting(100,"merge","random"))
    merge_1000=(TestSorting(1000,"merge","random"))

    #Quick Sort 3 trials: n=10,100,1000
    quick_10=(TestSorting(10,"quick","random"))
    quick_100=(TestSorting(100,"quick","random"))
    quick_1000=(TestSorting(1000,"quick","random"))

    #Print Table
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    "+bubble_10+"   " +bubble_100+"   "+bubble_1000)
    print("   selectionSort    "+selection_10+"   " +selection_100+"   "+selection_1000)
    print("   insertionSort    "+insertion_10+"   " +insertion_100+"   "+insertion_1000)
    print("       shellSort    "+shell_10+"   " +shell_100+"   "+shell_1000)
    print("       mergeSort    "+merge_10+"   " +merge_100+"   "+merge_1000)
    print("       quickSort    "+quick_10+"   " +quick_100+"   "+quick_1000)

    #Spacing
    print()
    print()

    ####Sorted####
    print("Input type = Sorted")

    #Bubble Sort 3 trials: n=10,100,1000
    bubble_10=(TestSorting(10,"bubble","sorted"))
    bubble_100=(TestSorting(100,"bubble","sorted"))
    bubble_1000=(TestSorting(1000,"bubble","sorted"))

    #Selection Sort 3 trials: n=10,100,1000
    selection_10=(TestSorting(10,"selection","sorted"))
    selection_100=(TestSorting(100,"selection","sorted"))
    selection_1000=(TestSorting(1000,"selection","sorted"))

    #Insertion Sort 3 trials: n=10,100,1000
    insertion_10=(TestSorting(10,"insertion","sorted"))
    insertion_100=(TestSorting(100,"insertion","sorted"))
    insertion_1000=(TestSorting(1000,"insertion","sorted"))

    #Shell Sort 3 trials: n=10,100,1000
    shell_10=(TestSorting(10,"shell","sorted"))
    shell_100=(TestSorting(100,"shell","sorted"))
    shell_1000=(TestSorting(1000,"shell","sorted"))

    #Merge Sort 3 trials: n=10,100,1000
    merge_10=(TestSorting(10,"merge","sorted"))
    merge_100=(TestSorting(100,"merge","sorted"))
    merge_1000=(TestSorting(1000,"merge","sorted"))

    #Quick Sort 3 trials: n=10,100,1000
    quick_10=(TestSorting(10,"quick","sorted"))
    quick_100=(TestSorting(100,"quick","sorted"))
    quick_1000=(TestSorting(1000,"quick","sorted"))

    #Print Table
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    "+bubble_10+"   " +bubble_100+"   "+bubble_1000)
    print("   selectionSort    "+selection_10+"   " +selection_100+"   "+selection_1000)
    print("   insertionSort    "+insertion_10+"   " +insertion_100+"   "+insertion_1000)
    print("       shellSort    "+shell_10+"   " +shell_100+"   "+shell_1000)
    print("       mergeSort    "+merge_10+"   " +merge_100+"   "+merge_1000)
    print("       quickSort    "+quick_10+"   " +quick_100+"   "+quick_1000)

    #Spacing
    print()
    print()

    ####Reverse####
    print("Input type = Reverse")

    #Bubble Sort 3 trials: n=10,100,1000
    bubble_10=(TestSorting(10,"bubble","reverse"))
    bubble_100=(TestSorting(100,"bubble","reverse"))
    bubble_1000=(TestSorting(1000,"bubble","reverse"))

    #Selection Sort 3 trials: n=10,100,1000
    selection_10=(TestSorting(10,"selection","reverse"))
    selection_100=(TestSorting(100,"selection","reverse"))
    selection_1000=(TestSorting(1000,"selection","reverse"))

    #Insertion Sort 3 trials: n=10,100,1000
    insertion_10=(TestSorting(10,"insertion","reverse"))
    insertion_100=(TestSorting(100,"insertion","reverse"))
    insertion_1000=(TestSorting(1000,"insertion","reverse"))

    #Shell Sort 3 trials: n=10,100,1000
    shell_10=(TestSorting(10,"shell","reverse"))
    shell_100=(TestSorting(100,"shell","reverse"))
    shell_1000=(TestSorting(1000,"shell","reverse"))

    #Merge Sort 3 trials: n=10,100,1000
    merge_10=(TestSorting(10,"merge","reverse"))
    merge_100=(TestSorting(100,"merge","reverse"))
    merge_1000=(TestSorting(1000,"merge","reverse"))

    #Quick Sort 3 trials: n=10,100,1000
    quick_10=(TestSorting(10,"quick","reverse"))
    quick_100=(TestSorting(100,"quick","reverse"))
    quick_1000=(TestSorting(1000,"quick","reverse"))

    #Print Table
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    "+bubble_10+"   " +bubble_100+"   "+bubble_1000)
    print("   selectionSort    "+selection_10+"   " +selection_100+"   "+selection_1000)
    print("   insertionSort    "+insertion_10+"   " +insertion_100+"   "+insertion_1000)
    print("       shellSort    "+shell_10+"   " +shell_100+"   "+shell_1000)
    print("       mergeSort    "+merge_10+"   " +merge_100+"   "+merge_1000)
    print("       quickSort    "+quick_10+"   " +quick_100+"   "+quick_1000)

    #Spacing
    print()
    print()

    ####Almost####
    print("Input type = Almost sorted")

    #Bubble Sort 3 trials: n=10,100,1000
    bubble_10=(TestSorting(10,"bubble","almost"))
    bubble_100=(TestSorting(100,"bubble","almost"))
    bubble_1000=(TestSorting(1000,"bubble","almost"))

    #Selection Sort 3 trials: n=10,100,1000
    selection_10=(TestSorting(10,"selection","almost"))
    selection_100=(TestSorting(100,"selection","almost"))
    selection_1000=(TestSorting(1000,"selection","almost"))

    #Insertion Sort 3 trials: n=10,100,1000
    insertion_10=(TestSorting(10,"insertion","almost"))
    insertion_100=(TestSorting(100,"insertion","almost"))
    insertion_1000=(TestSorting(1000,"insertion","almost"))

    #Shell Sort 3 trials: n=10,100,1000
    shell_10=(TestSorting(10,"shell","almost"))
    shell_100=(TestSorting(100,"shell","almost"))
    shell_1000=(TestSorting(1000,"shell","almost"))

    #Merge Sort 3 trials: n=10,100,1000
    merge_10=(TestSorting(10,"merge","almost"))
    merge_100=(TestSorting(100,"merge","almost"))
    merge_1000=(TestSorting(1000,"merge","almost"))

    #Quick Sort 3 trials: n=10,100,1000
    quick_10=(TestSorting(10,"quick","almost"))
    quick_100=(TestSorting(100,"quick","almost"))
    quick_1000=(TestSorting(1000,"quick","almost"))

    #Print Table
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    "+bubble_10+"   " +bubble_100+"   "+bubble_1000)
    print("   selectionSort    "+selection_10+"   " +selection_100+"   "+selection_1000)
    print("   insertionSort    "+insertion_10+"   " +insertion_100+"   "+insertion_1000)
    print("       shellSort    "+shell_10+"   " +shell_100+"   "+shell_1000)
    print("       mergeSort    "+merge_10+"   " +merge_100+"   "+merge_1000)
    print("       quickSort    "+quick_10+"   " +quick_100+"   "+quick_1000)
    
main()
