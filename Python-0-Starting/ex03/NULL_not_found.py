def NULL_not_found(object: any) -> int:
    if object == None:
        print(f'Nothing: {object} {type(object)}')
    # Nan은 자기 자신과 항상 다름. Nan == Nan의 값은 false
    elif type(object) == float and object != object:
        print(f'Cheese: {object} {type(object)}')
    elif type(object) == int and object == 0:
        print(f'Zero: {object} {type(object)}')
    elif type(object) == str and object == "":
        print(f'Empty: {object} {type(object)}')
    elif type(object) == bool and object == False:
        print(f'Empty: {object} {type(object)}')
    else:
        print('Type not Found')
        return 1
    return 0
