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
            endereco = instruction[1:].lstrip("0")

            if(opcode in "0"):
                answer = f"jns {endereco}"
            elif(opcode in "1"):
                answer = f"load {endereco}"
            elif(opcode in "2"):
                answer = f"store {endereco}"
            elif(opcode in "3"):
                answer = f"add {endereco}"
            elif(opcode in "4"):
                answer = f"subt {endereco}"
            elif(opcode in "5"):
                answer = "input"
            elif(opcode in "6"):
                answer = "output"
            elif(opcode in "7"):
                answer = "halt"
            elif(opcode in "8"):
                answer = f"skipcond {endereco}"
            elif(opcode in "9"):
                answer = f"jump {endereco}"
            elif(opcode in "a"):
                answer = "clear"
            elif(opcode in "b"):
                answer = f"addi {endereco}"
            elif(opcode in "c"):
                answer = f"jumpi {endereco}"
            elif(opcode in "d"):
                answer = f"loadi {endereco}"
            elif(opcode in "e"):
                answer = f"storei {endereco}"
            
            answer = answer.rstrip()
            print(answer)

            byte = binfile.read(2)
# -------------------------------------
# Trecho a seguir obrigatório para receber os parâmetros via linha de comando.
# NÃO APAGAR!!

if __name__ == "__main__":
    main(sys.argv[1:])