def lcs(s1, s2):
    """Returns the longest common subsequence of both strings."""
    table = [(len(s2)+1) * [0] for i in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    i, j = len(s1), len(s2)
    subsequence = ""
    while table[i][j] != 0:
        if s1[i-1] == s2[j-1]:
            subsequence = s1[i-1] + subsequence
            i -=1
            j -=1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1
    return subsequence

def line_edits_table(lines1, lines2):
    """Makes a bottom up table for line_edits."""
    table = [(len(lines2)+1) * [0] for i in range(len(lines1)+1)]
    for i in range(1, len(lines1)+1):
        table[i][0] = i
    for j in range(1, len(lines2)+1):
        table[0][j] = j
    for i in range(1, len(lines1)+1):
        for j in range(1, len(lines2)+1):
            if lines1[i-1] == lines2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
    return table

def mark_extras(string1, string2):
    """Returns string1 with the characters not in string2 marked."""
    i = 0
    new_string = ""
    for char in string1:
        if i < len(string2) and string2[i] == char:
            new_string += char
            i += 1
        else:
            new_string += f"[[{char}]]"
    return new_string

def line_edits(s1, s2):
    """Returns the line edits made to s1 to get s2."""
    lines1 = s1.splitlines()
    lines2 = s2.splitlines()
    table = line_edits_table(lines1, lines2)
    i, j = len(lines1), len(lines2)
    edits = []
    while i > 0 and j > 0:
        min_neighbour = min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        if lines1[i-1] == lines2[j-1]:
            edits.append(("C", lines1[i-1], lines2[j-1]))
            i -= 1
            j -= 1
        elif table[i-1][j-1] == min_neighbour:
            common = lcs(lines1[i-1], lines2[j-1])
            string1, string2 = mark_extras(lines1[i-1], common), mark_extras(lines2[j-1], common)
            edits.append(("S", string1, string2))
            i -= 1
            j -= 1
        elif table[i-1][j] == min_neighbour:
            edits.append(("D", lines1[i-1], ""))
            i -= 1
        else:
            edits.append(("I", "", lines2[j-1]))
            j -= 1
    while i > 0:
        edits.append(("D", lines1[i-1], ""))
        i -= 1
    while j > 0:
        edits.append(("I", "", lines2[j-1]))
        j -= 1
    edits.reverse()
    return edits

s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)