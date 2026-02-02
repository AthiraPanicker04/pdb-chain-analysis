""" -----------PROGRAM TO FIND GC CONTENT FROM .fasta FILES AND CREATE BOXPLOT. --------"""

""" ***********Developed by Athira P Anil**********"""

'''Biopython package should be installed'''

'''                         Biopython Installation Commands

                1.     python.exe -m pip install --upgrade pip     (For Installing pip)
                2.     pip install biopython                       (For Installing Biopython)
                                                                                                    '''
'''NOTE=====> This python script file and fasta file must be keep in same directory and should be connected to internet'''


from Bio.SeqUtils import GC                                           # Uploading GC function from Bio.SeqUtils by taking from Biopython package
lis=[]                                                                # An empty list for storing GC content of each species which can be used as data for plot creation
name=input("Enter the Species name:")                                 # User can enter a single species name
n= int(input("Enter the number of sequence files:"))                  # Give the number of sequence files for the specific species, it can be any integer value
for i in range(0,n):                                                  # Looping code following to find GC  content for n number of files, where n is the number of sequence files
   file_name = input("Enter your fasta file in .fasta format: ")       # User input for taking a fasta file
   sequence = ""                                                       # Creating an empty string for removing newline character between the sequences from fasta file_name

   try:                                                                # try keyword for any Exception
       with open(file_name,'r') as file_open:                          # opening fasta file
           file_read = file_open.readlines()[1:]                       # reading data from fasta file
           for i in file_read:
                sequence = sequence + i.strip('\n')
           gc = GC(sequence)                                           # GC() for calculation of gc content
           print()
           print("The GC content of file: ",file_name, "is",round(gc,3),"%") # round() for round figure of any number with 3 decimal places
           lis.append(gc)                                              # Appending the list with GC content from each cycle of the loop
   except FileNotFoundError as message:
       print()
       print(message)
print(lis)                                                       # Not neccessary
"To plot the GC content of a species here I am using matpplotlib package"
"matplotlib installation command - pip install matplotlib"
                                                

from matplotlib import pyplot as plt                      # import pyplot module from matplotlib package
 
fig=plt.figure()                                          # initializing a figure
fig.suptitle("GC content of species")                      # Giving a title to the figure
ax= fig.add_subplot(111)                                   # defining ax function by adding subplot
ax.boxplot(lis)                                            # creating boxplot
plt.xlabel(name)                                           # labelling the x axis with species name user entered
plt.ylabel("GC content")                                   # labelling y axis as GC content
plt.savefig("plotimg2.png")                                # saving the image in given file name:user can enter any filename with appropriate extension(exceptions are there like pdf).
                                                           #user can find the image in same directory where fasta files and program are stored.
plt.show()                                                 # temporary output to view the image(user can skip this)
"*****************************End of Program****************************"
