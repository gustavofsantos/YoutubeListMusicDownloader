#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Autor: Gustavo Fernandes dos Santos
# Email: gfdsantos@inf.ufpel.edu.br
import os

def main():
	arquivos = os.listdir()
	musicas = []
	for arquivo in arquivos:
		if str(arquivo[(len(arquivo)) - 4:len(arquivo)]) == '.mp3':
			musicas.append(arquivo)

	print('[!] Serão renomeadas {} musicas'.format(len(musicas)))

	for musica in musicas:
		novo_nome = musica[0:len(musica) - 4 - 12] + '.mp3'
		os.rename(musica, novo_nome)


if __name__ == '__main__':
	main()