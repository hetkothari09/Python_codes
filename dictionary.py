# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickky

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'Russia':'Moscow',
            'China':'Beijing'}

# print(capitals['India'])
# print(capitals.get('India'))
# print(capitals.get('Germany'))

print(capitals.keys())
print(capitals.values())
print(capitals.items())
print()

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')

for key, value in capitals.items():
    print(key, value)
