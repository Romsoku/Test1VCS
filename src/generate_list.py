import random

def generate_list():
    cantgo = 1
    alist = [x for x in range(random.randint(-10, 10))]
    assert (alist != []),"alist in Null"
    sum = 0
    for i in alist:
        sum += alist[i]
        
    assert sum >= -100, "Sum of alist is lower than -100"
        
    return alist
    
    """
    print a generate list
    """
    
def printIt():
    print(generate_list())
    
def main():
    printIt()
    
    """
    Tf this script file is called, it will run main() directly
    """
    
if __name__=='__main__':
    for i in range(1000):
        print("Test print():")
        main()
