ages = [12,34,15,73,73,13,97,23,95,23,98,53,83,45,90,23,75,23,78]

solution = ages[0]
for age in ages:
    if age > solution:
        solution = age

print(solution)

