# Course 1: Finding Hidden Messages in DNA

This section of my portfolio covers my work from the first course in the specialization, which introduces fundamental concepts of bioinformatics by searching for regulatory sequences in DNA.

---

### Week 1: Finding the Origin of Replication (ori)

#### The Biological Problem

DNA replication in bacteria begins at a specific region called the **origin of replication (ori)**. A key protein, **DnaA**, initiates this process by binding to short, specific DNA sequences within the ori known as **DnaA boxes**.

The central challenge is to identify these DnaA boxes computationally. Since DnaA needs to bind multiple times in a small region to start replication, the biological hypothesis is that **DnaA boxes are surprisingly frequent k-mers** within the ori region. This translates a biological mystery into a clear computational problem.

#### The Computational Problem: Frequent Words Problem

-   **Input:** A DNA string `Text` and an integer `k`.
-   **Output:** All `k`-mers that appear most frequently in `Text`.

#### My Implementation: `BetterFrequentWords`

The provided code (`code/frequent_words.py`) implements an efficient solution to the Frequent Words Problem. This approach is much faster than a naive brute-force method which would have a runtime of O(|Text|² * k).

The algorithm works in two main steps:

1.  **`FrequencyTable(Text, k)`**: First, we iterate through the `Text` once, sliding a window of length `k`. For each k-mer, we store it in a frequency map (a dictionary in Python) and increment its count. This avoids re-scanning the entire text for every single k-mer.

2.  **`BetterFrequentWords(Text, k)`**: After building the frequency map, we find the maximum frequency value among all k-mers. Then, we iterate through the map one more time to collect all k-mers that have this maximum frequency.

This two-pass approach is significantly more efficient for large genomes.

#### Usage

The script is runnable from the command line.

```bash
# Navigate to the code directory
cd C1_Finding-Hidden-Messages-in-DNA/code/

# Run the script
python frequent_words.py
```

**Sample Input:**
- `Text`: `ACGTTGCATGTCGCATGATGCATGAGAGCT`
- `k`: `4`

**Expected Output:**
```
CATG GCAT
```

---

### Key Concepts from Week 1

Beyond finding frequent words, this week introduced other critical concepts that I implemented solutions for:

*   **The Reverse Complement Problem:** DnaA protein can bind to either of DNA's two strands. Therefore, we must also consider the reverse complement of a k-mer when searching. For example, in *Vibrio cholerae*, `ATGATCAAG` and its reverse complement `CTTGATCAT` were both found to be frequent, strengthening the evidence that they are the DnaA box.

*   **The Pattern Matching Problem:** After identifying a candidate DnaA box, it's essential to find all its occurrences throughout the entire genome to confirm that it is uniquely clustered within the ori.

*   **The Clump Finding Problem:** This generalizes the search. Instead of looking for a *specific* frequent k-mer, we look for *any* k-mer that forms a "clump" (appears `t` or more times in a window of length `L`). This is a powerful technique for finding regulatory regions in a new genome where the DnaA box sequence is unknown.


# Week 2: A Scientific Detective Story - Skew Diagrams and Mismatches

## The Initial Mystery: A Failing Algorithm
Week 1's **FrequentWords** algorithm was a success on the *Vibrio cholerae* genome, but it failed to find the Origin of Replication (**ori**) in the well-studied *E. coli* genome.  
This mystery indicates that the "hidden message" of replication is more subtle and elusive than just finding the most common k-mer. We needed a new clue.

---

## The Breakthrough Clue: Asymmetry of DNA Replication
The critical insight comes from the biology of DNA replication. The process is asymmetric due to the unidirectional nature of the DNA polymerase enzyme:

- **Leading strand**: copied continuously, spends most of its time in a stable double-helix.  
- **Lagging strand**: copied in short segments, remains single-stranded for longer periods.  

This single-stranded state makes DNA more susceptible to a specific mutation: **deamination**, where a Cytosine (**C**) often transforms into a Thymine (**T**).

---

## Computational Problem 1: The Minimum Skew Problem
This biological bias gives us a computational tool for locating the approximate position of the **ori**.

- **Hypothesis**: Because of deamination, a statistical difference exists between the number of Guanines (#G) and Cytosines (#C) on the two strands.  
- **The GC Skew**: Defined as (#G – #C).  
  - It **decreases** on the half-genome leading to the ori.  
  - It **increases** on the half-genome after the ori.  
- **Computational Goal**: The ori is located at the position where the GC skew reaches its **absolute minimum**.  

This transforms the search into the **Minimum Skew Problem**.

- **Input**: A DNA string `Genome`.  
- **Output**: All positions `i` in `Genome` that minimize the GC skew.  

My implementation in `code/skew.py` solves this efficiently in a single pass.

---

## A Final Twist: Finding the "Approximate" Message
While the Minimum Skew method identified the ori region in *E. coli*, exact frequent k-mers still failed.  

**Biological insight**: Protein binding tolerates small errors. The **DnaA protein** can bind to sequences close, but not identical, to the perfect "DnaA box".  

Thus, our algorithm must find **frequent words with mismatches**.

---

## Computational Problem 2: Frequent Words with Mismatches and Reverse Complements
This is the biologically realistic formulation.

- **Input**: A DNA string `Text`, a k-mer length `k`, and a maximum number of mismatches `d`.  
- **Output**: All k-mers most frequent in `Text` (including reverse complements) when allowing up to `d` mismatches.  

My script `code/frequent_words_mismatch.py` solves this using:

- **HammingDistance**: to count differences between two strings.  
- **Neighbors**: generates the full **d-neighborhood**, i.e., all k-mers within `d` mismatches.  

---

## The Final Solution: A Full Bioinformatics Pipeline
By combining these tools, we solved the *E. coli* ori mystery:

1. Run `find_minimum_skew.py` on the genome to locate the approximate ori.  
2. Extract a **500 bp window** around this minimum skew location.  
3. Run `frequent_words_mismatch.py` with `k=9` and `d=1`.  

This pipeline correctly identified **TTATCCACA** (and its reverse complement) as the hidden **DnaA box** in *E. coli*.  

---

## Key Concepts from Week 2
This week expanded the bioinformatics toolkit, moving from simple counting to biologically-informed analysis.

- **Replication Asymmetry**: Leading vs. lagging strand synthesis.  
- **GC Skew Diagram**: Mutation bias as a genomic signal.  
- **Hamming Distance**: Core metric for string comparison.  
- **d-Neighborhood**: All "nearby" sequence variations.  
- **Mismatch-Tolerant Pattern Finding**: Algorithms accounting for biological reality.  
- **Algorithmic Pipelines**: Chaining steps into a powerful solution.  
