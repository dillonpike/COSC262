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
        result_root = mat_power(m, p/2)
        return mat_mul(result_root, result_root)
    else:
        return mat_mul(mat_power(m, p-1), m)
        
# Simple case of squaring a matrix
m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
print(mat_power(m, 2))

# Raise same m as above to the power of 20.
# Check number of calls to mat_mul.
m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
num_calls = 0
m20 = mat_power(m, 20)
if num_calls != 5:
    print(f"Wrong number of calls to mat_mul. Expected 5, got {num_calls}")
for row in m20:
    print(row)
    
# Raise same m as above to the power of 19.
# Check number of calls to mat_mul.
m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
num_calls = 0
m19 = mat_power(m, 19)
if num_calls != 6:
    print(f"Wrong number of calls to mat_mul. Expected 6, got {num_calls}")
for row in m19:
    print(row)
    
# A 100 x 100 identity matrix raised to the power of 100
mat = []
for i_row in range(100):
    row = [1 if j == i_row else 0 for j in range(100)]
    mat.append(row)

num_calls = 0
m100 = mat_power(mat, 100)
if num_calls != 8:
    print(f"Wrong number of calls to mat_mul. Expected 8, got {num_calls}")
if mat != m100:
    print("Sorry, wrong answer")
else:
    print("OK")