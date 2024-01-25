import PySimpleGUI as sg

def layout_main():
    sg.theme('DarkAmber')
    layout = [[sg.Text("Quantidade de caracteres:")],
            [sg.Input(key='-INPUT-')],
            [sg.Checkbox('', key="-LETRAS-"), sg.Text("Letras.")],
            [sg.Checkbox('', key="-NUMEROS-"), sg.Text("Números.")],
            [sg.Checkbox('', key="-SIMBOLOS-"), sg.Text("Símbolos.")],
            [sg.Text(size=(40, 2), key='-OUTPUT-')],
            [sg.Button('Gerar'), sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('Gerador de Senha', layout=layout, finalize=True)