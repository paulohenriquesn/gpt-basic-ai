import random

model_training = [
    "the world is so big",
    "big is a word that defines the world",
    "the world is a great place to live",
    "to live in the world you have to be happy"   
]

tokens = {}

for i in range(0, len(model_training)):
    phrase_tokens = model_training[i].split()
    for x in range(0, len(phrase_tokens)):
        tokens[phrase_tokens[x].lower()] = []
       
for i in range(0, len(model_training)):
    phrase_tokens = model_training[i].split()
    for x in range(0, len(phrase_tokens)):
        if (x + 1 < len(phrase_tokens)):
            tokens[phrase_tokens[x].lower()].append(phrase_tokens[x + 1].lower())


print(tokens)

def findNextToken(token):
    if(len(tokens[token]) >= 1):
        return tokens[token][random.randint(0, len(tokens[token]) - 1)]
    else:
        return []


results = []

def promptize(phrase):
    phrase_tokens = phrase.split()
    result = []
    for i in range(0, len(phrase_tokens)):
        next_token = findNextToken(phrase_tokens[i].lower())
        if(next_token == []):
            return
        result.append(next_token)
    
    result_tokens = []
    for x in range(0, len(phrase.split())):
        result_tokens = [w for w in result if w!= phrase.split()[x]]
    
    if(len(result_tokens) == 1):
        results.append(result_tokens[0])
        promptize(result_tokens[0])
    


result = promptize(input('-> '))

result_append_str = ''

for x in range(len(results)):
    result_append_str += results[x] + ' '

print(result_append_str)
