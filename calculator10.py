from replit import clear
logo ="""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
"""

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
symbol={"+":add,"-":sub,"*":mul,"/":div}
    
def calculator_10():
    print(logo)
    n1=float(input("Enter your 1st num: "))
    for i in symbol:
        print(i)
    run=True
    while run==True:
        op=input("Enter your operator: ")
        n2=float(input("What's the next number?: "))
        op2=symbol[op]
        answer=op2(n1,n2)
        print(f"{n1}{op}{n2}={answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")=="y":
            n1=answer
        else:
            clear()
            run=False
            calculator_10
calculator_10()
