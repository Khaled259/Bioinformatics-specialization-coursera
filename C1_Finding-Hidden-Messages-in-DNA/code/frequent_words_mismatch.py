# C1: Finding Hidden Messages in DNA
# Week 2: Frequent Words with Mismatches and Reverse Complements

from collections import defaultdict

# --- Helper Functions ---

def hamming_distance(p, q):
    """
    Calculates the Hamming distance between two DNA strings of equal length.
    
    Args:
        p (str): The first DNA string.
        q (str): The second DNA string.
        
    Returns:
        int: The number of mismatches between p and q.
    """
    return sum(1 for ch1, ch2 in zip(p, q) if ch1 != ch2)

def reverse_complement(pattern):
    """
    Computes the reverse complement of a DNA string.
    
    Args:
        pattern (str): The DNA string.
        
    Returns:
        str: The reverse complement of the pattern.
    """
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement_map.get(base, 'N') for base in reversed(pattern))

def neighbors(pattern, d):
    """
    Recursively generates the d-neighborhood of a pattern. The d-neighborhood
    is the set of all k-mers with Hamming distance at most d from the pattern.
    
    Args:
        pattern (str): The starting DNA pattern.
        d (int): The maximum allowed Hamming distance.
        
    Returns:
        set: A set of all k-mers in the d-neighborhood.
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
        
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in 'ACGT':
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
            
    return neighborhood

# --- Core Algorithm ---

def frequent_words_mismatch_rc_FAST(text, k, d):
    """
    Finds the most frequent k-mers (with up to d mismatches and reverse complements)
    in a given DNA text. This is an optimized algorithm suitable for larger datasets.
    
    Args:
        text (str): The DNA string to analyze.
        k (int): The length of the k-mer.
        d (int): The maximum number of mismatches allowed.
        
    Returns:
        list: A list of the most frequent k-mers found.
    """
    # 1. First, count only the k-mers that ACTUALLY appear in the text and their complements.
    actual_kmer_counts = defaultdict(int)
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        pattern_rc = reverse_complement(pattern)
        actual_kmer_counts[pattern] += 1
        actual_kmer_counts[pattern_rc] += 1

    # 2. Score candidate patterns by summing counts of all real k-mers in their neighborhood.
    candidate_scores = defaultdict(int)
    for pattern, count in actual_kmer_counts.items():
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            candidate_scores[neighbor] += count

    # 3. Find the maximum score among all candidates.
    max_score = 0
    if candidate_scores:
        max_score = max(candidate_scores.values())

    # 4. Collect all k-mers that achieve this maximum score.
    result_patterns = [
        pattern for pattern, score in candidate_scores.items() if score == max_score
    ]
        
    return result_patterns

# This block allows the script to be run directly from the command line
if __name__ == '__main__':
    # --- Sample Input from the course ---
    # Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    # k = 4, d = 1
    # Expected Output: ATGT ACAT

    # Ask for user input to test with any data
    input_text = input("Enter a DNA string (Text): ")
    input_k = int(input("Enter k-mer length (k): "))
    input_d = int(input("Enter max mismatches (d): "))

    if not input_text:
        print("\nUsing default sample data:")
        input_text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
        input_k = 4
        input_d = 1
        print(f"Text: {input_text}\nk: {input_k}, d: {input_d}")
    
    # Calculate the most frequent k-mers
    frequent_patterns = frequent_words_mismatch_rc_FAST(input_text, input_k, input_d)
    
    # Print the result in the format required by the course (space-separated)
    print("\nMost frequent k-mers (with mismatches and reverse complements):")
    print(" ".join(frequent_patterns))
