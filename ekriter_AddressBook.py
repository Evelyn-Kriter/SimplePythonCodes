#Evey Kriter/CSCI0101/11.16.2019/Lab 9

class Contact:
    '''
        A class that represents a contact in an address book
        
        Attributes:
            first  : first name
            last   : last name
            number : telephone number
            email  : email address
        Methods:
            __init__ : initialize an instance of Contact from the attributes
            __str__  : prints the first and last name of the contact    
    '''
    def __init__(self, first, last, number, email):
        self.first = first
        self.last = last
        self.number = number
        self.email = email
    
    def __str__(self):
        return self.first + " " + self.last


class AddressBook:
    '''
        A class that represents an address book
        
        Attributes:
            contacts : a list of Contact objects

        Methods:
            __init__ : creates an AddressBook from a .csv file (and reads it)
            __str__  : prints the number of contacts in the address book
            new      : creates a new contact from user input
            save     : saves all contacts to a .csv file
    '''
    def __init__( self , filename ):
        '''
            creates an AddressBook from a .csv file (and reads it)
        '''
        # initialize the contact list by reading the file
        file = open(filename, encoding='utf-8')

        # read each line in the file and add the contact information to a list of Contacts
        self.contacts = []
        for line in file:
            
            # remove the '\n' if it exists
            idx = line.find('\n')
            if idx!=-1:
                line = line[:len(line)-1]
            
            # split the contact information at the commas
            data = line.split(',')
            
            # append a new contact (this won't work until the Contact class is defined)
            self.contacts.append( Contact(data[0],data[1],data[2],data[3] ) )
        
        # close the file
        file.close()
    
    def __str__(self):
        '''
            returns a string that reports how many contacts are stored
        '''
        return "your address book has " + str(len(self.contacts)) + " contacts"
    
    def new( self ):
        '''
            creates a new contact (and adds it) by calling "input" for all
            the attributes that are needed to create a Contact object
        '''
        print("Enter first name:")
        self.first = input()
        print("Enter last name:")
        self.last = input()
        print("Enter phone number:")
        self.number = input()
        print("Enter email address")
        self.email = input()
        
        self.contacts.append(Contact(self.first, self.last, self.number, self.email))
        
    def save( self , filename ):
        '''
            writes the list of Contacts to a file in .csv format
        '''
        file = open(filename,"w")
        for contact in self.contacts:
            file.write( contact.first + "," + contact.last + "," + contact.number + ","+contact.email+"\n" )
        file.close()

# part 1a: create Contact object
contact = Contact("Mike" , "Wazowski" , 8021234567,"mwazowsk@middlebury.edu")
print(contact)

# part 2: working with an address book
# import the initial contacts
book = AddressBook( 'contacts.csv' )
print(book) # how many contacts do we currently have?

# create a new contact
book.new()
print(book) # how many contacts do we have now?

# save the address book to a new file
book.save( "updated_contacts.csv" )

# part 3: explain how you would modify the attributes/methods
#         of your AddressBook to solve one of the following problems:
#     - searching for (maybe you want to edit or remove) a specific contact
#     - listing all contacts whose last name starts with a certain character
#     - listing all Middlebury contacts (you can assume those contacts have a @middlebury.edu email)
'''
To find a specific contact, I would create a for loop with a range length of the address book list
and then I would make an if statement for whether the string of the name we are looking for
is "in" the address book list[index]. If the statement is true then we print out the list and index number,
and the contact list in that list which will contain the first and last name, email address, and phone number.
'''
