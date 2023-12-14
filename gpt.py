import random

#Modelos de treinamento

'''
model_training = [
    "ola tudo bem",
    "ola tudo legal com vc",
    "vc esta bem?",
    "ola boa noite",
    "boa noite pra todos",
    "bom dia galera tudo bem",
    "estar bem é sempre otimo estar ok",
    "tudo otimo com vc"
]
'''

tokens = {}

#Função que irá tokenizar as frases usando unigram
for i in range(0, len(model_training)):
    phrase_tokens = model_training[i].split()
    for x in range(0, len(phrase_tokens)):
        tokens[phrase_tokens[x].lower()] = [] 
    
#Função que irá tokenizar a proxima possibilidade de um token
for i in range(0, len(model_training)):
    phrase_tokens = model_training[i].split()
    for x in range(0, len(phrase_tokens)):
        if (x + 1 < len(phrase_tokens)):
            if phrase_tokens[x + 1].lower() not in tokens[phrase_tokens[x]]:
                tokens[phrase_tokens[x].lower()].append(phrase_tokens[x + 1].lower())

print("\n"*4)

print(tokens)

print("\n"*4)

#Função que irá pegar o proximo token de um determinado token
# ola [ mundo, tudo bem, como vai ]

def findNextToken(token):
    if(len(tokens[token]) >= 1):
        return tokens[token][random.randint(0, len(tokens[token]) - 1)]
    else:
        return []


results = []

#Função que irá promptizar minha frase fazendo ela sempre obter o proximo token 
# e gerando um contexto
# ola [ mundo, tudo bem, como vai ]
# ola tudo bem [ com voce, contigo ]
# ola tudo bem contigo [ consegue me ajudar, consegue me dar uma resposta ]


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
results_formatted = []

# Pega todo o contexto e gera o resultado

for x in range(len(results)):
    if results[x] not in results_formatted:
        results_formatted.append(results[x])
    elif len(results[x]) <= 3:
        results_formatted.append(results[x])

for x in range(len(results_formatted)):
    result_append_str += results_formatted[x] + " "

print(result_append_str) #Output
