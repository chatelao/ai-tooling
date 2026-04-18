from Bio import SeqIO
import os
# Correct path relative to where biopython_run_test.sh is executed
for record in SeqIO.parse('examples/example.fasta', 'fasta'):
    print(record.id, record.seq)
