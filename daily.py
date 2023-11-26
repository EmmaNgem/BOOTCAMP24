input_str = raw_input("Please provide some info: ")
if not re.match("^[a-z]*$", input_str):
    print ("Error! Only letters a-z allowed!")
    sys.exit()
    input_str = raw_input("Please provide some info: ")
if not re.match("^[a-z]*$", input_str):
    print ("Error! Only letters a-z allowed!")
    sys.exit()
elif len(input_str) > 15:
    print ("Error! Only 15 characters allowed!")
    sys.exit()

print ("Your input was:", input_str)