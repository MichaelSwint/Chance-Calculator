import PySimpleGUI as sg
import sys


#Set the theme for the gui (text, colors background, colors etc.)
sg.theme("DarkAmber")

#This is the contents of the window!
layout=[[sg.Text("Enter the chance in decimal format (%1 = .01)")],
        [sg.InputText(key='-Chance-')],
        [sg.Text("Enter the series(number of runs)")],
        [sg.InputText(key='-Runs-')],
        [sg.Submit(), sg.Cancel()],
]
#The contents are wraped within the window.
window = sg.Window('Chance Calculator', layout)

#Grab the user input.
event, values = window.read()

#Close the main menu to free up thread.
window.close()

#Function to calculate the chance.
def calc_chance(series, per):
       chance = 1-((1-per)**series)
       return chance

#If the user cancels or closes the window, no need to run remainder of program.
if event == sg.WIN_CLOSED or event == 'Cancel':
        exit()

#User input is currently type string, this converts to float.
float_Chance = float(values['-Chance-'])
float_Runs = float(values['-Runs-'])

#Pass the values to calc_chance function
chance = calc_chance(float_Runs, float_Chance)

#Create a 'popup' window with the completed calculation!
sg.popup(F"The chance of an event occuring at least once over {values['-Runs-']} runs is {chance:.10%}")




