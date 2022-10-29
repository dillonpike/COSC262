num_calls = 0  # Global counter of mat_mul calls

def mat_mul(m1, m2):
    """Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       as lists of lists.
    """
    global num_calls # Counter of calls (for marking)
    num_calls += 1   # Increment the count of calls
    n = len(m1)    # Size of the matrix
    assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)]
    return mprod

def mat_power(m, p):
    if p == 1:
        return m
    elif p % 2 == 0:
        a = mat_mul(m, m)
        return mat_power(a, p/2)
    else:
        return mat_mul(mat_power(m, p-1), m)
    
