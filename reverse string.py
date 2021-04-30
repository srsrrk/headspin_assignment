# reverse.string
string=input(" enter a string with dots as separater : ")
words = string.split(".")
words = list(reversed(words))
print(".".join(words))
