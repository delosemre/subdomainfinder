#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################
#                        #
#Emre Yılmaz (delosemre) #
# 	   emreylmz.com      #
# 	  kernelblog.org     #
##########################

import requests
import os,sys
import signal


def sigint_handler(signum, frame):
    print ("\n CTRL+C detected!")
    print(" \033[1;91m@Good bye\033[1;m")
    sys.exit() 
 
signal.signal(signal.SIGINT, sigint_handler)


def domain_scanner(domain_name,sub_domnames):

	print("""\033[1;91m
	
 (                                            (                            
 )\ )        )   (                            )\ )           (             
(()/(  (  ( /(   )\ )       )      ) (       (()/( (         )\ )  (  (    
 /(_))))\ )\()) (()/( (    (    ( /( )\  (    /(_)))\  (    (()/( ))\ )(   
(_)) /((_|(_)\   ((_)))\   )\  ')(_)|(_) )\ )(_))_((_) )\ )  ((_))((_|()\  
/ __(_))(| |(_)  _| |((_)_((_))((_)_ (_)_(_/(| |_  (_)_(_/(  _| (_))  ((_) 
\__ \ || | '_ \/ _` / _ \ '  \() _` || | ' \)) __| | | ' \)) _` / -_)| '_| 
|___/\_,_|_.__/\__,_\___/_|_|_|\__,_||_|_||_||_|   |_|_||_|\__,_\___||_|   
Emre Yılmaz (delosemre) - Subdomain Finder | github.com/delosemre | V1
	\033[1;m """)

	for subdomain in sub_domnames:

		url = f"https://{subdomain}.{domain_name}"

		try:
			requests.get(url)
			cikti = str(f'[+] {url}')
			print(cikti)
			f = open(domain_name+"_subdomain"+".txt", "a")
			f.write(cikti + "\n")
			f.close()


		except requests.ConnectionError:	
			pass
	
	print("\n \033[1;91m your output file is in your current directory \033[1;m")
	os.system("pwd")
	print(" \033[1;91m Your current directory \033[1;m")


if __name__ == '__main__':
	
	dom_name = input("Enter the Domain Name: ")
	sub_list = input("Enter the Sub-List (leave blank for default): ")
	if not sub_list:
		with open('sublist.txt','r') as file:
			name = file.read()
			sub_dom = name.splitlines()
	else:
		with open(sub_list,'r') as file:
			name = file.read()
			sub_dom = name.splitlines()
	domain_scanner(dom_name,sub_dom)

