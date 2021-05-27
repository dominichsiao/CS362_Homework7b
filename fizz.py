def main():
    print_things()

def print_things():
    list = []
    for i in range (1,100):
        temp = str(i)
        list.append(temp)
        if(i % 3 == 0):
            #print("Fizz", end = '')
            #print(" ", end = '')
            list.append("Fizz")
        if(i % 5 == 0):
            #print("Buzz", end = '')
            #print(" ", end = '')
            list.append("Buzz")
        if(i % 3 == 0):
            if(i % 5 == 0):
                #print("FizzBuzz", end = '')
                #print(" ", end = '')
                list.append("FizzBuzz")
    print(list)
    return list

if __name__ == '__main__':
    main()