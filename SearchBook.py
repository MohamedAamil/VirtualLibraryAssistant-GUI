import PySimpleGUI as sg
from Functions import SearchBook

sg.theme("Material2")

layout = [

    [sg.Image("Library.png",size=(800, 160))],
    [sg.Text("Search By" , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (80,20)),
    sg.Combo(['Author','Book'],font = ("Simplified Arabic Fixed" , 9) , background_color= "white", text_color= "black", size = (10,0) , key = 'choice' , default_value = 'Book')],
    [sg.Text("Enter a word " , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (80,20)) , sg.InputText("" , size = (20 , 1), font = ("Cambria" , 14), background_color= "#DBD9D5" , text_color=  'black' ,pad = (0 , 0) , key = 'input3')],
    [sg.Button("Done" , font = ("Simplified Arabic" , 12) , size = (15 , 0) , pad = (80,30), key = 'done')],
    [sg.Listbox([], size = (60,10) , font = ("Cambria" , 14) , key = 'tasklist' , background_color = "white" , pad = (100 , 10) , text_color = "black")],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit' , pad = (10,0))]

]

def call_search():
    global layout

    window = sg.Window("Hello", layout, size=(800, 700))

    while True:
        event, value = window.Read()
        diction = {'Author':"2" , 'Book':"1"}

        if event == 'done':
            window.FindElement('tasklist').Update('')
            val = SearchBook(diction[value['choice']] , value['input3'])
            window.FindElement('tasklist').Update(values = val)

        else:
            layout = [
                [sg.Image(
                    "Library.png",
                    size=(800, 160))],
                [sg.Text("Search By", font=("Simplified Arabic Fixed", 13), pad=(80, 20)),
                 sg.Combo(['Author', 'Book'], font=("Simplified Arabic Fixed", 9), background_color="white",
                          text_color="black", size=(10, 0), key='choice', default_value='Book')],
                [sg.Text("Enter a word ", font=("Simplified Arabic Fixed", 13), pad=(80, 20)),
                 sg.InputText("", size=(20, 1), font=("Cambria", 14), background_color="#DBD9D5", text_color='black',
                              pad=(0, 0), key='input3')],
                [sg.Button("Done", font=("Simplified Arabic", 12), size=(15, 0), pad=(80, 30), key='done')],
                [sg.Listbox([], size=(60, 10), font=("Cambria", 14), key='tasklist', background_color="white",
                            pad=(100, 10), text_color="black")],
                [sg.Button("Back", font=("Simplified Arabic", 12), size=(5, 0), key='exit', pad=(10, 0))]

            ]
            break

    window.Close()
