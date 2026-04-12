from Bio import SeqIO
import os
for record in SeqIO.parse('factsheets/bioinformatik/biopython/examples/example.fasta', 'fasta'):
    print(record.id, record.seq)