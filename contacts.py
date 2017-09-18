class Contact:
    
    def __init__(self,cname,phoneno,email,website,bday):
        
        self.cname = cname
        self.phoneno = phoneno
        self.email = email
        self.website = website
        self.bday = bday


    def __repr__ (self):
        return """
        Contact
        Name = {}
        phone = {}
        email = {}
        website = {}
        bday = {}
        """.format(self.cname,self.phoneno,self.email,self.website,self.bday)

cname = input('Name: ')
phoneno = input('Phone: ')
email = input('Email: ')
website = input('Website: ')
bday = input("bday: ")

newContact = Contact(cname,phoneno,email,website,bday)
print(newContact)




    

    

