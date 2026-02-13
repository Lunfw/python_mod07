from os import listdir


__all__: list = []


for i in listdir():
    if i.endswith('.py'):
        __all__.append(i[:-3])


print(__all__)
