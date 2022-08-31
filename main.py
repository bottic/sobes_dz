from classes import Stack

fixture_opens = '([{'
fixture_closerss = ')]}'


def isbalansed(info: str):
    stack = Stack()
    index = 0
    end = False
    while index < len(info) and end == False:
        element = info[index]
        if element in fixture_opens:
            stack.push(element)
        elif stack.isEmpty():
            end = True
        else:
            open = stack.pop()
            if not fixture_opens.index(open) == fixture_closerss.index(element):
                end = True
        index += 1
    if end == False and stack.isEmpty() == True:
        return 'balansed'
    else:
        return 'not balansed'


print(isbalansed('[([])((([[[]]])))]{()}'))
