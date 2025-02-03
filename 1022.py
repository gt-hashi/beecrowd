# -*- coding: utf-8 -*-

import math
    

def gcd(x, y): #ユークリッドの互除法
    while(y):
       x, y = y, x % y
    return abs(x)
        
def main():
    temp = int(input())
    
    while True:
        try:
            expression = input()
            if not expression:
                break
            A, ign1, B, op, C, ign2, D = expression.split()
            A, B, C, D = int(A), int(B), int(C), int(D)
            
            if op == '+':
                E, F = A * D + C * B, B * D
            elif op == '-':
                E, F = A * D - C * B, B * D
            elif op == '*':
                E, F = A * C, B * D
            elif op == '/':
                E, F = A * D, B * C
            else:
                continue
            
            GCD = gcd(abs(E), abs(F))
            G, H = E // GCD, F // GCD
            
            if H < 0:
                G, H = -G, -H
            
            print(f"{E}/{F} = {G}/{H}")
        except EOFError:
            break
        except ValueError:
            break

if __name__ == "__main__":
    main()
    
    