#iterators is an object on which you can traverse upon
#list tuple dictonaries are iterable objects
newtuple = (10,20,30)
myiter = iter(newtuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

newstr = 'python'
newiter = iter(newstr)
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))