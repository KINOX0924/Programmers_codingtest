n = int(input())
right_triangle = ""

for i in range(1 , n + 1) :
    right_triangle += "*" * i
    right_triangle += "\n"

print(right_triangle)