class Contact:
    
    def __init__(self,cname,phoneno,email,website,bday):
        
        self.cname = cname
        self.phoneno = phoneno
        self.email = email
        self.website = website
        self.bday = bday


cname = input('Name: ')
phoneno = input('Phone: ')
email = input('Email: ')
website = input('Website: ')
bday = input("bday: ")

newContact = Contact(cname,phoneno,email,website,bday)
print(newContact.cname)
print(newContact.phoneno)
print(newContact.email)
print(newContact.website)
print(newContact.bday)




    

    

