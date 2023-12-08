# Program 1 - Perulangan dengan Output Tertentu
for i in range(1, 101):
    if i == 6 or (i >= 7 and i <= 10):
        print("Aku Arief Ganteng")
    else:
        print(i)

# Program 2a - For Loops
my_list = [3, 8, 5, 12, 20]

for value in my_list:
    if value < 10:
        print(f"{value} kurang dari 10")
    else:
        print(f"{value} lebih dari atau sama dengan 10")

# Program 2b - While Loops
counter = 5

while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1

print("Countdown selesai!")

# Program 3 - Variabel Array dan Perulangan For
my_array = [1, 4, 5, 9, 17]

for value in my_array:
    print(value)
