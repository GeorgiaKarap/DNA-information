from programs import gc_content, reverse_complement, translate_dna

if __name__ == "__main__":
    sequence = "ATGCGATACGTT"

    print(f"DNA sequence: {sequence}")
    print(f"GC content: {gc_content(sequence):.2f}%")
    print(f"Reverse complement: {reverse_complement(sequence)}")
    print(f"Protein translation: {translate_dna(sequence)}")
