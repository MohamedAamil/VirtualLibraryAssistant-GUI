import PySimpleGUI as sg
from Functions import ReturnBook

sg.theme("Material2")


layout = [

    [sg.Image("Library.png", size=(800, 160))] ,
    [sg.Text("Enter your ID " , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (80,40) , key = 'id') , sg.InputText("" , size = (60 , 1), font = ("Cambria" , 14), background_color= "#DBD9D5" , text_color= "black" ,pad = (0 , 0) , key = 'input3')],
    [sg.Button("Done" , font = ("Simplified Arabic" , 12) , size = (15 , 0) , pad = (80,20), key = 'done')],
    [sg.Text("Thank You for Returning the book", font=("Simplified Arabic Fixed", 11), pad=(240, 40), visible=False, key='tet'), sg.Text("                    ", font=("Simplified Arabic Fixed", 11), key='name', pad=(250, 10) , visible = False)],
    [sg.Text("Our Record has been updated on your Book Return" , key = 'text6', font = ( "Simplified Arabic Fixed" , 12 ) , pad = (140,30) , visible = False)],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit' , pad = (10,10))]

]


def call_return():
    global layout
    window = sg.Window("Hello", layout, size=(800, 700))

    while True:
        event, value = window.Read()

        if event == 'done':
            try:
                ID , Book , BookName , name = ReturnBook(value['input3'])

                if ID and Book:
                    window.FindElement('id').Update("Book Name ")
                    window.FindElement('input3').Update(BookName)
                    window.FindElement('text6').Update(visible = True)
                    window.FindElement('exit').Update(visible=True)
                    window.FindElement('done').Update(visible=False)
                    window.FindElement('tet').Update(visible=True)
                    window.FindElement('name').Update(name)
                    window.FindElement('name').Update(visible=True)


                elif not ID:
                    window.FindElement('input3').Update(value="Incorrect Id")

                elif not Book:
                    window.FindElement('input3').Update(value = "NO Books Borrowed")
            except ValueError:
                window.FindElement('input3').Update(value="That's not a Number")


        else:
            layout = [
                [sg.Image(
                    "Library.png",
                    size=(800, 160))],
                [sg.Text("Enter your ID ", font=("Simplified Arabic Fixed", 13), pad=(80, 40), key='id'),
                 sg.InputText("", size=(60, 1), font=("Cambria", 14), background_color="#DBD9D5", text_color="black",
                              pad=(0, 0), key='input3')],
                [sg.Button("Done", font=("Simplified Arabic", 12), size=(15, 0), pad=(80, 20), key='done')],
                [sg.Text("Thank You for Returning the book", font=("Simplified Arabic Fixed", 11), pad=(240, 40),
                         visible=False, key='tet'),
                 sg.Text("                    ", font=("Simplified Arabic Fixed", 11), key='name', pad=(250, 10),
                         visible=False)],
                [sg.Text("Our Record has been updated on your Book Return", key='text6',
                         font=("Simplified Arabic Fixed", 12), pad=(140, 30), visible=False)],
                [sg.Button("Back", font=("Simplified Arabic", 12), size=(5, 0), key='exit', pad=(10, 10))]
            ]
            break

    window.Close()
