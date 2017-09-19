class Contact:
    
    def __init__(self,fname="",lname="",phone="",email=""):
        
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

    def __repr__ (self):
        return """
        Name = {} {}
        phone = {}
        email = {}
        """.format(self.fname,self.lname,self.phone,self.email)

class ContactManager:
    
    def __init__(self):
        self.addressBook = []
    
    def addContact(self, contact):
        self.addressBook.append(contact)
    
    def searchContactbyFirstName(self, contactName):
        for contact in self.addressBook:
            if contact.fname == contactName:
                return contact
            else:
                pass
        return 0    

    def deleteContactByFirstName(self, contactName):
        subjectContact = self.searchContactbyFirstName(contactName)
        if subjectContact != 0:
            index = self.addressBook.index(subjectContact)
            del self.addressBook[index]
            print("contact deleted")
        else:
            print("no contact found")

    def listAllContacts(self):
        if len(self.addressBook) > 0:
            for contact in self.addressBook:
                print(contact)
                print("")
                print("")
        else:
            print("no contacts in addressbook")

#getting user input
fname = input("input the first name: ")
lname = input("input the last name: ")
phone_number = input("input the phone number: ")
email = input("input the email: ")

#initializing the contactmanager
phoneBook = ContactManager()
#adding a contact
phoneBook.addContact(Contact(fname=fname, lname=lname, phone=phone_number, email=email))

phoneBook.listAllContacts()

#searching contact details of a person
print("")
search = input("Input the first name of the contact you want to search: ")
result = phoneBook.searchContactbyFirstName(search)
if result != 0:
    print(result)
else:
    print("No contact found")

#deleting a contact
print("")
search = input("Input the first name of the contact you want to delete: ")
phoneBook.deleteContactByFirstName(search)

phoneBook.listAllContacts()




    

    

