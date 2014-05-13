import sys

usage = "usage: python factorial.py (int)[n]"

def factorial(n):
    if n<0:
        raise ValueError("There is no factorial for negativ numbers.")
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

def check_argv():
    if len(sys.argv)==2:
        return True
    else:
        sys.exit(usage)

def demonstrate_argv():
    print str(sys.argv) + " is complete argv"
    print str(len(sys.argv)) + " is length of argv"

if __name__ == '__main__':
    demonstrate_argv()
    if check_argv():
        n = int(sys.argv[1])
        print str(sys.argv[1])+"! = "+str(factorial(n))