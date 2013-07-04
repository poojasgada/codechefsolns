'''
Created on Jul 3, 2013

@author: psgada
'''
'''
A tourist is visiting Byteland. The tourist knows English very well. The language of Byteland is rather 
different from English. To be exact it differs in following points:

    Bytelandian alphabet has the same letters as English one, but possibly different in meaning. Like 'A' in 
    Bytelandian may be 'M' in English. However this does not mean that 'M' in Bytelandian must be 'A' in English.
     More formally, Bytelindian alphabet is a permutation of English alphabet. It will be given to you and could 
     be any possible permutation. Don't assume any other condition.
    People of Byteland don't like to use invisible character for separating words. Hence instead of space (' ') 
    they use underscore ('_'). Other punctuation symbols, like '?', '!' remain the same as in English.
'''

import sys
def trans_bytelandia_english():
    
    num_trans, translator = sys.stdin.readline().strip().split()
    
    eng_dict = {}
    ascii_i = 97
    
    for i in range(0, 26):
        eng_dict[str(unichr(ascii_i))] = translator[i]
        ascii_i += 1
    
    for i in range(0, int(num_trans)):
        bytelandia_s = sys.stdin.readline().strip()

        english_s = []
        
        for j in range(0, len(bytelandia_s)):
            cur_char = bytelandia_s[j]
            
            if cur_char.isalpha():
                if cur_char.isupper():
                    byte_char = eng_dict[cur_char.lower()].upper()
                else:
                    byte_char = eng_dict[cur_char]
            elif cur_char == '_':
                byte_char = ' '
            else:
                byte_char = cur_char    
                
            english_s.append(byte_char)
            
        print ''.join(english_s)
    
trans_bytelandia_english()
