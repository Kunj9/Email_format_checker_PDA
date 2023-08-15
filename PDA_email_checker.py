""" 
Written by : Kunj Bhatt
"""

import os
from queue import Empty
        
def pdastringcheck(pdastr):
    stack=[]
    state = 1
    print("\nPDA's Starting state: q1")
    #this loop will check the string and prints = state in ehikb char reads, what pop's, and pushes. 
    #Even it will show it in this form (ε, ε --> ε) seperated by '|' from written words.
    for kb in pdastr :
        #starting state checks %  and goes to state 2 read %, pop nothing, push %.
        if state == 1 : 
            if (kb=='%'):
                stack.append('%')
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" "+kb+" "+" | "+
                       "( "+ kb +" , "+"ε --> "+kb +"  )")
                state = 2
            else:
                print("PDA crashes before reaching the end of the input string.")
                print ("String is rejected.")
                break
            # it will check for ( , digit, and dot. if it does not have the given things it will reject
        elif state == 2:
            # if there is '(' then it will stay in state 2. read ( , pop nothing, push )
            if (kb=='('):
                stack.append(')')
                state = 2 
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ) "+" | "+
                      "( "+ kb +" , "+"ε --> ) "+" )")
                continue
                kb +=1
                # if there is digit it will go to state 3. Read digit, pop nothing, push nothing.
            if kb.isdigit():
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+"ε --> ε "+" )")
                state=3
                continue
                kb +=1
                # if there is dot it will go to state 4. Read dot, pop nothing, push nothing. 
            elif kb == '.':
                state = 4 
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                     "( "+ kb +" , "+"ε --> ε "+" )")
            else:
                print("\nPDA crashes before reaching the end of the input string.")
                print ("String is rejected.")
                break
                
        # it will check if the second input is ( or dot. if it does not have the given things it will reject
        elif state == 4:
            # if there is digit it will go to state 5. Read digit, pop nothing, push nothing.
            if kb.isdigit():
                state = 5 
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+"ε --> ε "+" )")
                continue
                kb +=1
            elif (kb == '+' or kb == '-' or kb == '/' or kb == '*'):
                state = 5
           
            else:
                print("\nPDA crashes before reaching the end of the input string.")
                print ("String is rejected.")
                break
                
        # this check digit and has a loot to check digit, if it does not have the given things it will reject
        elif state == 3:
            # if there is digit it will go to state 3. Read digit, pop nothing, push nothing.
            if kb.isdigit():
                state = 3
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+"ε --> ε "+" )")
                continue
                kb +=1
            if kb == '.':
                state = 5  
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+"ε --> ε "+" )")

            else:
                print("\nPDA crashes before reaching the end of the input string.")
                print ("String is rejected.")
                break  
             # checks for operators, digits,  ) , and % . If it does not have the given things it will reject
        elif state == 5:
            # if there is operator it will gp to 2 state. read operator pop nothing push nothing.
            if kb=='+'or kb=='-'or kb=='*'or kb=='/':
                
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+"ε --> ε "+" )")
                state = 2
                continue
                kb+=2
                # if there is digit it will go to state 5. Read digit, pop nothing, push nothing.
            if kb.isdigit():
                state = 5 
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+"ε --> ε "+" )")
                continue
                kb +=1
                # if there is ')' then it will go to state 6 and read ), pop ) push nothing
            if (kb==')'):
                
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ) "+" push "+" ε "+" | "+
                      "( "+ kb +" , "+") --> ε "+" )")
                if(')'in stack):
                     state = 6 
                     stack.pop()
                     continue
                else:
                    print("\nPDA crashes before reaching the end of the input string.")
                    print ("String is rejected.")
                    break
            
                
            if (kb=='%'):     
                if ('%' in stack):  
                    state = 7      # in this it will check if % is in stack then it will go to state 7. 
                    stack.pop()         #  else reject
                
                else:
                    print("\nPDA crashes before reaching the end of the input string.")
                    print ("String is rejected.")
                    break   
               
            else:
                print("\nPDA crashes before reaching the end of the input string.")
                print ("String is rejected.")
                break
                # checks for (, operators,and % then if it gets % goes to state 7 or else reject
        elif state == 6:
           # if kb = ')' then it will go to state 6. read ) pop ) push nothing
            if (kb==')'):
                
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ) "+" push "+" ε "+" | "+
                       "( "+ kb +" , "+") --> ε "+" )")
                if ('(' in stack):
                    state = 6 
                    stack.pop()
                    continue 
                    kb +=1
                if(')' in stack):
                    state = 6 
                    stack.pop()
                    continue 
                    kb +=1
                else:
                    print("\nPDA crashes before reaching the end of the input string.")
                    print ("String is rejected.")
                    break
              #  checks operation if there is any and then goes to state 2
            if kb=='+'or kb=='-'or kb=='*'or kb=='/':
                state = 2
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +" "+" ε "+" push "+" ε "+" | "+
                       "( "+ kb +" , "+"ε --> ε "+" )")
                continue
                kb +=1
                # if there is % it will go to final state 7
            if (kb=='%' ):     
                if ('%' in stack): #in this it will check if % is in stack then it will go to state 7. 
                    state = 7
                    stack.pop()
                
                else:
                    print("\nPDA crashes before reaching the end of the input string.")
                    print ("String is rejected.")
                    break   
                
                    
            else:
                print("\nPDA crashes before reaching the end of the input string.")
                print ("String is rejected.")
                break
           # FINAL STATE IF THE STING REACHES IN THIS IT WILL ACCEPTS
        if state == 7:
          
            if not stack:
                print("In State "+ str(state)+" Read character: " + kb +" "+" pop " +"  "+ kb +"  push "+" ε "+" | "+
                       "( "+ kb +" , "+"% --> ε "+" )")
                print ("String is accepted")
               
         
def main():
    
    print("\nProject 2 for CS 341 \n"+"Section number : 005 \n"+"Semester : Fall 2022\n"+
      "Written by : Kunj Bhatt, kb556\n"+ "Instructor : Marvin Nakayama, marvin@njit.edu\n");

    val = input("Would you like to enter a string? (y/n): \n")
    #loop to keep asking answers
    while True: 
        if(val == 'n'):
            print("\n ")
            break
        elif(val != 'y'):
            val = input("\n"+"Please enter 'y' for Yes or 'n' for No \n")
            continue
        else:
            pdastr = input("Enter a string: ")
            pdastringcheck(pdastr)
            val = input("\n"+"Would you like to enter a string? (y/n): \n")
            continue

main()
