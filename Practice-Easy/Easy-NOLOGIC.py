'''
Created on Jun 21, 2013

@author: psgada
'''
import sys



def answer_no_logic():
    num_cases = int(sys.stdin.readline().strip()) 
    
    for i in range(0, num_cases):
        char_list = [0 for i in range(0, 26)]
        while 1:
            chval = sys.stdin.read(1)
            if chval == '\n':
                break

            if chval.islower() or chval.isupper():
                char_list[ord(chval.lower()) - 97] += 1
        
        try:    
            ans_char_index = char_list.index(0)
        except:
            print '~'
            continue
        
        print chr(ans_char_index + 97)
        

answer_no_logic()
