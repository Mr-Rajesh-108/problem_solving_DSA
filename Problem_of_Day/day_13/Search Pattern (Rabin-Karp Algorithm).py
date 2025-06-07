def rabin_karp(text, pattern):
    # Base and modulus for hash function
    base = 256  # Total number of characters in the input alphabet (a-z)
    mod = 10**9 + 7  # A large prime to avoid overflow and reduce collisions

    n, m = len(text), len(pattern)
    if m > n:
        return []

    # Precompute (base^(m-1)) % mod
    h = 1
    for _ in range(m - 1):
        h = (h * base) % mod

    # Compute hash of pattern and first window of text
    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod

    positions = []

    # Slide the pattern over text
    for i in range(n - m + 1):
        # Check the hash values first
        if p_hash == t_hash:
            # Double-check characters to avoid false positive
            if text[i:i + m] == pattern:
                positions.append(i + 1)  # 1-based indexing

        # Compute hash of next window
        if i < n - m:
            t_hash = (t_hash - ord(text[i]) * h) * base + ord(text[i + m])
            t_hash %= mod
            if t_hash < 0:
                t_hash += mod

    return positions


print(rabin_karp("birthdayboy", "birth"))        # Output: [1]
print(rabin_karp("geeksforgeeks", "geek"))       # Output: [1, 9]
print(rabin_karp("abcabcabc", "abc"))            # Output: [1, 4, 7]
print(rabin_karp("abcdefgh", "xyz"))             # Output: []
