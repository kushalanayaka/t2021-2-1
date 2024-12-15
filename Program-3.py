def generate_series(a):
    n = a if a % 2 !=0 else a-1
    return[2 * i + 1 for i in range(n)]

a = int(input("Enter a value : "))

if a > 0:
    result = generate_series(a)
    print(", ".join(map(str, result)))
else:
    print("Please enter positive Number.")
