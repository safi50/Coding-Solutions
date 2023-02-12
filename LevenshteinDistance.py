
#Taking user Inputs of Strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

#variables for counting operations
ins = 0
dele = 0
sub = 0

a = len(str1)
b = len(str2)

#creating a 2D of size lengths of input strings + 1
lev = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

#populating first row and column

for i in range(len(str1) + 1):
  lev[i][0] = i

for i in range(len(str2) + 1):
  lev[0][i] = i

# Using Levenshtein Algorithm 
  
for i in range(1, len(str1) + 1):
  for j in range(1, len(str2) + 1):
    if str1[i - 1] == str2[j - 1]:
      lev[i][j] = lev[i - 1][j - 1]
    else:
      insertion = lev[i][j - 1] + 1
      deletion = lev[i - 1][j] + 1
      substitution = lev[i - 1][j - 1] + 1

      lev[i][j] = min(insertion, deletion, substitution)

# Printing Matrix 
print("\nLevenshtein Matrix is: ")
for i in range(len(lev)):
  print(lev[i], ",")

print("\nLevenshtein Distance: ", lev[len(str1)][len(str2)])

# Calculating Number of Insertions, Deletions, and Substitutions
while a != 0 or b != 0:
  if lev[a][b - 1] <= min(lev[a - 1][b], lev[a - 1][b - 1]):
    ins = ins + 1
    b = b - 1
  elif lev[a - 1][b] < min(lev[a][b - 1], lev[a - 1][b - 1]):
    dele = dele + 1
    a = a - 1

  elif lev[a - 1][b - 1] < min(lev[a][b - 1], lev[a - 1][b]):
    if lev[a-1][b-1] != lev[a][b]:
      sub = sub + 1
    a = a - 1
    b = b - 1


print("\nNumber of Insertions: ", ins)
print("Number of Deletions: ", dele)
print("Number of Substitutions: ", sub)
