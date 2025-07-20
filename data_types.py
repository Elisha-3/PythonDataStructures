# Perform arithmetic and string concatenation.
# You’re given:

# An integer: i = 4

# A float: d = 4.0

# A string: s = "HackerRank "
i = 4
d = 4.0
s = "HackerRank "
#  Read and convert input values
i2 = int(input())
d2 = float(input())
s2 = input()
#  Print the sum of i and i2
print(i + i2)
#  Print the sum of d and d2
print(f"{d + d2:.1f}")
#  Print the concatenation of s and s2
print(s + s2)
