x = int(input("First positive value: "))
y = int(input("Second positive value: "))

z = (x * y) / 10
z = int(z)
bit_shift_value = 1 << z  # shift 1 to the left by z value which is derved from amount of zeros in the product 

# Print the result
print(bit_shift_value,"Is the value ")
