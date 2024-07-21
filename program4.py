def listfunc(startindx, endindx, numbs):
    startindx=int(startindx)
    endindx=int(endindx)
    #new even list
    evensqrs=[]
    for i in numbs:
        if i % 2 == 0:
            evensqrs.append(i**2)
    #slice
    sublist=numbs[startindx:endindx]

    return evensqrs, sublist

print("Welcome to the program. ")
print("Enter the list of integers, seperated by spaces. ")
print("For example: 1 2 3 ")
numbs = list(map(int, input("Enter a list of integers: ").split()))
#print list to get desired output
print(f'[{",".join(map(str, numbs))}]')

startindx=input("Enter start index: ")
endindx=input("Enter end index: ")

evensqrs, sublist = listfunc(startindx,endindx,numbs)
print("List of squares of even numbers: ",evensqrs)
print("Sublist: ", sublist)
