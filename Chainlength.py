#program to check which among the chains have more number of residues
from Bio.PDB.PDBParser import PDBParser
parser = PDBParser()
structure = parser.get_structure("test", "3k8x.pdb")
model = structure[0]
number_chains = (len(model))#find & printthe number of chains in model taken 
print("number of chains in the model is=",number_chains)
#the purpose of function given below is to convert index of chains in numbers
#to alphabets such that it can be used as chain id later
def getting_id(i):
  alphabets= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
  id= alphabets[i]
  return (id)
#for loop will limit the procedure within the number of chains
for i in range (-1,number_chains-1):
    i= i+1
    name = getting_id(i)
    print("chain:",name)
    chain= model[name]
    #print(chain)
    print("length of the chain is", len(chain))


    
     
     
    