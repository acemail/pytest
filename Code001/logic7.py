# def cheeseshop(kind, *arguments, **keywords):
#     print('-- do you have any', kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.", 
# "It's really very, VERY runny, sir.",
# shopkeeper="Michael Palin", 
# client="John Cheese", 
# sketch="Cheese shop sketch")


# print('')
# print('-' * 20, "start here", '-' * 20)
# def concat(*args, sep="/"):
#     return sep.join(args)

# print(concat("earth", "mars", "venus"))
# print(concat("earth", "mars", "venus", sep="^"))


print('')
print('-' * 20, "start here", '-' * 20)
print(list(range(3,6)))
args = [3, 10]
print(list(range(*args)))


print('')
print('-' * 20, "start here", '-' * 20)
def parrot(voltage, state='a stiff', action='voom'):
    print("-- this parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


print('')
print('-' * 20, "start here", '-' * 20)
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(5))


print('')
print('-' * 20, "start here", '-' * 20)
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
