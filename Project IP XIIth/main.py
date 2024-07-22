import pandas as pd
import matplotlib.pyplot as plt
from  datetime import date

def addBook():
    bookid = int(input("Enter a book id : "))
    title = input("Enter book title : ")
    author = input("Enter author of the book : ")
    publisher = input("Enter book publisher : ")
    edition = input("Enter edition of book : ")
    cost = int(input("Enter cost of the book : "))
    category = input("Enter category of book : ")
    bdf = pd.read_csv("books.csv")
    n = bdf["bookid"].count()
    bdf.at[n] = [bookid,title,author,publisher,edition,cost,category]
    bdf.to_csv("books.csv",index = False)
    print("Book added successfully")

print("_"*30)
print("    CHOOSE AN OPTION     ")
print("_"*30)
print("Press 1 - ADD A NEW MEMBER")
print("Press 2 - DELETE AN EXISTING  MEMBER")
print("Press 3 - SHOW ALL MEMBERS")
print("Press 4 - ADD A NEW BOOK")
print("Press 5 - DELETE AN EXISTIING BOOK ")
print("Press 6 - SHOW ALL BOOKS ")
print("Press 7 - ISSUE A BOOK ")
print("Press 8 - RETURN A BOOK ")
print("Press 9 - SHOW ISSUED BOOKS")
print("Press 10 - SHOW RETURNED BOOKS ")
print("Press 11 - EXIT")
ch=int(input("Enter Your choice : "))
if ch==1 :
    addBook()
"""elif ch== 2:
    deletemember()     
elif ch== 3 :
    showmembers()
elif ch== 4 :
    addbook()
elif ch== 5 :
    deletebook()
elif ch== 6 :
    showbooks()
elif ch== 7 :
    issue()
elif ch== 8 :
    returnbook()
elif ch== 9 :
    issuedbooks()
elif ch== 10 :
    returnedbooks
elif ch== 11 :
    break
"""
