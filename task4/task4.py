with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]


minim = float('inf')
for i in range(len(numbers)):
    summ = 0
    for j in range(len(numbers)):
        if i == j:
            continue
        summ += abs(numbers[i] - numbers[j])
    if summ < minim:
        minim = summ

print(minim)
