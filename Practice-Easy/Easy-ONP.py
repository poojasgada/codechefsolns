'''
Created on Jul 4, 2013

@author: psgada
'''
import sys
#In this problem, will be using python List as a Stack, peek and pop will be really easy in the list


#The algorithm is simple:
# Maintain a stack - List is used as a stack in python
# Push '(' into the stack and add ')' to the end of infix string
# If the char is a operand, push it into postfix string
# If the char is ')', pop and push the character from stack to the string until a matching '(' is found
# If the char is a '(' push into the stack
# If the char is a operator, until stack top operator precedence is higher or equal to char precedence, 
#    pop and push into postfix string
# Push the char into the stack

def get_priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return -1

def infix_to_postfix(exprss):
    stack = ['(']
    postfix_e = []
    
    for i in range(0, len(exprss)):
        cur_char = exprss[i]
        
        if cur_char == '(':
            stack.append('(')

        elif cur_char.isalpha():
            postfix_e.append(cur_char)
        
        elif cur_char == ')':
            
            while stack and stack[len(stack)-1]!= '(':
                postfix_e.append(stack.pop())
            #Remove the matching open '('
            stack.pop()
        else:
            while get_priority(stack[len(stack)-1]) >= get_priority(cur_char):
                postfix_e.append(stack.pop())
            
            stack.append(cur_char)
    
    while stack and stack[len(stack)-1] != '(':
        postfix_e.append(stack.pop())
        
    return ''.join(postfix_e)

def get_input():
    num_cases = int(sys.stdin.readline().strip())
    
    for i in range(0, num_cases):
        print infix_to_postfix(sys.stdin.readline().strip()+')')
        
get_input()