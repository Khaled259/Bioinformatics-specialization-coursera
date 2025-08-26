# C1: Finding Hidden Messages in DNA
# Week 1: Frequent Words Problem

def FrequencyTable(text, k):
    """
    Generates a frequency map of k-mers in a given text.

    Args:
        text (str): The DNA string to analyze.
        k (int): The length of the k-mers.

    Returns:
        dict: A dictionary where keys are k-mers and values are their frequencies.
    """
    freqMap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        # Use dict.get() for a cleaner implementation
        freqMap[pattern] = freqMap.get(pattern, 0) + 1
    return freqMap

def MaxMap(freqMap):
    """
    Finds the maximum value in a frequency map dictionary.

    Args:
        freqMap (dict): A dictionary of item frequencies.

    Returns:
        int: The highest frequency found in the map.
    """
    # Python's built-in max() function is more efficient for this
    if not freqMap:
        return 0
    return max(freqMap.values())

def BetterFrequentWords(text, k):
    """
    Finds the most frequent k-mers in a DNA string.
    This is an efficient implementation that uses a frequency map.

    Args:
        text (str): The DNA string to analyze.
        k (int): The length of the k-mer.

    Returns:
        list: A list of all k-mers that have the highest frequency.
    """
    frequent_patterns = []
    freqMap = FrequencyTable(text, k)
    max_val = MaxMap(freqMap)
    
    for pattern in freqMap:
        if freqMap[pattern] == max_val:
            frequent_patterns.append(pattern)
            
    return frequent_patterns

# Main function to make the script runnable
if __name__ == "__main__":
    # Sample Input from the course
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4

    # Run the function
    most_frequent_kmers = BetterFrequentWords(text, k)

    # Print the result in the format required by the course
    print(" ".join(most_frequent_kmers))

    # Example Output should be: CATG GCAT
