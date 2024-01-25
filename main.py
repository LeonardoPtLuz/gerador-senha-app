import PySimpleGUI as sg
from layout_main import *
from gerador_senha import *

def main():

    window = layout_main()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        
        if event == "Gerar":
            try:
                quantidade_numeros = int(values['-INPUT-'])

                if quantidade_numeros <= 0:
                    window['-OUTPUT-'].update('Apenas números inteiros maiores que zero!')
                    continue
                    
                senha = gerar_senha_geral(quantidade_numeros)
                window['-OUTPUT-'].update('Senha gerada: ' + f'--> {senha} <--')

            except ValueError:
                window['-OUTPUT-'].update('Apenas números inteiros maiores que zero!')

        elif event == "Limpar":
            window['-INPUT-'].update('')
            window['-OUTPUT-'].update('')

    window.close()

if __name__ == "__main__":
    main()