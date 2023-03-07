# Debug library
from icecream import ic
ic.configureOutput(prefix='Debug| ')
#ic.disable()

# Opening file
with open('input-25.txt') as f:
  content = f.read()

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
k = 25

# The dicts to be used
prefixes = {}
#prefixCount = {}
#suffixCount = {}
count = {}

# Looping to create the prefix dict and check what is the first prefix and last suffix
for i in mers:
  prefix = i[0:(len(i)-1)]
  suffix = i[1:]

  # Check if the key does not exist, if not creates it
  '''
  if(not((prefixes.get(prefix,False)))):
    prefixes[prefix] = []
  if(not((prefixCount.get(prefix,False)))):
    prefixCount[prefix] = 0
  if(not((suffixCount.get(suffix,False)))):
    suffixCount[suffix] = 0

  prefixes[prefix].append(suffix)
  prefixCount[prefix] += 1
  suffixCount[suffix] += 1
  '''
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
DNA = nextMer
lastMer = nextMer

while(prefixes):
  nextMer = prefixes[lastMer].pop(0)
  if(not(prefixes[lastMer])):
    del prefixes[lastMer]
  DNA = DNA + nextMer[-1]
  lastMer = nextMer


arquivo = open('output.txt','w')
arquivo.write(DNA + '\n')
arquivo.close()  