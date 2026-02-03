# DNA to RNA converter

def dna_to_rna(dna_seq):
    """Convert DNA sequence to RNA by replacing T with U."""
    dna_seq = dna_seq.upper().strip()
    return dna_seq.replace("T", "U")


if __name__ == "__main__":
    dna = input("Enter DNA sequence: ")
    rna = dna_to_rna(dna)
    print("RNA sequence:", rna)

