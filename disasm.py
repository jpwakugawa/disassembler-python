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
        byte = binfile.read(2)
        while byte:
            instruction = byte.hex()
            opcode = instruction[0]
            endereco = instruction[1:]

            if(opcode in "0"):
                print(f"jns {endereco}")
            elif(opcode in "1"):
                print(f"load {endereco}")
            elif(opcode in "2"):
                print(f"store {endereco}")
            elif(opcode in "3"):
                print(f"add {endereco}")
            elif(opcode in "4"):
                print(f"subt {endereco}")
            elif(opcode in "5"):
                print("input")
            elif(opcode in "6"):
                print("output")
            elif(opcode in "7"):
                print("halt")
            elif(opcode in "8"):
                print(f"skipcond {endereco}")
            elif(opcode in "9"):
                print(f"jump {endereco}")
            elif(opcode in "a"):
                print("clear")
            elif(opcode in "b"):
                print(f"addi {endereco}")
            elif(opcode in "c"):
                print(f"jumpi {endereco}")
            elif(opcode in "d"):
                print(f"loadi {endereco}")
            elif(opcode in "e"):
                print(f"storei {endereco}")

            byte = binfile.read(2)
    

# -------------------------------------
# Trecho a seguir obrigatório para receber os parâmetros via linha de comando.
# NÃO APAGAR!!

if __name__ == "__main__":
    main(sys.argv[1:])