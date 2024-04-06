s = "IV"

ds = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
d1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
i = 0
num = 0

while i < len(s):
    if (
        i + 1 < len(s) and s[i : i + 2] in ds
    ):  # check if the next two characters are in the dictionary
        num += ds[s[i : i + 2]]  # add the value of the two characters to the number
        i += 2
    else:
        num += d1[s[i]]
        i += 1


print(num)


roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}
while i < len(s):
    # 檢查是否是特殊組合
    if i + 1 < len(s) and s[i : i + 2] in roman_dict:
        num += roman_dict[s[i : i + 2]]
        i += 2  # 跳過下一個字符
    else:
        num += roman_dict[s[i]]
        i += 1
