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
