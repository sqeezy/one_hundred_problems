def read_lines_till_end_and_reverse():
    result = []
    go = True
    current = ""
    print "To cancel enter END"
    while go:
        current = raw_input("Enter text: ")
        if current == "END":
            go = False
        else:
            result.append(current)
    result.reverse()
    return result

def print_list(list):
    for elem in list:
        print elem

if __name__ == '__main__':
    print_list(read_lines_till_end_and_reverse())