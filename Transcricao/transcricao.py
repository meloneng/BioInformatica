dna = input()

transcricao = ""
for i in dna:
        if i == 'A': 
            transcricao += 'U'
        if i == 'T':
            transcricao += 'A'
        if i == 'G':
            transcricao += 'C'
        if i == 'C':
            transcricao += 'G'

print(transcricao)
