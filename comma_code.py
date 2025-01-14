myList = ['apples', 'bananas', 'tofu', 'cats']
myList = []
myList = [1, 2, 3, 4, 5]

def commaCode(list):

    if len(list) == 0:
        return 'No items in your list!'

    output = ''

    for item in list:
        if item == list[-1]:
            output += 'and ' + str(item)
            return output

        output += str(item) + ', '
    
print(commaCode(myList))