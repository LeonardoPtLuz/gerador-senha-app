import PySimpleGUI as sg
from layout_main import *
from gerador_senha import *

def logica():
    window = layout_main()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        senha = ''
        
        if event == "Gerar":
            try:
                quantidade_caracteres = int(values['-INPUT-'])

                if quantidade_caracteres <= 0 or values['-LETRAS-'] == False and values['-NUMEROS-'] == False and values['-SIMBOLOS-'] == False:
                    window['-OUTPUT-'].update('Apenas números inteiros maiores que zero!')
                    continue

                if values['-LETRAS-']:
                    senha = gerar_senha_letras(quantidade_caracteres)

                if values['-NUMEROS-']:
                    senha = gerar_senha_numeros(quantidade_caracteres)

                if values['-SIMBOLOS-']:
                    senha = gerar_senha_simbolos(quantidade_caracteres)

                if values['-LETRAS-'] and values['-NUMEROS-']:
                    senha = gerar_letras_numeros(quantidade_caracteres)

                if values['-LETRAS-'] and values['-SIMBOLOS-']:
                    senha = gerar_letras_simbolos(quantidade_caracteres)

                if values['-NUMEROS-'] and values['-SIMBOLOS-']:
                    senha = gerar_numeros_simbolos(quantidade_caracteres)

                if values['-LETRAS-'] and values['-NUMEROS-'] and values['-SIMBOLOS-']:
                    senha = gerar_senha_geral(quantidade_caracteres)
                    
                window['-OUTPUT-'].update('Senha gerada: ' + f'--> {senha} <--')

            except ValueError:
                window['-OUTPUT-'].update('Apenas números inteiros maiores que zero!')

        elif event == "Limpar":
            window['-INPUT-'].update('')
            window['-OUTPUT-'].update('')
            window['-LETRAS-'].update('')
            window['-NUMEROS-'].update('')
            window['-SIMBOLOS-'].update('')

    window.close()