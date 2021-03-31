def main():
    string = input("Give a String ")
    string_as_int = input("Give an Integer ")
    string_as_float = input("Give a float ")
    string_as_boolean = input("Give a Boolean ")

    intvalue = int(string_as_int)
    floatvalue = float(string_as_float)
    booleanvalue = bool(string_as_boolean)


    print("You gave the string " + string)
    print("You gave the integer " + str(intvalue))
    print("You gave the float " + str(floatvalue))
    print("You gave the Boolean " + str(booleanvalue))

if __name__ == '__main__':
    main()
