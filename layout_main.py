import PySimpleGUI as sg


def layout_main():
    sg.theme('DarkAmber')
    layout = [[sg.Text("Quantidade de caracteres:")],
            [sg.Input(key='-INPUT-')],
            [sg.Checkbox(''), sg.Text("Letras.")],
            [sg.Checkbox(''), sg.Text("Números.")],
            [sg.Checkbox(''), sg.Text("Símbolos.")],
            [sg.Text(size=(40, 2), key='-OUTPUT-')],
            [sg.Button('Gerar'), sg.Button('Limpar'), sg.Button('Sair')]]
    return sg.Window('Gerador de Senha', layout=layout, finalize=True)