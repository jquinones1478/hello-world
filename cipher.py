#!/usr/bin/python3

#This code encode a phrase into a password using the ceasar cipher.

#import re

secret_code = input('enter the phrase: ')
key = int(input('Enter the number for the key: '))
encode = list(secret_code)

new_encode = []
for i in encode:
    new_encode.append(ord(i))

#print(new_encode)

cipher_encode = []
for i in new_encode:
    cipher_encode.append(i + key)

#print(cipher_encode)

decode = []
for i in cipher_encode:
    decode.append(chr(i))
#print(decode)

decode = ''.join(decode)

#decode_wo_special_char = re.sub(r'@|\'*$%#!&()[]{}', "", decode)


print('\nNew password created: ' + decode)

print('\n')
