# TranscriptAssembly
Genome assempbly using adaptive overlapping graph traversal.

## Usage: 
```bash
python findTransript.py kmer
```
## Example:

### Input:
```bash
AAGGGATTTCGGA	1
ACCCTAAATTTTA	1
TATTTCATCCACA	1
TAGGGCATCCACA	1
ACAATTGGTCCAA	1
```
### Run:
```bash
python findTransript.py k-mer.txt
```

### Output:
#### Possible transcripts:
 ```bash
[ACCCTAAATTTTA,TATTTCATCCACA, ACAATTGGTCCAA, AAGGGATTTCGGA]
[ACCCTAAATTTTA,TAGGGCATCCACA, ACAATTGGTCCAA, AAGGGATTTCGGA']
[ACCCTAAATTTTA, TATTTCATCCACA, ACAATTGGTCCAA] 
[TATTTCATCCACA, ACAATTGGTCCAA, AAGGGATTTCGGA]
[TAGGGCATCCACA, ACAATTGGTCCAA, AAGGGATTTCGGA]
```
