#T1 - Cache com Mapeamento Direto - Bruno Pires e Pedro Felix.

class IO:
    def output(self, s):
        print(s, end='')

    def input(self, prompt):
        return input(prompt)



class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender


class RAM:
    def __init__(self, k):
        self.tamanho = 2**k
        self.memoria = [0] * self.tamanho

    def verifica_endereco(self, ender):
        if (ender < 0) or (ender >= self.tamanho):
            raise EnderecoInvalido(ender)

    def capacidade(self):
        return self.tamanho

    def read(self, ender):
        self.verifica_endereco(ender)
        return self.memoria[ender]

    def write(self, ender, val):
        self.verifica_endereco(ender)
        self.memoria[ender] = val


class CPU:
    def __init__(self, mem,cache, io):
        self.mem = mem
        self.io = io
        self.PC = 0                   
        self.A = self.B = self.C = 0   
        
        self.cache = cache

    def run(self, ender):
        self.PC = ender
       
        self.A = self.mem.read(self.PC)
        self.PC += 1
        self.B = self.mem.read(self.PC)
        self.PC += 1

        self.C = 1
        while self.A <= self.B:
            self.mem.write(self.A, self.C)
            self.io.output(f"{self.A} -> {self.C}\n")
            self.C += 1
            self.A += 1 

class Cache:
    def __init__(self,size_total, size_line, ram_total):
        self.size_line = 2 ** size_line 
        self.size_total = 2 ** size_total 
        self.ram_total = ram_total 
try:
    io = IO()
    ram = RAM(12)   
    cache = Cache(7, 4, ram) 
    cpu = CPU(ram,cache, io)

    question = int(input("Escolha a quantidade de informacoes de endereco que deseja adicionar : "))
    list = []

    for i in range(0,question,1):
        answer = input(f"Digite a informacao {i}: ")

        list.append(answer)
        ram.write(i, list[i])
        cpu.run(i) # FAZER A FUNCAO 

    search_ender = input(" Digite o endereco que deseja buscar : ")
    search_num = input(" Digite o numero que deseja buscar : ")
    

except EnderecoInvalido as e:
    print("Endereco inválido:", e.ender)
