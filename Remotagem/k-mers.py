# Debug library
from icecream import ic
ic.configureOutput(prefix='Debug| ')
#ic.disable()

# Solve loops in the graph
def solveLoop():
  global DNA
  global k
  # Looking for a possible loop inside the DNA already formed
  for idx, _ in ic(enumerate(DNA)):
    if((idx+(k-1) > len(DNA))):
      exit("Error: No loop found")
    piece = DNA[idx:(idx+(k-1))]
    if((piece in prefixes)):
      lastMer = piece
      nextMer = (prefixes[lastMer].pop(0))
      if(not(prefixes[lastMer])):
        del prefixes[lastMer]
      DNAaux = nextMer[-1]
      lastMer = nextMer
      
      # Building the DNA section that forms the loop
      while((nextMer != piece)):
        if(not(lastMer in prefixes)):
          solveLoop()
        nextMer = prefixes[lastMer].pop(0)
        if(not(prefixes[lastMer])):
          del prefixes[lastMer]
        DNAaux = DNAaux + nextMer[-1]
        lastMer = nextMer
      
      # Inserting the new loop section in the DNA already formed
      DNA = DNA[:(idx+(k-1))] + DNAaux + DNA[(idx+(k-1)):]

      break
    else:
      exit("Error: No loop found")


# Opening file
with open('input-50.txt') as f:
  content = f.read()

k = 50

# Creating an array with all the mers
aux1 = ""
mers = []
for i in content:
  if (i == ','):
    mers.append(aux1)
    aux1 = ""
    continue
  aux1 = aux1 + i


# Tamanho do mers


# The dicts to be used
prefixes = {}
count = {}


# Looping to create the prefix dict and check what is the first prefix and last suffix
for i in mers:
  prefix = i[0:(len(i)-1)]
  suffix = i[1:]

  # Check if the key does not exist, if not creates it
  if(not((prefixes.get(prefix,False)))):
    prefixes[prefix] = []
  if(not((count.get(prefix,False)))):
    count[prefix] = 0
  if(not((count.get(suffix,False)))):
    count[suffix] = 0

  prefixes[prefix].append(suffix)
  count[prefix] += 1
  count[suffix] -= 1
    

# Defining what is the first prefix and last suffix inside sandf
keysList = count.keys()
'''start and finish'''
sandf = ["",""]
for i in keysList:
  if(count[i] == 1):
    sandf[0] = i
  if(count[i] == -1):
    sandf[1] = i


# Build the DNA using the prefixes knowing the first and last mer
nextMer = prefixes[sandf[0]].pop(0)
if(not(prefixes[sandf[0]])):
  del prefixes[sandf[0]]
DNA = sandf[0][0] + nextMer
lastMer = nextMer

while(prefixes):
  #ic(DNA)
  if(not(lastMer in prefixes)):
    solveLoop()
    break
  nextMer = prefixes[lastMer].pop(0)
  if(not(prefixes[lastMer])):
    del prefixes[lastMer]
  DNA = DNA + nextMer[-1]
  lastMer = nextMer


# Write rebuild DNA on 'output.txt' file
arquivo = open('output.txt','w')
arquivo.write(DNA + '\n')
arquivo.close()  

#ic(DNA)