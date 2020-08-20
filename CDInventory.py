#------------------------------------------#
# Title: CDInventory.py
# Desc: Create a CD inventory. Allow the user to exit the program, load existing
#       data, add data to the table, display the data in memory, delete entries,
#       and save the data in memory to a file. 
# Change Log: (Who, When, What)
# AWaller, 2020-Aug-12, Created file 
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # dictionary of data row
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input

print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Loading existing data
        try:
            # Checking if file object exists and executing code block if so.
            objFile = open(strFileName, 'r')
            lstTbl.clear() # clear the current table in memory for loaded data 
            for row in objFile:
                lstRow = row.strip().split(',')
                dicRow = {'ID':int(lstRow[0]), 'Title':lstRow[1],'Artist':lstRow[2]}
                lstTbl.append(dicRow)
            objFile.close()
            print(lstTbl)
        except IOError:
            # Raising an error if the file does not exist. 
            print('No file exists. Create a file first. \n')    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':intID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        if lstTbl:
            # Checking to make sure there is data to display in the table.
            print('ID, CD Title, Artist')
            for row in lstTbl:
                print(*row.values(), sep = ', ')
        else:
            print('No entries exist to display. Choose \'a\' from menu.\n')
    elif strChoice == 'd': 
        # Delete an entry 
        if lstTbl: 
            # Check that there are entries in the table to delete.
            delValue = int(input('Enter the ID of the entry you wish to delete: '))
            for i in range(len(lstTbl)): 
                if lstTbl[i]['ID'] == delValue:
                    del(lstTbl[i])
                    break
            for row in lstTbl: 
                print(*row.values(), sep = ', ')
        else:
            print('No entries exist to delete. Select a different option. \n')
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow= ''
            for item in row.values(): 
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

