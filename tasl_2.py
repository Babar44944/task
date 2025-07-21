numbers = [78, 92, 85, 63, 89, 55, 90, 74]

total = sum(numbers)
count = len(numbers)
average = total / count
print("Average is:", average)

hightes = max(numbers)
lowest = min(numbers)
print("Hightes", hightes)
print("Lowest", lowest)

count = 0

for i in numbers:
    if(i >= 60):
        count +=1
print(count)

passed = len([numbers for numbers in numbers if numbers >= 60])
failed = len(numbers) - passed
print("Numbers of statudent passesd: ", passed)
print("Numbers of Student failes: ", failed)


shot_numbers = sorted(numbers, reverse=True)
print("sorted Numbers:", shot_numbers)


