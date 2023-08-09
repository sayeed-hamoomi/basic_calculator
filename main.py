import utils

print(
    "menu\n   operation\n1. Addition\n2. Subtraction\n3. multiplycation\n4. division\n5. modulus\n6. exponant\n7. floor division\n8. mean\n9. median\n10. mode"
)
option = int(input("select an operation: "))
i = 0
n = int(input("enter the number of operands: "))
operands = []
while i < n:
    operand = int(input("enter the number: "))
    operands.append(operand)
    i += 1


if option == 1:
    result = utils.addition(operands)
    print(f"The result of operation is: {result}")

elif option == 2:
    result = utils.subtraction(operands)
    print(f"The result of operation is: {result}")
elif option == 3:
    result = utils.multiplication(operands)
    print(f"the result of operation is: {result}")
elif option == 4:
    result = utils.division(operands)
    print(f"the result of operation is: {result}")
elif option == 5:
    result = utils.modulus(operands)
    print(f"the result of operation is: {result}")
elif option == 6:
    result = utils.exponent(operands)
    print(f"the result of operation is: {result}")
elif option == 7:
    result = utils.floor_division(operands)
    print(f"the result of operation is: {result}")
elif option == 8:
    result = utils.mean(operands, n)
    print(f"the result of operation is: {result}")
elif option == 9:
    result = utils.median(operands, n)
    print(f"the result of operation is: {result}")
elif option == 10:
    result = utils.mode(operands)
    print(f"the result of operation is: {result}")
