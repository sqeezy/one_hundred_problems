import sys

usage = "usage: python min_and_max.py int(argv*)"
numbers = []

if len(sys.argv) < 2:
    sys.exit(usage)

for i in range(1,len(sys.argv)):
    try:
        numbers.append(int(sys.argv[i]))
    except ValueError:
        exit_string = "{} is not a valid number.".format(sys.argv[i])
        sys.exit(exit_string)

numbers.sort()
print "Read {} number.".format(len(numbers))
print "Max: {}".format(numbers[-1])
print "Min: {}".format(numbers[0])
