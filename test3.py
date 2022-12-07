measurements = [1,5,-12,4,5,645,12,456,-94,123,7,9,0,1,456,-43,38,-28,0,1,6,12,4,12,54]


negatives = 0
fifty = 0
hundred = 0

for value in measurements:
    if value < 0:
        negatives += 1

    if value > 50:
        fifty += 1

    if value > 100:
        hundred += 1

print("Negatives " + str(negatives))
print("Greater than 50 " + str(fifty))
print("Greater than 100 " + str(hundred))