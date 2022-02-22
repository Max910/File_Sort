import time
import So as sort

import St as search

import f as file

print("\n\n\n     ********************************\n ",end="") 
time.sleep(0.400)
print( "\tHello Welcome to Text Sort!\n" ,end="")
time.sleep(0.400)
print("     ********************************\n",end="")
time.sleep(0.800)
File = file.Get_file()

while True:

    # Printing the file name, os.path.basename will split the file name11 from the path
    # example: user entered path "C:\Users\ded\Downloads\Test\testf.txt" it will remove "C:\Users\ded\Downloads\Test\" and return"testf.txt"
    C = int(input("1) Press 1 to Enter a Word to be Searched from the file\n"
              "2) Press 2 to Sort the file \n"
              "3) Press 3 if you want to change the path\n"
              "4) Press 4 to Exit the Program\n"))

    
    if C==2:
        sort.Sort_function(File)
    elif C==1:
        search.Search_function(File)
    elif C== 3:
        File = file.Get_file()
    elif C== 4: 
        print("\n\tProcees have been successfully Terminated......\n\n")
        break
    else:
        print("Error, Select a valid option")


        # C:\Users\kchar\Downloads\TestP\Test1.txt