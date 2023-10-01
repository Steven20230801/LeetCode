string = "Hello World test"
string_b = str("Hello World test")
print(id(string))
print(id(string_b))
print(string == string_b)
"單行使用雙引號/單引號皆可"
"單行使用雙引號/單引號皆可"

"""
多行使用三個雙引號
1
2
3
"""

"""str is immutable"""

# try except
try:
    string[0] = "h"  # TypeError: 'str' object does not support item assignment
except TypeError as e:
    print(e)
except Exception as e:
    print(e)

print(string)

# string basic
print(f"string[0]", string[0])
print(f"string[0:5]", string[0:5])
print(f"string[0:5:2]", string[0:5:2])
print(f"string[-1]", string[-1])

# +
print(f"string + string", string + "123456")
# *
print(f"string * 3", string * 3)
# in
print(f"'H' in string", "H" in string)
# fstring / format
string_with_variable = "prtin string_variable: {string_variable}"
print(string_with_variable.format(string_variable="Hello World"))
print(f"string_with_variable: {string_with_variable}")
# format
today = "2021-01-01"
print("today is {}".format(today))
print("today is {today}".format(today=today))
print("today is {today}".format(**{"today": today}))
print("today is {today}".format_map({"today": today}))
# %

# string method
print(f"string.upper()", string.upper())
print(f"string.lower()", string.lower())
print(f"string.capitalize()", string.capitalize())
print(f"string.title()", string.title())
print(f"string.swapcase()", string.swapcase())
print(f"string.strip()", string.strip())
print(f"string.lstrip()", string.lstrip())
print(f"string.rstrip()", string.rstrip())
print(f"string.replace('o', '0')", string.replace("o", "0"))
print(f"string.split(' ')", string.split(" "))
print(f"string.splitlines()", string.splitlines())
print(f"string.join(' ')", string.join(" "))
print(f"string.join(['1', '2', '3'])", string.join(["1", "2", "3"]))
print(f"string.startswith('H')", string.startswith("H"))
print(f"string.endswith('d')", string.endswith("d"))
print(f"string.find('W')", string.find("W"))
print(f"string.rfind('o')", string.rfind("o"))
print(f"string.index('W')", string.index("W"))
print(f"string.rindex('o')", string.rindex("o"))
print(f"string.count('o')", string.count("o"))
print(f"string.isalnum()", string.isalnum())
print(f"string.isalpha()", string.isalpha())
print(f"string.isdecimal()", string.isdecimal())
print(f"string.isdigit()", string.isdigit())
print(f"string.isnumeric()", string.isnumeric())
print(f"string.islower()", string.islower())
print(f"string.isupper()", string.isupper())
print(f"string.isspace()", string.isspace())
print(f"string.istitle()", string.istitle())
print(f"string.isidentifier()", string.isidentifier())
print(f"string.isprintable()", string.isprintable())
print(f"string.isascii()", string.isascii())
print(f"string.encode()", string.encode())
print(f"string.format()", string.format())
print(f"string.format_map({{}})", string.format_map({}))
