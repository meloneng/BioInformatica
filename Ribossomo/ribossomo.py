def ribossomo(fita):
    start = ["AUG"]
    stop = ["UAA","UAG","UGA"]
    translation = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 
        'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 
        'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST', 
        'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W', 
        'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
        'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
        'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
        'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
        'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
        'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
        'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
        }

    matriz = []
    aux = ''
    flagStart = False
    for i in range(0,len(fita),3):
        codon = fita[i:i+3]
        
        if codon in start[0]:
            flagStart = True
            aux+=translation[codon]
        elif codon in stop:
            flagStart = False
            aux+=translation[codon]
            matriz.append(aux)
            aux = ''
        elif flagStart:
            aux+=translation[codon]     
    return matriz


arquivo = open('Gabriel Sousa.txt','w')
proteina = ribossomo('AUGCCUUACCGCGUGACGAGUAUUAAACCCGCGCGAGCGCAUCCGAUACAUACGGUAAGUAGUUAG')

for aminoAcido in proteina:
    arquivo.write(aminoAcido+'\n')
arquivo.close()