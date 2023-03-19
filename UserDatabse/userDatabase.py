import sqlite3

conn = sqlite3.connect('userDatabase.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS User(Name TEXT(30), Username TEXT(30) PRIMARY KEY, Email TEXT(50), Password TEXT(25))")
conn.commit()

class User:
    def __init__(self, dbname):
        self.dbname = dbname
        self.load()

    def load(self):
        str = "SELECT * FROM User"
        cursor.execute(str)
        cursor.fetchall()

    def get_user(self, email):
        str = "SELECT  * FROM User WHERE Email = ?"
        cursor.execute(str, (email, ))
        data = cursor.fetchall()
        if data:
            #for x in data:
            #   print(x[0], x[1], x[2], x[3])
            return data[0]
        else:
            print("Email does not exist")
            return -1

    def valide_email(self, email):
        if email[-10::1] == "@gmail.com" and email[-10::1].islower():
            return True
        else:
            return False
    
    def add_user(self, name, username, email, password):
        str = "SELECT * FROM User WHERE Email = ?"
        cursor.execute(str, (email, ))
        data = cursor.fetchall()
        if not data:
            if self.valide_email(email):
                str1 = "INSERT INTO User VALUES(?, ?, ?, ?)"
                cursor.execute(str1, (name, username, email, password))
                conn.commit()
                return 1
            else:
                print("Invalid Email")
                return -1
        else:
            print("Email already exists")
            return -1

    def validate(self, email, password):
        str = "SELECT Password FROM  User WHERE Email = ?"
        cursor.execute(str, (email, ))
        data = cursor.fetchall()
        if self.get_user(email) != -1:
            return data[0][0] == password
        else:
            return False

x = User("userDatabase.db")
print(x.valide_email("bridsahil007@gmail.com"))
print(x.validate("omkars@gmail.com", "Omkar22"))
x.add_user("Omkar", "omkars", "omkars@gmail.com", "Omkar22")

cursor.execute("CREATE TABLE IF NOT EXISTS Cart(Price TEXT)")
conn.commit()

class Item:
    def __init__(self, dbname):
        self.dbname = dbname
        self.load()

    def load(self):
        str = "SELECT * FROM CART"
        cursor.execute(str)
        cursor.fetchall()

    def add(self):
        pass

'''user1 = User("Sahil", "sahilbrid", "bridsahil007@gmail.com", "Sahilbrid007")
user2 = User("Rohan", "rohanbrid", "bridrohan1122@gmail.com", "rohan@1812")
        

cursor.execute("INSERT INTO User VALUES(?, ?, ?, ?)", (user1.name, user1.username, user1.email, user1.password))
conn.commit()

cursor.execute("INSERT INTO User  VALUES(?, ?, ?, ?)", (user2.name, user2.username, user2.email, user2.password))
conn.commit()
'''