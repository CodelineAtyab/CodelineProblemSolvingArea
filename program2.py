def conversionfunc(numb):
    if numb < 0:
        print("Please enter a positive decimal number.")
        quit()
        #incase of incorrect input
    if numb == 0:
        return 0
    bin = ""
    while numb >= 1:
        bin = str(numb % 2) + bin
        numb = numb // 2
    return bin


decnumb = int(input("Input: "))
binnumb = conversionfunc(decnumb)
print("Output:" ,binnumb)

#code does not handle decimals like 2.5, as it was not shown in the examples