# for
# for variable in sequence:
#     statement(s)

sequence = [1, 2, 3, 4, 5]
for variable in sequence:
    print(variable)

# range
# range(stop)
# range(start, stop[, step])

for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(1, 5, 2):
    print(i)

# break
# break is used to terminate the loop entirely. The execution continues at the statement immediately after the loop.
for i in range(5):
    if i == 3:
        break
    print(i)
# continue
# continue is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
for i in range(5):
    if i == 3:
        continue
    print(i)

# while
# while expression:
#     statement(s)
i = 0
while i < 5:  # while True:
    print(i)
    i += 1
