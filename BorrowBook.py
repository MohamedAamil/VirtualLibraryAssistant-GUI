import PySimpleGUI as sg
from Functions import BorrowBook

sg.theme("Material2")

layout = [


    [sg.Image("Library.png" , size = (800 , 160) )],
    [sg.Text("Please do remember that you can borrow only one book from the Library" , font = ( "Simplified Arabic Fixed" , 11 ) , pad = (70,30) , key = 'text'), sg.Text("               " , font = ( "Simplified Arabic Fixed" , 11 ) , key = 'name' , pad = (0,30) ,visible=False)],
    [sg.Text("Enter your ID " , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (50,50) , key = 'id') , sg.InputText("" , size = (20 , 1), font = ("Cambria" , 14), background_color= "#DBD9D5" , text_color= "black" ,pad = (0 , 0) , key = 'input3')],
    [sg.Text("Enter Book Number ", font=("Simplified Arabic Fixed", 13), pad=(50, 0), key = 'book'), sg.InputText("(1000 - 1558) ", size=(60, 1), font=("Cambria", 14), background_color="#DBD9D5", text_color="black", pad=(0, 0), key = 'input4')],
    [sg.Button("Done" , font = ("Simplified Arabic" , 12) , size = (15 , 0) , pad = (80,30), key = 'done')],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit')]
]

def call_borrow():
    global layout
    window = sg.Window("Hello" , layout, size = (800 , 700))

    while True:
        event, value = window.Read()

        if event == 'done':
            try:
                if 1000 < int(value['input4']) < 1559:
                    ID , Book , BookNum , BookName , BookAuth , name = BorrowBook(value['input3'] , value['input4'])

                    if ID and Book:
                        window.FindElement('id').Update(value = "Book Number")
                        window.FindElement('book').Update(value = "Book Name")
                        window.FindElement('input3').Update(BookNum)
                        window.FindElement('input4').Update(BookName)
                        window.FindElement('text').Update(value = "Thank You for borrowing the book - " )
                        window.FindElement('name').Update(name)
                        window.FindElement('name').Update(visible=True)
                        window.FindElement('done').Update(visible=False)

                    elif not ID:
                        window.FindElement('input3').Update(value = "Incorrect Id")

                    elif not Book:
                        window.FindElement('input4').Update(value = "You Already Borrowed a Book")

                else:
                        window.FindElement('input4').Update(value="Invalid Book Number")
            except ValueError:
                window.FindElement('input4').Update(value="That's not a Number")

        else:
            layout = [[sg.Image("Library.png" , size = (800 , 160) )],
    [sg.Text("Please do remember that you can borrow only one book from the Library" , font = ( "Simplified Arabic Fixed" , 11 ) , pad = (70,30) , key = 'text'), sg.Text("               " , font = ( "Simplified Arabic Fixed" , 11 ) , key = 'name' , pad = (0,30) ,visible=False)],
    [sg.Text("Enter your ID " , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (50,50) , key = 'id') , sg.InputText("" , size = (20 , 1), font = ("Cambria" , 14), background_color= "#DBD9D5" , text_color= "black" ,pad = (0 , 0) , key = 'input3')],
    [sg.Text("Enter Book Number ", font=("Simplified Arabic Fixed", 13), pad=(50, 0), key = 'book'), sg.InputText("(1000 - 1558) ", size=(60, 1), font=("Cambria", 14), background_color="#DBD9D5", text_color="black", pad=(0, 0), key = 'input4')],
    [sg.Button("Done" , font = ("Simplified Arabic" , 12) , size = (15 , 0) , pad = (80,30), key = 'done')],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit')]
]
            break


    window.Close()
