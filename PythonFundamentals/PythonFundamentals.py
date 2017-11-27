2 + 2
6 * 7
x = 5
x
3 * x
_
_ * 2
print('Hello, Python')

for i in range(5):
    x = i * 10
    print(x)

import math
math.sqrt(81)
help(math.sqrt)
help(math.factorial)
math.factorial(5)
math.factorial(6)
n = 5
k = 3
math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
from math import factorial
factorial(n) / (factorial(k) * factorial(n - k))
from math import factorial as fac
fac(n) / (fac(k) * fac(n - k))
2**31 - 1 
fac(12)
fac(13)
n = 100
k = 2
fac(n) // (fac(k) * fac(n - k))
fac(n)
len(str(fac(n)))

10
0b10
0o10
0x10
int(3.5)
int(-3.5)
int("496")
int("10000", 3)
3.125
3e8
1.616e-35
float(7)
float("1.618")
float("nan")
float("inf")
float("-inf")
3.0 + 1
None
a = None
a is None
True
False
bool(0)
bool(42)
bool(-1)
bool(0.0)
bool(0.207)
bool(-1.117)
bool([])
bool([1, 5, 9])
bool("")
bool("Spam")
bool("True")
bool("False")

g = 20
g == 20
g == 13
g != 20
g != 13
g < 30
g > 30
g <= 20
g >= 20

if True:
    print("It's true!")

if False:
    print("It's true!")

if bool("eggs"):
    print("Yes please")

if "eggs":
    print("Yes please")

h = 42
if h > 50:
    print("Greater than 50")
else:
    print("50 or smaller")

if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")

c = 5
while c != 0:
    print(c)
    c -= 1
else:
    print("end of while loop")
    print(c)

while True:
    print("Looping")

while True:
    response = input('--> ')
    if int(response) % 7 == 0:
        break

