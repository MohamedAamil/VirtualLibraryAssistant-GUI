
#Global Declaration

Dot = "."
SEndLine = "\n"
StringZero = str(0)
Tab = "\t\t\t\t\t"
TEndLine = "\n\n\n"
Plus = "+"

#NEW MEMBER ID CREATION
def NewMember(mname):

    #Variables
    count = 1

    #Opening File
    ma = open("MemberDetails.txt","a")
    mr = open("MemberDetails.txt", "r")

    #Getting Total Lines in File
    for i in mr:
        count += 1

    #Member ID
    Mid = 100 + count


    #Writing in the File
    ma.write(str(Mid))
    ma.write(Dot)
    ma.write(mname)
    ma.write(Dot)
    ma.write(StringZero)
    ma.write(SEndLine)

    #Closing File
    ma.close()
    mr.close()

    return Mid


#DISPLAYING ALL THE BOOKS
def DisplayBooks():
    val = []
    elem = " "

    # Opening Files
    bk = open("BookTitlesNum.txt", "r")
    bs = open("BookTitlesNum.txt", "r")

    # Getting Total Line in the File
    array = bs.readlines()
    size = len(array)
    bs.close()

    # Reading Every line in the BookTitles File
    for i in range(size):
        data = bk.readline()
        data = data.split(Plus)

        # Passing the Book Bame alone to a variable
        search = data[1].lower()

        # Checking if the word matches and Displays the same
        if elem in search:
            val.append(data[0] + "  " + data[1])
    #Closing File
    bk.close()

    return val


#BORROWING BOOK
def BorrowBook(mid , bnum):

    #Variables
    check = False
    ID = True
    Book = True
    BookNum = 0
    BookName = " "
    BookAuth = " "
    size = 1

    #Opening Files
    ma = open("MemberDetails.txt","r+")
    bk = open("BookTitlesNum.txt", "r")
    ms = open("MemberDetails.txt","r")

    #Getting Total Line in the File
    array = ms.readlines()
    size = len(array)

    #Closing File
    ms.close()

    #Checking if ID matches with the file data
    for i in range(size):
        data = ma.readline()
        data = data.split(Dot)
        if int(data[0]) == int(mid):
            name = data[1]
            check = True
            break

    #If ID Matches then,
    if check:

        #Checking If User Already has a Book Borrowed
        if data[2].strip() == StringZero:

            #Reading File by Line
            book = bk.readline()

            #Checking if Book Number Matches User Input
            while book != ' ':
                book = book.split(Plus)
                if book[0] == bnum:
                    BookNum = book[0]
                    BookName = book [1]
                    BookAuth = book[2]
                    break
                else:
                    book = Plus.join(book)
                    book = bk.readline()

            #Formatting Book data according to the MemberDetails.txt File
            book[1] = book[1] + "\n"
            data[2] = book[1]

            #Joining the Data which was splitted Before
            data = Dot.join(data)

            #Closing File
            ma.close()

            #Opening File Again to read the data from beginning
            ma = open("MemberDetails.txt", "r")

            #Storing all the Data of file in Variable Data
            Data = ma.readlines()

            #Finding the Line where User's data is present in the File
            Value = int(mid) - 101

            #Replacing hte previous stored Data with Updated one
            Data[Value] = data

            #Closing File Again
            ma.close()

            #Opening File for Writing
            ma = open("MemberDetails.txt","w")

            #Writing in File
            ma.writelines(Data)

            #Closing File
            ma.close()
            bk.close()

        #If User Already has a Book borrowed
        else:
            Book = False

    #If ID does not match
    else:
        ID = False

    return ID , Book , BookNum , BookName , BookAuth ,name


#RETURNING BOOK
def ReturnBook(mid):

    #Variables
    check = False
    size = 0
    ID = True
    Book = True
    BookName = " "
    name = " "

    #Opening Files
    ma = open("MemberDetails.txt", "r")
    ma = open("MemberDetails.txt","r")
    ms = open("MemberDetails.txt", "r")

    # Getting Total Line in the File
    array = ms.readlines()
    size = len(array)

    # Closing File
    ms.close()


    #Checking if ID matches with the file data
    for i in range(size):
        data = ma.readline()
        data = data.split(Dot)
        if int(data[0]) == int(mid):
            name = data[1]
            check = True
            break

    #Closing File
    ma.close()

    #If User ID is valid
    if check:

        #To check if Book is Borrowed
        if data[2].strip() != StringZero:

            BookName = data[2]

            #Formatting Data as per the File and joining
            data[2] = StringZero + "\n"
            data = Dot.join(data)

            #Opening File
            ma = open("MemberDetails.txt","r")


            #Storing All the Files Data in "Data"
            Data = ma.readlines()
            Value = int(mid) - 101
            Data[Value] = data

            #Closing File
            ma.close()

            #Opening File, Writing the New Data, Closing File
            ma = open("MemberDetails.txt","w")
            ma.writelines(Data)
            ma.close()

        #If no Books are Borrowed
        else:
            Book = False

    #If ID does not match
    else:
        ID = False

    return ID, Book, BookName ,name


#SEARCH BOOK
def SearchBook(choice ,elem):

    val = []

    #Opening Files
    bk = open("BookTitlesNum.txt", "r")
    bs = open("BookTitlesNum.txt", "r")

    #Getting Total Line in the File
    array = bs.readlines()
    size = len(array)
    bs.close()


    #To search by Book Name
    if choice == "1":


        #Reading Every line in the BookTitles File
        for i in range(size):
            data = bk.readline()
            data = data.split(Plus)

            #Passing the Book Bame alone to a variable
            search = data[1].lower()

            #Checking if the word matches and Displays the same
            if elem in search:
                val.append(data[0] + "  " + data[1])


    #To Search by Author Name
    elif choice == "2":

        #Reading Every line in the BookTitles File
        for i in range(size):
            data = bk.readline()
            data = data.split(Plus)

            # Passing the Author Name alone to a variable
            search = data[2].lower()

            # Checking if the Name matches and Displays the same
            if elem in search:
                val.append(data[0] + "  " + data[1])

    #Closing the File
    bk.close()

    return val


