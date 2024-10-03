import tkinter as tk
from tkinter import messagebox


#estados
S = {'s0': 0.00, 's1': 0.25, 's2': 0.50, 's3': 0.75, 's4': 1.00, 's5': 1.25, 's6': 1.50, 's7': 1.75, 's8': 2.00}

#entradas
I = {'m25': 0.25, 'm50': 0.50, 'm100': 1.00, 'b': 'botao'}

#saidas
O = {'t25': 0.25, 't50': 0.50, 't75': 0.75, 't100':1.00, 'r': 'refrigerante', 'n': None}

#transicoes
T = {

    #s0
    ('s0', 'b'): ('s0', 'n'),
    ('s0', 'm25'): ('s1', 'n'),
    ('s0', 'm50'): ('s2', 'n'),
    ('s0', 'm100'): ('s4', 'n'),

    #s1
    ('s1', 'b'): ('s1', 'n'),
    ('s1', 'm25'): ('s2', 'n'),
    ('s1', 'm50'): ('s3', 'n'),
    ('s1', 'm100'): ('s5', 'n'),

    #s2
    ('s2', 'b'): ('s2', 'n'),
    ('s2', 'm25'): ('s3', 'n'),
    ('s2', 'm50'): ('s4', 'n'),
    ('s2', 'm100'): ('s6', 'n'),

    #s3
    ('s3', 'b'): ('s3', 'n'),
    ('s3', 'm25'): ('s4', 'n'),
    ('s3', 'm50'): ('s5', 'n'),
    ('s3', 'm100'): ('s7', 'n'),

    #s4
    ('s4', 'b'): ('s4', 'n'),
    ('s4', 'm25'): ('s5', 'n'),
    ('s4', 'm50'): ('s6', 'n'),
    ('s4', 'm100'): ('s8', 'n'),

    #s5
    ('s5', 'b'): ('s5', 'n'),
    ('s5', 'm25'): ('s6', 'n'),
    ('s5', 'm50'): ('s7', 'n'),
    ('s5', 'm100'): ('s8', 't25'),

    #s6
    ('s6', 'b'): ('s6', 'n'),
    ('s6', 'm25'): ('s7', 'n'),
    ('s6', 'm50'): ('s8', 'n'),
    ('s6', 'm100'): ('s8', 't50'),

    #s7
    ('s7', 'b'): ('s7', 'n'),
    ('s7', 'm25'): ('s8', 'n'),
    ('s7', 'm50'): ('s8', 't25'),
    ('s7', 'm100'): ('s8', 't75'),

    #s8
    ('s8', 'b'): ('s0', 'r'),
    ('s8', 'm25'): ('s8', 't25'),
    ('s8', 'm50'): ('s8', 't50'),
    ('s8', 'm100'): ('s8', 't100')
}

#funcao de transicao
def transicao (estado_atual, input_simbolo):
    try:
        proximo_estado, output = T[(estado_atual, input_simbolo)]
        return proximo_estado, output
    except KeyError:
        return estado_atual, None

#funcao para atualizar a interface 
def atualiza_estado (input_simbolo):
    global estado_atual
    proximo_estado, output = transicao(estado_atual, input_simbolo)
    estado_atual = proximo_estado
    estado_label.config(text=f"Estado atual: {estado_atual}")
    output_label.config(text=f"Saída:  {output if output else 'Nenhuma saída'}")

#funcao chamada ao pressionar o botao
def botao_pressionado():
    atualiza_estado('b')

#funcao chamada ao inserir uma moeda
def inserir_moeda(moeda):
    atualiza_estado(moeda)

#inicializacao da interface
estado_atual = 's0'

root = tk.Tk()
root.title("Máquina de Vendas")

estado_label = tk.Label(root, text=f"Estado atual: {estado_atual}", font=("Arial", 16))
estado_label.pack(pady=10)

output_label = tk.Label(root, text=f"Saída: Nenhuma saída", font=("Arial", 16))
output_label.pack(pady=10)

btn_m25 = tk.Button(root, text="Inserir R$0,25", command=lambda: inserir_moeda('m25'), width=15)
btn_m25.pack(pady=5)

btn_m50 = tk.Button(root, text="Inserir R$0,50", command=lambda: inserir_moeda('m50'), width=15)
btn_m50.pack(pady=5)

btn_m100 = tk.Button(root, text="Inserir R$1,00", command=lambda: inserir_moeda('m100'), width=15)
btn_m100.pack(pady=5)

btn_press = tk.Button(root, text="Pressionar Botão", command=botao_pressionado, width=15)
btn_press.pack(pady=5)

# Inicia o loop da interface
root.mainloop()