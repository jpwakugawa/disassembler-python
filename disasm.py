#!/usr/bin/python3

import sys

def main(argv):
    if (len(argv) == 0):
        print('Error: inform a filename to disassemble.')
        exit()
     
    # Nome do arquivo binário de entrada
    filename = argv[0]
    
    # Opção 'rb' abre o arquivo para leitura em formato binário
    with open(filename, 'rb') as binfile:
        #
        # Seu código começa aqui!
        # 
        # Utilize a variável "binfile" para ler os bytes do arquivo
        #
    

# -------------------------------------
# Trecho a seguir obrigatório para receber os parâmetros via linha de comando.
# NÃO APAGAR!!

if __name__ == "__main__":
    main(sys.argv[1:])