import string
import random

def gerar_senha_geral(tamanho):
    senha_random = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha

def gerar_senha_letras(tamanho):
    senha_random = string.ascii_letters
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha

def gerar_senha_numeros(tamanho):
    senha_random = string.digits
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha

def gerar_senha_simbolos(tamanho):
    senha_random = string.punctuation
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha

def gerar_letras_numeros(tamanho):
    senha_random = string.ascii_letters + string.digits
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha

def gerar_letras_simbolos(tamanho):
    senha_random = string.ascii_letters + string.punctuation
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha

def gerar_numeros_simbolos(tamanho):
    senha_random = string.digits + string.punctuation
    senha = ''.join(random.choice(senha_random) for i in range(tamanho))
    return senha