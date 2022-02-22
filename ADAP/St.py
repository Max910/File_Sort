import os


def Search_function(File_path):
    with open (File_path, 'r') as rf: #rf = Read File

        # Sword = Search Word
        Sword = input("Enter the word you want to search:\n")
        print ("Searching...")
        for number, line in enumerate( rf ):
            rf.readline
            found = True #
            linec = line #
            LineC = str(line.split()) #
            Lc = linec.lower() #

            

            # print(linec)
            Swordc = Sword #
            Sw= Swordc.lower() #

            if Sw in Lc:

                n = str(number+1)
                print(f"\n\t**found "+ str(LineC)[1:-1] + " at line " + n+ "**\n\n")
                found = False 
                #break
                
        if found == True:
            print("Word"+ ' " '+Sword+' " '+ "Not found")










            # else:
            #     print ("Word not found")
