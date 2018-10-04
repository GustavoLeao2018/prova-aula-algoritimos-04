#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercicio 1."""

from pygame import *
from sys import exit

def tela():
    """Cria uma tela."""
    tamanho = largura, altura = (800, 600)

    janela = display.set_mode(tamanho)
    display.set_caption("Exercício 1")

    init()

    while True:
        for evento in event.get():
            if evento.type == QUIT:
                exit()
                
        display.flip()


if __name__ == '__main__':
    tela()
