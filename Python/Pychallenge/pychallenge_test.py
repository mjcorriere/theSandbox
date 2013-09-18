# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:02:26 2013

@author: NotMark
"""


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def replace(char):

    if char in alphabet:
        i = alphabet.index(char)
        return alphabet[(i + 2) % 26]
        
    else:
        return char
    

phrase = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc ' \
            + 'dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq' \
            + 'rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu' \
            + ' ynnjw ml rfc spj.'
         
phrase2 = 'map'

print ''.join(map(replace, phrase))

