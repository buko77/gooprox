#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ce script permet de générer une liste de proxy qui comprend :
# Adresse IP (https ou non)
# Port
# Pays
# Fournisseur d'anonymat
# Dernier update
# Les proxy viennent du site : http://google-proxy.net
# Une option permet de ne selectionner que les proxy HTTPS.

# SCRIPT MADE BY BUKO	
# VERSION 1.0
# bukowski@openmailbox.org

from BeautifulSoup import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description="Liste les proxys provenant de http://google-proxy.net")
parser.add_argument('-s', '--secure', help="""Permet de lister uniquement les proxys HTTPS.""", required=False, action='store_true')
args = parser.parse_args()

url = 'http://google-proxy.net'

r = requests.get(url)

soup = BeautifulSoup(r.text)
table = soup.find('tbody')
ip_info = table.findAll('tr')

def https():
	for i in ip_info:
		ip_net = i.findAll('td')
		if ip_net[6].text == 'yes':
			print 'Adresse IP HTTPS :', ip_net[0].text
			print 'Port :', ip_net[1].text
			print 'Pays :', ip_net[3].text
			print 'Anonymat :', ip_net[4].text
			print 'Dernier update :', ip_net[7].text
			print '-'*len(ip_net[7].text)+('-'*16)
def main():
	if args.secure is True:
		https()
	else:
		for i in ip_info:
			ip_net = i.findAll('td')
			print 'Adresse IP :', ip_net[0].text
			print 'Port :', ip_net[1].text
			print 'Pays :', ip_net[3].text
			print 'Anonymat :', ip_net[4].text
			print 'Dernier update :', ip_net[7].text
			print '-'*len(ip_net[7].text)+('-'*16)

if __name__== '__main__':
	main()
