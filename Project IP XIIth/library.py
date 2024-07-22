#IP PROJECT
#Abanaa Nanda Class:XII-A
import pandas as pd
from datetime import date

def addNewBook():
    bookid = int(input("Enter a book id: "))
    title = input("Enter book title: ")
    author = input("Enter author of the book: ")
    publisher = input("Enter book publisher: ")
    edition = input("Enter edition of book: ")
    cost = int(input("Enter cost of the book: "))
    category = input("Enter category of book: ")
    bdf = pd.read_csv(r"Project IP XIIth\books.csv")
    
    # Creating a new row as a DataFrame
    new_book = pd.DataFrame([[bookid, title, author, publisher, edition, cost, category]], 
                            columns=["bookid", "title", "author", "publisher", "edition", "cost", "category"])
    
    # Appending the new row to the DataFrame
    bdf = pd.concat([bdf, new_book], ignore_index=True)
    
    bdf.to_csv(r"Project IP XIIth\books.csv", index=False)
    print("Book added successfully")

def login():
    uname = input("Enter Username: ")
    pwd = input("Enter Password: ")
    df = pd.read_csv(r"Project IP XIIth\users.csv")
    df = df.loc[df["username"] == uname]
    if df.empty:
        print("Invalid Username given")
        return False
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True

def searchBook():
    name = input("Enter book title to be searched: ")
    bdf = pd.read_csv(r"Project IP XIIth\books.csv")
    df = bdf.loc[bdf["title"] == name]
    if df.empty:
        print("No book found with given title")
        return False
    else:
        print("Book details are:")
        print(df)
        return True

def deleteBook():
    name = input("Enter book title to be deleted: ")
    bdf = pd.read_csv(r"Project IP XIIth\books.csv")
    bdf = bdf.drop(bdf[bdf["title"] == name].index)
    bdf.to_csv(r"Project IP XIIth\books.csv", index=False)
    print("Book Deleted Successfully")

def showBooks():
    bdf = pd.read_csv(r"Project IP XIIth\books.csv")
    print(bdf)

def addNewMember():
    mid = int(input("Enter Member id: "))
    name = input("Enter name of the member: ")
    phone = input("Enter phone number: ")
    email = input("Enter email id: ")
    address = input("Enter address: ")
    number = 0
    mdf = pd.read_csv(r"Project IP XIIth\members.csv")
    
    new_member = pd.DataFrame([[mid, name, phone, email, address, number]], 
                              columns=["Memberid", "Name", "Phone", "Email", "Address", "Number"])
    mdf = pd.concat([mdf, new_member], ignore_index=True)
    mdf.to_csv(r"Project IP XIIth\members.csv", index=False)
    print("Member added successfully")

def searchMember():
    name = input("Enter member name to be searched: ")
    mdf = pd.read_csv(r"Project IP XIIth\members.csv")
    df = mdf.loc[mdf["Name"] == name]
    if df.empty:
        print("No member found with given name")
        return False
    else:
        print("Member details are:")
        print(df)
        return True

def deleteMember():
    name = input("Enter member name to be deleted: ")
    mdf = pd.read_csv(r"Project IP XIIth\members.csv")
    mdf = mdf.drop(mdf[mdf["Name"] == name].index)
    mdf.to_csv(r"Project IP XIIth\members.csv", index=False)
    print("Member Deleted Successfully")

def showMembers():
    mdf = pd.read_csv(r"Project IP XIIth\members.csv")
    print(mdf)

def issueBook():
    bname = input("Enter Book name to be searched: ")
    df = pd.read_csv(r"Project IP XIIth\books.csv")
    df = df.loc[df["title"] == bname]
    if df.empty:
        print("No Book Found in the Library")
        return

    mname = input("Enter member name to be searched: ")
    df = pd.read_csv(r"Project IP XIIth\members.csv")
    df = df.loc[df["Name"] == mname]
    if df.empty:
        print("No such Member Found")
        return

    idf = pd.read_csv(r"Project IP XIIth\issuedbooks.csv")
    book_issue = [bname, mname, date.today(), ""]
    n = idf["book_name"].count()
    idf.at[n] = book_issue
    idf.to_csv(r"Project IP XIIth\issuedbooks.csv", index=False)
    print("Book Issued Successfully")

def showIssuedBooks():
    idf = pd.read_csv(r"Project IP XIIth\issuedbooks.csv")
    print(idf)

def returnBook():
    bname = input("Enter Book to be returned: ")
    mname = input("Enter Member who has the book: ")
    idf = pd.read_csv(r"Project IP XIIth\issuedbooks.csv")
    idf = idf.loc[idf["book_name"] == bname]
    if idf.empty:
        print("The book is not issued in records")
    else:
        idf = idf.loc[idf["member_name"] == mname]
        if idf.empty:
            print("The book is not issued to the member")
        else:
            print("Book can be returned")
            ans = input("Are you sure you want to return the book: ")
            if ans.lower() == "yes":
                idf = pd.read_csv(r"Project IP XIIth\issuedbooks.csv")
                idf = idf.drop(idf[idf["book_name"] == bname].index)
                idf.to_csv(r"Project IP XIIth\issuedbooks.csv", index=False)
                print("Book Returned Successfully")
            else:
                print("Return operation cancelled")


def showMenu():
    print("-----------------------------")
    print("       FAITH ACADEMY LIBRARY        ")
    print("-----------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - To Exit")
    choice = int(input("Enter your choice: "))
    return choice

if login():
    while True:
        ch = showMenu()
        if ch == 1:
            addNewBook()
        elif ch == 2:
            searchBook()
        elif ch == 3:
            deleteBook()
        elif ch == 4:
            showBooks()
        elif ch == 5:
            addNewMember()
        elif ch == 6:
            searchMember()
        elif ch == 7:
            deleteMember()
        elif ch == 8:
            showMembers()
        elif ch == 9:
            issueBook()
        elif ch == 10:
            returnBook()
        elif ch == 11:
            showIssuedBooks()        
        elif ch == 12:
            break
        else:
            print("Invalid Option Selected")
