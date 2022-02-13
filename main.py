import string


def make_dict_from_txt(txtfile: list):
    d = {}
    for line in txtfile:
        d[line[0:3]] = line[4:7]
    return d



def dna_to_rna(dna: str):
    return dna.replace("T", "U")

def rna_to_amino_acids(rna: str):
    codons = []
    # 1. Break the string into lists of 3 chars (codons)
    # 2. Plug the codons into the dictionary read from the file
    num_codons = len(rna)//3
    num_cycles = 0
    i = 0
    while num_cycles <= num_codons - 1:
        codon = rna[i:i+3]
        amino_acid = codonDict[codon]
        codons.append(amino_acid)
        if amino_acid == 'stop':
            return (codons,"")
        i += 3
        num_cycles += 1
    return (codons, rna[i:])



# read the file containing the codon to amino acid converter
lines = open("codon-to-protein.txt").readlines()
# convert it to a dictionary
codonDict = make_dict_from_txt(lines)


while True:
    dna_sequence = input("Please enter the DNA sequence you would like to transcribe to mRNA (coding strand, not the template strand):")
    dna_sequence = dna_sequence.upper().strip();
    blacklist = [char for char in string.ascii_uppercase if char not in ['A', 'T', 'G', 'C']]
    bad_chars = [char for char in blacklist if char in dna_sequence]
    if (len(bad_chars) == 0):
        break
    else:
        print("You've entered at least one character that isn't allowed...")
        print("Bad characters entered: {}".format(bad_chars))

rna = dna_to_rna(dna_sequence)
(amino_acids, untranslated) = rna_to_amino_acids(rna)
print("Amino Acid Sequence:")
print(amino_acids)
print("Untranslated RNA Sequence: {}".format(untranslated))

