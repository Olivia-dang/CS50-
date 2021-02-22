from cs50 import get_int

def main ():
    i = get_positive_interger()
    print(i)
    
def get_positive_interger():
    while True:
        n = get_int("Positive Interger: ")
        if n>0:
            break
    return n
    
main()
