b = "Hello, World!"
print(b[2:5]) #b[startIndex:endIndex]

b2 = "Hello, World!"
print(b[:5])

b3 = "Hello, World!"
print(b[-3:-1]) # b[end:start] when use negative index which will start from -1 to -3

print(len("Hello, World!"))
print(b.lower()); print(b.upper())
print("    Hello    ".strip())
print("Hello, World!".replace("H", "J"))
print("Hello, World!".split(","))

#String format
price = 59
print(f"The price is {price} dollars")
print(f"The price is {price:.2f} dollars")
print(f"The price is {20 * 59} dollars")