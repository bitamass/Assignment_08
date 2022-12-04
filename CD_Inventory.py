#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Bmassoudi, 2022-Dec-01, modified to Object Oriented Programming
#------------------------------------------#
# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = [] #list of objects

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        txtList: return a string with 3 properties infomation.
    """
    # TODONE Add Code to the CD class
    def __init__(self, cd_id, cd_title, cd_artist):
        #  attributes  #
            
            self. __id= cd_id
            self. __title= cd_title
            self. __artist= cd_artist
        #  Properties  #
    @property
    def cd_id(self):
            return self.__id
    @property
    def cd_title(self):
            return self.__title
    @property
    def cd_artist(self):
            return self.__artist
        
    @cd_id.setter
    def cd_id(self, value):
                self.__cd_id = value
    @cd_title.setter
    def cd_title(self, value):
                self.__cd_title = value
    @cd_artist.setter
    def cd_artist(self, value):
                self.__cd_artist = value            
                
        #  Methods  #
            
    def __str__(self):
            return self.txtList() 
        
    def txtList(self):
        return '{},{},{}'.format(self.cd_id, self.cd_title, self.cd_artist)
        

       

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODONE Add code to process data from a file
    # TODONE Add code to process data to a file
  
    @staticmethod
    def read_file(strFileName, lstOfCDObjects):
        """Function to read stored binary data
            file_name (string): name of file used to read the data from
            rowData: [0]=> CD, [1]=>TITLE, [2]=>Artist
            cd_info: object of CD info
        """
    try:
        lstOfCDObjects.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            rowData = row.strip().split(',')
            cd_info = CD(int(rowData[0]), rowData[1], rowData[2])
            lstOfCDObjects.append(cd_info)
        objFile.close()
    except FileNotFoundError as e:
            print('Text file does not exist!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        
            
    @staticmethod
    def write_file(strFileName, lstOfCDObjects):
        """Save CD data
        Args:
            file_name (string): name of file used to save the data
            table: list of CD object(lstOfCDObjects)
            objList: A string from txtList
        """
        while True:
            try:
                strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
                if not strYesNo:
                    raise Exception
                break
            except Exception:
                print('Didn\'t enter anything! Type again!!')
        # 3.6.2 Process choice 'y'
        # save data to txt file
        if strYesNo == 'y':
            objFile = open(strFileName, 'w')
            for item in lstOfCDObjects:
                objList = item.txtList()
                objFile.write(objList + '\n')
            objFile.close()
            print('\nCD DATA SAVED\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')          
    

# -- PRESENTATION (Input/Output) -- #
class IO:
    """
    User interaction
    properties:
    methods:
        print_menu():Display the menu choice to the user
        menu_choice: input user for menu selection
        show_inventory(table): current inventory table
        user-input(table): input for new ID, CD Title, and Artist        
    """
    # TODONDE add docstring
    # TODONE add code to show menu to user
    # TODONE add code to captures user's choice
    # TODONE add code to display the current data on screen
    # TODONE add code to get CD data from user
    @staticmethod
    def print_menu():    
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')    
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        #Error Handling for not entering anything in [l, a, i, s, x]
        while True:
            try:
                choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
                if (choice == 'a') or (choice == 'l') or(choice == 'i') or(choice == 's') or(choice == 'x'):
                    break
                else: raise Exception
            except Exception:
                print('This is an invalid choice! Please try again!!')
        print()  # Add extra space for layout
        return choice
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table: list of object
            row: string for each line
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        
        # Use a for loop to print this "CD objects" list
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def CDInput():
        """User Enter CD data
        Returns: intID, strTitle, stArtist
        """
        while True:
            strID = input('Enter ID: ').strip()
            #Error Handling if user enter non-numeric value
            try:
                intID = int(strID)
                break
            except ValueError:
                print('This is not an integer! Enter again!')
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, stArtist

# -- Main Body of Script -- #
# TO DONE Add Code to the main body
# -- PRESENTATION (Input/Output) -- #

# Load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstOfCDObjects )

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        break

    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press any key to continue to the menu.')

    # let user add data to the inventory
    elif strChoice == 'a':
        forID, forTitle, forArtist = IO.CDInput()
        objCD = CD(forID, forTitle, forArtist)
        lstOfCDObjects.append(objCD)
        IO.show_inventory(lstOfCDObjects)
        continue

    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  
        
    # let user save inventory to file
    elif strChoice == 's':
        FileIO.write_file(strFileName, lstOfCDObjects)
        continue
    else:
        print('General Error')


