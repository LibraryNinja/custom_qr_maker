import PySimpleGUI as sg
from pathlib import Path
import os

working_directory = os.getcwd()

def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    sg.popup_error('Missing File Path')
    return False


def make_qr(toqr, outputname, outputpath):
    import qrcode

    img = qrcode.make(toqr)

    type(img) #qrcode.image.pil.PilImage

    filename = (f'{outputname}.png')
    img.save(Path(outputpath) /filename)

def main_window():
    layout = [
        [sg.T('Simple tool for generating QR Codes', s=40, justification='l')],
        [sg.HorizontalSeparator()],
        
        [sg.T("Enter string/URL to make into a QR code:")], 
         
        [sg.Multiline(default_text="", s=(35, 3), background_color="White", text_color="Black", key='-TOQR-')],

        [sg.HorizontalSeparator()],

        [sg.T('Enter Output Filename:')],
        
        [sg.Input(default_text='', background_color="White", text_color="Black", s=25, key='-OUTPUT_NAME-')],

        [sg.T('Save File To:', s=10, justification='l'), 
        sg.Input(background_color="White", text_color="Black", s=25, key='-OL_OUT-'), sg.FolderBrowse()], 

        [sg.HorizontalSeparator()],
        [sg.Button('Run', button_color='OliveDrab', s=16), sg.Exit(s=16, button_color='OrangeRed3'),]]



    window_title = "QR Code Generator"
    window = sg.Window(window_title, layout, use_custom_titlebar=True)

    while True:
        event, values = window.read()
        #print(event,values)
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
       
        if event == 'Run':
            make_qr(toqr=values['-TOQR-'], outputname=values['-OUTPUT_NAME-'], outputpath=values['-OL_OUT-'])
            print(values['-TOQR-'])
            sg.popup("Finished!")

    window.close()



if __name__ == '__main__':
    SETTINGS_PATH = Path.cwd()
    theme = 'LightBlue7'
    font_family = 'Arial'
    #Sets value as integer
    font_size = 16
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    main_window()