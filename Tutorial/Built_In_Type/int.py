# python int 資料型別
# int is a built-in Python type.
# int is a class.
# int is immutable.
int_1 = 1
int_2 = int(1)
print(id(int_1))
print(id(int_2))
print(int_1 == int_2)
# int basic
print(f"int_1 + int_2", int_1 + int_2)
print(f"int_1 - int_2", int_1 - int_2)
print(f"int_1 * int_2", int_1 * int_2)
print(f"int_1 / int_2", int_1 / int_2)
print(f"int_1 // int_2", int_1 // int_2)
print(f"int_1 % int_2", int_1 % int_2)
print(f"int_1 ** int_2", int_1**int_2)
# int method
print(f"int_1.bit_length()", int_1.bit_length())
print(f"int_1.to_bytes()", int_1.to_bytes(1, "big"))
print(f"int_1.from_bytes()", int.from_bytes(b"\x00\x00\x00\x01", "big"))
# int_1.to_bytes(1, "big")
