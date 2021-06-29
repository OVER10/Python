#!/usr/bin/env python3
import PySimpleGUI as sg
import pyperclip

# Example SMB path below:
# smb://hap-it-mgmt/installers/WinDirStat

# Function to convert SMB path to UNC path
def smb2unc(input):
    return input.replace('/','\\').replace('smb:','')

# Overall style/colours/font for PySimpleGUI
sg.theme('Dark Grey 2')

# Creates a layout for initial window to be called later
layout = [[sg.Text('Please enter any SMB path to convert to UNC: ')],
                [sg.Input(key='-IN-')],
                [sg.Button('Convert'), sg.Exit()]]

# Creates an actual window with a title and previously created layout
window = sg.Window('SMB Converter', layout)

# Uses 'event' trigger which is basically user 'click' to determine what happens
while True:
    event, values = window.read()
    text_input = smb2unc(values['-IN-'])
    if event == 'Convert':
        pyperclip.copy(text_input)
        sg.popup('UNC Path Copied!', text_input)
        break
    elif event == sg.WIN_CLOSED or event == 'Exit':
        break
    window.close()







#print(smb2unc())





#print(str(input("Please enter your SMB path for conversion: ")).replace("/","\\").replace("smb:", ""))
