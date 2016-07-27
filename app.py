#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Autor: Gustavo Fernandes dos Santos
# Email: gfdsantos@inf.ufpel.edu.br

import sys
import subprocess

info_str    = '[info]    '
warning_str = '[warning] '
status_str  = '[status]  '

# Function that print info from developer
def print_dev_info():
	print('{}Author: Gustavo Santos'.format(info_str))
	print('{}E-mail: gfdsantos@inf.ufpel.edu.br'.format(info_str))
	print('{}This program was developed for fun,'.format(warning_str))
	print('          don\'t use for serious things.')



def download_links(path):
	file = open(path, 'r')
	links = file.readlines()
	print("{}Downloading {} links".format(info_str, len(links)))

	for link in links:
		flag = subprocess.call(['youtube-dl', link, '-x','--audio-format', 'mp3', '--audio-quality', '0', '--embed-thumbnail', '--add-metadata'])
		print("{}{}".format(status_str, flag))



# Get file that contains all links to download
def main():
	print_dev_info()
	args = sys.argv
	if len(args) == 2:
		# check if ffmpeg and youtube-dl is installed
		res = subprocess.call(['which', 'youtube-dl'])
		if res == 0:
			res = subprocess.call(['which', 'ffmpeg'])
			if res == 0:
				download_links(args[1])
			else:
				print('[error] FFMPEG isn\'t installed')
				print('        install it using: sudo apt-get install ffmpeg')
		else:
			print('[error] Youtube-dl isn\'t installed')
			print('        install it using: sudo apt-get install youtube-dl')



if __name__ == '__main__':
	main()