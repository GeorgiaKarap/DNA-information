# DNA Sequence Toolkit

A simple Python toolkit for basic DNA sequence analysis.  
Its functions calculate GC content, generate the reverse complement, and translate DNA into protein sequences.

---

## Features
- Calculates GC content of a DNA sequence.
- Gets the reverse complement of a DNA sequence.
- Translates DNA into a protein sequence using the standard codon table.
  
---

## Project Structure
dna_sequence_toolkit/
- programs/
  - __ init __.py
  - gc_content.py
  - reverse_complement.py
  - translate_dna.py
- main.py
- README.md
- LICENSE
- .gitignore

---

## How It Works

- The user provides a DNA sequence as input (string).  
- Functions from the dna_toolkit module are applied to:  
  - Calculate GC content
  - Find the reverse complement
  - Translate to protein  
- Results are printed in the terminal.  

---

## Example Usage

python main.py</p>

Example output:<br>
DNA sequence: ATGCGATACGTT<br>
GC content: 50.00%<br>
Reverse complement: AACGTATCGCAT<br>
Protein translation: MYR</p>

---

## Input Files

This program works directly with DNA sequences provided as strings.<br>

---

## Installation

Download the zip file and unzip it. 

---

## Compilation

No compilation is needed.

---

## Execution

Open the IDLE of Python (Python 3.12 recommended).<br>
Select "File", "Open File", "main.py". Into this new window select "Run" and "Run Module"

---

## Notes

- Only standard Python 3 is required. No external libraries are needed.
- The DNA sequence is already installed in the program.
 
---

## License

This project is licensed under the ΜΙΤ License
