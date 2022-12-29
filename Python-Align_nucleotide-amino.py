def gapsFromPeptide( peptide_seq, nucleotide_seq ):
    """Trasferisce gli spazi vuoti dalla seq peptidica allineato alla seq nucleotidica partizionata in codoni
           - peptide_seq è una sequenza peptidica allineata con gap che devono essere trasferiti alla seq nucleotidica
           - nucleotide_seq è una sequenza di DNA non allineata i cui codoni si traducono in peptide seq"""
    def chunks(nucleo, n):
        """ Genera blocchi sucessivi di dimensione n dalla seq nucleotidica"""
        for i in range(0, len(nucleo), n):
            yield nucleo[i:i+n] #Uso yeald per farmi restituire un risultato per volta dal generatore
    codons = [codon for codon in chunks(nucleotide_seq,3)]  #splitto i nucleotidi in codoni (triplets)
    #print(codons)
    gappedCodons = []
    codonCount = 0
    for aa in peptide_seq:  #aggiungo '---' gaps alla sequenza nucleotidica correspondente alla peptidica
        if aa!='-':
            gappedCodons.append(codons[codonCount])
            #print(gappedCodons)
            codonCount += 1
        else:
            #print(aa)
            gappedCodons.append('---')
    return(''.join(gappedCodons))

'''Apro i file della sequenza nucleotidica e di quella proteica elimino gli spazi e i "\n" e li trasformo in stringa'''
file = open('/Users/rosadesantis/Desktop/Sample-dna.txt', 'r')
dna1 = file.read()
dna=dna1.replace("\n",'')
unaligned_dna_seq = str(dna.replace(" ",''))
#print(unaligned_dna_seq)
file = open('/Users/rosadesantis/Desktop/Prot.txt', 'r')
seq=file.read()
s=seq.replace("\n",'')
aligned_peptide_seq=str(s.replace(" ",''))
#print(aligned_peptide_seq)

#unaligned_dna_seq='ATGTTTGTTTTTCTTGTTTTATTGCCAATCTTTAAAATAAAACCC'
#aligned_peptide_seq='-MFVFLVLLP---SKYWER'
'''Richiamo la funzione'''
aligned_dna_seq = gapsFromPeptide(aligned_peptide_seq, unaligned_dna_seq)
print(aligned_dna_seq)

