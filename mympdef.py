from collections import defaultdict

def maketotal(dictionary):
    """Calculate the total sum of values in a dictionary."""
    return sum(dictionary.values())

def compute_jaccard_for_pair(pair):
    """Calculate Jaccard similarity for a pair of dictionaries."""
    dict1, dict2 = pair
    intersection = {item: min(dict1[item], dict2[item]) for item in dict1 if item in dict2}
    intersection_total = maketotal(intersection)
    union = maketotal(dict1) + maketotal(dict2) - intersection_total
    return intersection_total / union if union > 0 else 0

def mapper(pairs):
    """Compute Jaccard similarity for a subset of pairs and return results as a dictionary."""
    
    collector = defaultdict(float)
    for (i, j), (dict1, dict2) in pairs:
        collector[(i, j)] = compute_jaccard_for_pair((dict1, dict2))
    return collector





