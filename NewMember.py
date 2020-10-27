import PySimpleGUI as sg
from Functions import NewMember

sg.theme("Material2")

id = 0

layout = [


    [sg.Image("Library.png" , size = (800 , 160) ) ],
    [sg.Text("Hello and Welcome to our Library, fully dedicated to The Physics Department" , font = ( "Simplified Arabic Fixed" , 11 ) , pad = (50,30) , key = 'text1') ,sg.Text("You have to create an id to proceed with the library" , font = ( "Simplified Arabic Fixed" , 11 ) , pad = (150,30) , key = 'text3', visible=False)  ],
    [sg.Text("Are you New Here  " , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (300,50), key = 'text2') ,sg.Text("Enter Your Name  " , font = ( "Simplified Arabic Fixed" , 13 ) , pad = (300,10), key = 'text4', visible=False)],
    [sg.Button("Yes" , font = ("Simplified Arabic" , 12) , size = (10 , 0) , pad = (200,10), key = 'choice1') , sg.Button("No" , font = ("Simplified Arabic" , 12) , size = (10 , 0) , pad = (10,10) , key = 'choice2') ],

    [sg.InputText("" , size = (20 , 1), font = ("Cambria" , 14), background_color= "#DBD9D5" , text_color= "black" ,pad = (270 , 0) , key = 'input1', visible=False) , sg.Button("Done" , font = ("Simplified Arabic" , 12) , size = (10 , 0) , pad = (200,10), key = 'button1' , visible = False)],
    [sg.Text("Your Id is " ,  font = ( "Simplified Arabic Fixed" , 13 ) ,pad = (325 , 30) ,visible = False ,  key = 'text5'),sg.Text("   ",  font = ( "Simplified Arabic Fixed" , 13 ) ,pad = (15, 0) ,visible = False ,  key = 'text6') ],
    [sg.Button("Next" , font = ("Simplified Arabic" , 12) , size = (40 , 0) , pad = (225,40), key = 'exit' , visible = False)]

]



window = sg.Window("Hello" , layout, size = (800 , 700))


def show_page():
    window.FindElement('text3').Update(visible=True)
    window.FindElement('text4').Update(visible=True)
    window.FindElement('input1').Update(visible=True)
    window.FindElement('button1').Update(visible=True)

def new_member(value):
    global id , check
    name = value['input1']
    id = NewMember(str(name))
    window.FindElement('text5').Update(visible=True)
    window.FindElement('text6').Update(visible=True,value = id)
    window.FindElement('exit').Update(visible = True)
    window.FindElement('button1').Update(visible=False)


while True:
    event , value = window.Read()

    if event == 'choice1':
        window.FindElement('text1').Update(visible= False)
        window.FindElement('choice1').Update(visible=False)
        window.FindElement('text2').Update(visible=False)
        window.FindElement('choice2').Update(visible=False)
        show_page()

    elif event == 'button1':
        new_member(value)

    else:
        break


window.Close()