#!/usr/bin/eny python
# -*- coding:utf-8 -*-

import hashlib

def md5():
	parola = hashlib.md5(metin.encode()).hexdigest()
	print "Şifrenen metin : " + parola

def sha1():
	parola = hashlib.sha1(metin.encode()).hexdigest()
	print "Şifrenen metin : " + parola

def sha224():
	parola = hashlib.sha224(metin.encode()).hexdigest()
	print "Şifrenen metin : " + parola

def sha256():
	parola = hashlib.sha256(metin.encode()).hexdigest()
	print "Şifrenen metin : " + parola

def sha384():
	parola = hashlib.sha384(metin.encode()).hexdigest()
	print "Şifrenen metin : " + parola

def sha512():
	parola = hashlib.sha512(metin.encode()).hexdigest()
	print "Şifrenen metin : " + parola


textencoding_ico = """
#########################################################
#         PYTHON - TEXT ENCODING - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print textencoding_ico

metin = raw_input("Şifrelenecek metini giriniz : ")

sifreleme_turleri = """
(1) MD5
(2) SHA-1
(3) SHA-224
(4) SHA-256
(5) SHA-384
(6) SHA-512
"""

print sifreleme_turleri

islem = input("Şifreleme türünü belirleyiniz : ")

if islem == 1:
	md5()

if islem == 2:
	sha1()

if islem == 3:
	sha224()

if islem == 4:
	sha256()

if islem == 5:
	sha384()

if islem == 6:
	sha512()
