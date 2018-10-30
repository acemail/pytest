def my_function():
    """Do nothing, but document it. 

    no, really. it doesn't do anything.
    """
    pass

print(my_function.__doc__)

print('')
print('-' * 20, "start here", '-' * 20)
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam', 'telur')