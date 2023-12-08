# Tugas 1 PBO (Pemrograman Perbasis Objek)

## Nama : Arief Haris Prasetyo Rizaldi

## NPM : G1F022073

## Soal :

1. Buatlah perulangan hingga 100 menggunakan Python dengan output sebagai berikut:
   1
   2
   3
   4
   6
   8
   9
   Your Name
   Your Name
   Your Name
   11
   12
   13
   14
   15
   16
   17
   18
   19
   Your Name
   Your Name
   Your Name

2. Buatlah program bebas, dengan menerapkan if else pada:
   a. For Loops
   b. While Loops

3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for

## Jawab :

### Program 1 - Perulangan dengan Output Tertentu

**Source Code :**

```
for i in range(1, 101):
    if i == 6 or (i >= 7 and i <= 10):
        print("Aku Arief Ganteng")
    else:
        print(i)
```

**Output :**

![Alt text](<Gambar/Perulangan dengan Output Tertentu.jpeg>)

**Penjelasan :**

1. `for i in range(1, 101):` Ini adalah loop for yang akan melakukan for pada variabel i dari 1 hingga 100 .

2. `if i == 6 or (i >= 7 and i <= 10)`: Jika nilai i sama dengan 6 atau berada di antara 7 dan 10 (inklusif), maka kondisi ini terpenuhi.
   Jika kondisi di atas terpenuhi, program akan mencetak string "Aku Arief Ganteng".

3. `else: print(i)`: Jika kondisi di atas tidak terpenuhi, program akan mencetak nilai i.

## 2 Buatlah program bebas, dengan menerapkan if else pada: a. For Loops b. While Loops

### - For Loops

**Source Code :**

```
# Program 2a - For Loops
my_list = [3, 8, 5, 12, 20]

for value in my_list:
    if value < 10:
        print(f"{value} kurang dari 10")
    else:
        print(f"{value} lebih dari atau sama dengan 10")
```

**Output :**

![Alt text](<Gambar/For Loops.jpeg>)

**Penjelasan :**

1. `my_list = [3, 8, 5, 12, 20]`: Membuat list my_list yang berisi beberapa nilai.

2. `if value < 10`: Pada setiap iterasi, program melakukan pemeriksaan kondisi:

- Jika nilai `value` kurang dari 10, maka kondisi ini terpenuhi.
- Jika kondisi di atas terpenuhi, program akan mencetak pesan yang menyatakan bahwa nilai tersebut kurang dari 10.

3. `else: print(f"{value} lebih dari atau sama dengan 10")`: Jika kondisi di atas tidak terpenuhi, artinya nilai value lebih dari atau sama dengan 10, maka program akan mencetak pesan yang menyatakan bahwa nilai tersebut lebih dari atau sama dengan 10.

### - While Loops

**Source Code :**

```
# Program 2b - While Loops
counter = 5

while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1

print("Countdown selesai!")
```

**Output :**

![Alt text](<Gambar/While Loops.jpeg>)

**Penjelasan :**

1. `counter = 5`: Inisialisasi variabel counter dengan nilai 5.

2. `while counter > 0:`: Membuat loop while yang akan terus berjalan selama nilai counter lebih dari 0.

3. `print(f"Countdown: {counter}")`: Pada setiap iterasi, program mencetak pesan yang menampilkan nilai countdown saat itu.

4. `counter -= 1`: Setiap iterasi, nilai counter dikurangi 1.

5. `print("Countdown selesai!")`: Setelah loop selesai (ketika nilai counter menjadi 0), program mencetak pesan bahwa countdown telah selesai.

## 3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for

**Source Code :**

```
# Program 3 - Variabel Array dan Perulangan For
my_array = [1, 4, 5, 9, 17]

for value in my_array:
    print(value)

```

**Output :**

![Alt text](<Gambar/Variabel Array dan Perulangan For.jpeg>)

**Penjelasan :**

1. `my_array = [1, 4, 5, 9, 17]`: Membuat array (list) my_array yang berisi beberapa nilai.

2. `for value in my_array:`: Membuat loop for yang akan mengiterasi variabel value melalui setiap elemen dalam array my_array.

3. `print(value)`: Pada setiap iterasi, program mencetak nilai value, yang merupakan nilai dari elemen saat ini dalam array.
