import tokenize
reader = open("endless_func.py").readline
print(reader)
print(type(reader))
tokens = tokenize.generate_tokens(reader)
#tokens is a generator.
print(tokens)
print(next(tokens))
print(next(tokens))
print(next(tokens))




