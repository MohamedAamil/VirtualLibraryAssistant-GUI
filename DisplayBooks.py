import PySimpleGUI as sg
from Functions import DisplayBooks

sg.theme("Material2")

val = DisplayBooks()

layout = [

    [sg.Image("Library.png",size=(800, 160))],
    [sg.Text("All Books" , font = ( "Simplified Arabic Fixed" , 17 ) , pad = (320,20))],
    [sg.Listbox(val, size = (60,17) , font = ("Cambria" , 14) , key = 'tasklist' , background_color = "white" , pad = (100 , 10) , text_color = "black")],
    [sg.Button("Back" , font = ("Simplified Arabic" , 12)  ,size = (5,0), key = 'exit' , pad = (10,0))]

]

def call_display():
    global layout
    window = sg.Window("Hello", layout, size=(800, 700))

    while True:
        event, value = window.Read()

        if event == 'exit':
            layout = [
                [sg.Image(
                    "Library.png",
                    size=(800, 160))],
                [sg.Text("All Books", font=("Simplified Arabic Fixed", 17), pad=(320, 20))],
                [sg.Listbox(val, size=(60, 17), font=("Cambria", 14), key='tasklist', background_color="white",
                            pad=(100, 10), text_color="black")],
                [sg.Button("Back", font=("Simplified Arabic", 12), size=(5, 0), key='exit', pad=(10, 0))]

            ]
            break

        else:
            continue
    window.Close()

