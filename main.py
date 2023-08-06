import utils

print(
    "menu\n   operation\n1. Addition\n2. Subtraction\n3. multiplycation\n4. modulus\n5. division\n6. exponant\n7. floor division\n8. mean\n9. median\n10. mode"
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
    result = utils.addition(*operands)


print(f"The result of operation is: {result}")
