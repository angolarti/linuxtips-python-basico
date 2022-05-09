#!/usr/bin/env python3

"""
Hello World Muili Language

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_PT.utf8


Execução:
    python3 hello.py
    ou
    ./hello.py
"""

# metadatos: são informações adicionais que não fazer necessaria parte do 
# programa para executar
__version__ = '0.0.1'
__author__ = 'Walter Angolar'
__license__ = 'Unlicense'


import os


current_language = os.getenv('LANG', 'en_GB')[:5]
mensage = 'Hello World!'


if __name__ == '__main__':

    if current_language == 'pt_PT':
        mensage = 'Olá, Mundo!'
    elif current_language == 'it_IT':
        mensage = 'Ciao, Mondo!'
    elif current_language == 'es_SP':
        mensage = 'Hola, Mundo!'
    else current_language = 'fr_FR':
        mensage = 'Bonjour Monde!'
 
    print(mensage)  # test-ignore
