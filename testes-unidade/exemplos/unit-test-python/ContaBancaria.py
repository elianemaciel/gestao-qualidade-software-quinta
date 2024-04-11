#!/usr/bin/python
# -*- coding: utf8 -*-

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print('Saque de R${valor:.2f} realizado com sucesso.'.format(
                valor=valor))
        elif valor <= 0:
            print('O valor do saque deve ser maior que zero.')
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo disponível: R${self.saldo:.2f}')
