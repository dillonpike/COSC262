def memoise(f):
    """Adds a functions parameter and return pairs into a dictionary."""
    cache = {}
    def new_f(*param):
        """Wrapper function to store parameter and return pairs into a dictionary."""
        if param not in cache:
            cache[param] = f(*param)
        return cache[param]
    return new_f
    

@memoise
def lcs(s1, s2):
    """Returns the longest common subsequence."""
    if len(s1) == 0 or len(s2) == 0:
        return ''
    elif s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1]) + s1[-1]
    else:
        result1 = lcs(s1[:-1], s2)
        result2 = lcs(s1, s2[:-1])
        if len(result1) >= len(result2):
            return result1
        else:
            return result2
            
# A simple test that should run without caching
s1 = "abcde"
s2 = "qbxxd"
string = lcs(s1, s2)
print(string)

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))