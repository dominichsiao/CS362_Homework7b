def main():
    a = input("Please type a year ")
    check_year(a)
    return

def check_year(a):

    a = int(a)
    #print(a)
    if (a % 4 == 0):
        b = 1
    else:
        b = 0

    if (b == 1):
        return(str(a) + " is a leap year")
    else:
        return(str(a) + " is not a leap year")


if __name__ == "__main__":
    main()
