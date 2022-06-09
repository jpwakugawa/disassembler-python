# Disassembler-Python-MARIE 


## Descrição

Um programa "disassembler" é responsável por fazer o inverso de um programa "assembler".

Em um "assembler", um programa escrito em linguagem de montagem(texto) é convertido para binário (linguagem de máquina) para ser executado na CPU. Em um "disassembler", o processo inverso é feito: o código binário do programa em linguagem de máquina é convertido novamente para linguagem de montagem.

A arquitetura utilizada foi [MARIE](https://marie.js.org/book.pdf) (**M**achine **A**rchitecture that is **R**eally **I**ntuitive and **E**asy)

## Como utilizar

- Passe o arquivo binário como argumento para converter:
    ```bash
    python3 disasm.py marie_instruction.bin
    ```