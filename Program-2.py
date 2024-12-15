def generate_series(a):
    series = []
    for i in range(a):
        series.append(2 * i - 1)
    return series

a = int(input("Enter a value : "))

if a>0:
    result = generate_series(a)
    print(", ".join(map(str, result)))
else:
    print("Please enter positive Number")
