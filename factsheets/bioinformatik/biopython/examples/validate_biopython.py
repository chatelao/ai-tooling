from Bio import SeqIO
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
fasta_path = os.path.join(script_dir, 'example.fasta')
for record in SeqIO.parse(fasta_path, 'fasta'):
    print(record.id, record.seq)
