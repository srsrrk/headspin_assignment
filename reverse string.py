# reverse.string
string=input(" enter a string with dots as separator : ")
words = string.split(".")
words = list(reversed(words))
print(".".join(words))
