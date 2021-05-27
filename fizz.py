def main():
    print_things()

def print_things():
    list = []
    for i in range (1,100):
        temp = str(i)
        list.append(temp)
    print(list)
    return list

if __name__ == '__main__':
    main()