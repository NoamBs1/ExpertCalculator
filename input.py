def getStr() -> str:
    """
    gets a string from the user
    :return: the string without white spaces
    :raises: EOFError if the user insert EOF
    """
    try:
        UserInput = input("enter an algebraic expression: ")
        UserInput = UserInput.replace(' ', '').replace('\t', '')
    except EOFError:
        raise EOFError("goodbye!")
    except KeyboardInterrupt:
        raise KeyboardInterrupt("goodbye!")
    else:
        return UserInput
