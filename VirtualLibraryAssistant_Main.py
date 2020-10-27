import PySimpleGUI as sg
from BorrowBook import call_borrow
from ReturnBook import call_return
from SearchBook import call_search
from DisplayBooks import call_display
import NewMember

sg.theme("Material2")

layout = [

    #title page
    [sg.Image("Library.png" , size = (800 , 160) )],
    [sg.Text("Home Screen " , font = ( "Simplified Arabic Fixed" , 17 ) , pad = (313,20), key = 'home')],
    [sg.Button("Borrow a Book " , font = ("Simplified Arabic" , 13) , size = (40 , 0) , pad = (225,18), key = 'borrow')],
    [sg.Button("Return a Book " , font = ("Simplified Arabic" , 13) , size = (40 , 0) , pad = (225,18), key = 'return')],
    [sg.Button("Search a Book " , font = ("Simplified Arabic" , 13) , size = (40 , 0) , pad = (225,18), key = 'search')],
    [sg.Button("Display all Books " , font = ("Simplified Arabic" , 13) , size = (40 , 0) , pad = (225,18), key = 'display')],
    [sg.Button("Exit " , font = ("Simplified Arabic" , 13) , size = (40 , 0) , pad = (225,18), key = 'exit')],
    [sg.Image("Creator.png" , size = (800 , 160) )]

]


window = sg.Window("Hello" , layout, size = (800 , 700))

while True:
    event, value = window.Read()

    if event == 'borrow':
        call_borrow()

    elif event == 'return':
        call_return()

    elif event == 'search':
        call_search()

    elif event == 'display':
        call_display()


    else:
        break



window.Close()
