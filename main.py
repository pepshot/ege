with open('27-B_demo.txt') as f:
    text = f.readlines()
    values = []
    for i in text[1::]:
        v1, v2 = map(int, i.split())
        values.append((v1, v2))
min_vichet_val = 10 ** 10
max_sum = 0
for i in values:
    v1, v2 = i
    max_sum += max(v1, v2)
    if abs(v1 - v2) < min_vichet_val and abs(v1 - v2) % 3 != 0:
        min_vichet_val = abs(v1 - v2)
if max_sum % 3 == 0:
    print(max_sum - min_vichet_val)
else:
    print(max_sum)
#A) 127127
#B) 399762080