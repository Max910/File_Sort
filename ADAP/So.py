import os
import time

def Sort_function(fso):
    c = input("You want to sort file Assending or Desending?\nPress A for Assending\nPress D for Desending")

    # Partion procedure will takes place here(Here List will get slipt into two ) 
    def partition(arr, low, high):

        i = (low-1)		 # index of smaller element
        pivot = arr[high]	 # taking high element as pivot
    
        for j in range(low, high):

            if c == 'A' or c == 'a': #If choice is equal to A the file will sort Assending
                if arr[j] <= pivot:
                    i += 1 #Incrementing the i
                    arr[i], arr[j] = arr[j], arr[i]
            elif c == 'D' or c == 'd':
                if arr[j] >= pivot: #If choice is equal to D the file will sort Desending
                    i += 1
                    # Swapping the elements of the list
                    arr[i], arr[j] = arr[j], arr[i]
        arr[high],arr[i+1] = arr[i+1],arr[high]
        
        return (i+1)


    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:

            pi = partition(arr, low, high)
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)


    print("Running" + fso)
    with open(fso, 'r') as rf:
        content = rf.read()
        Content = content.split("\n")
        while("" in Content):
            Content.remove("")
        print("Total number of lines in selected file is: ",len(Content))
        print("Before sorting:\n")
        print(Content)
        n = len(Content)
        quickSort(Content, 0, n-1)
        print("After Sorting: ")
        print(Content)

        wf = os.path.splitext(fso)[0]
        with open(wf+"_Sorted.txt", 'w') as wf:
            for element in Content:
                wf.write(element + "\n")
        time.sleep(0.900)
        os.startfile(wf.name)
































    # wf =  os.path.splitext(fso)[0]
    # print("Running" + fso)
    # with open(fso, 'r') as rf:
    #     with open(wf+"_Sorted.txt", 'w') as  wf:

    #         Fs = fso
    #         print(Fs)
    #         for line in sorted(rf):
    #             wf.write(line)
    #             # opening the file and printing the contents
    #             print(line, end="")
    #             os.sleep(1.5)
    #         os.startfile(wf)
