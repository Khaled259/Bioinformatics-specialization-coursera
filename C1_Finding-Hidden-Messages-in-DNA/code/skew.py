# C1: Finding Hidden Messages in DNA
# Week 2: Minimum Skew Problem

def find_minimum_skew(genome):
    """
    Finds all positions in a genome where the GC skew (#G - #C) is minimized.

    This algorithm makes a single pass over the genome, calculating the
    cumulative skew at each position and keeping track of the positions where
    the minimum value is found.

    Args:
        genome (str): The DNA string to analyze.

    Returns:
        list: A list of all integer positions (1-based) where the skew
              reaches its minimum value.
    """
    positions = [0]  # The skew is always 0 before the first nucleotide
    skew = 0
    min_skew = 0

    for i in range(len(genome)):
        # Update skew based on the current nucleotide
        if genome[i] == 'G':
            skew += 1
        elif genome[i] == 'C':
            skew -= 1

        # Check against the current minimum
        if skew < min_skew:
            min_skew = skew
            # We found a new minimum, so reset our list of positions
            positions = [i + 1]
        elif skew == min_skew:
            # We found another position with the same minimum, add it
            positions.append(i + 1)
            
    return positions

# This block allows the script to be run directly from the command line
if __name__ == '__main__':
    # --- Sample Input from the course ---
    # Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    # Expected Output: 11 24

    # Ask for user input to test any genome
    input_genome = input("Enter a DNA string (Genome) to find minimum skew positions: ")
    
    if not input_genome:
        print("\nUsing default sample genome:")
        input_genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
        print(input_genome)

    # Calculate the minimum skew positions
    min_skew_positions = find_minimum_skew(input_genome)

    # Print the result in the format required by the course (space-separated integers)
    print("\nPositions with minimum skew:")
    print(" ".join(map(str, min_skew_positions)))
