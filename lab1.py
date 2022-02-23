data = [104, 2262, 3376, 408, 208, 27, 823, 30, 584,
        1176, 558, 550, 90, 601, 287, 176, 569, 492,
        24, 47, 231, 1113, 2123, 1231, 226, 789,
        865, 223, 1240, 729, 32, 157, 11, 605, 741,
        377, 52, 782, 73, 138, 283, 251, 2930, 99,
        284, 965, 118, 751, 56, 324, 1223, 5, 1675,
        902, 735, 882, 111, 2027, 219, 1714, 615,
        41, 19, 561, 650, 316, 1083, 813, 622, 1682,
        1940, 312, 671, 245, 19, 243, 1883, 593,
        1545, 605, 811, 1468, 791, 16, 497, 296,
        410, 137, 621, 16, 1287, 881, 76, 990, 106,
        347, 404, 109, 657, 510]

avg = sum(data) / len(data)
print(f'Середній наробіток до відмови Tср: {avg}')
γ = 0.57
t1 = 1858
t2 = 3288
k = 10
h = max(data) / k
intervals = []
f = []
P = [1]
for i in range(1, k + 1):
    intervals.append([h * (i - 1), h * i])
for [minimum, maximum] in intervals:
    f.append(len(list(filter(lambda x: minimum <= x <= maximum, data))) / 100 / h)

counter = 0
for el in f:
    counter += el * h
    P.append(1 - counter)

for i in range(len(intervals)):
    if P[i] >= γ > P[i + 1]:
        d = (P[i + 1] - γ) / (P[i + 1] - P[i])
        print(f'γ-відсотковий наробіток навідмову Tγ: {intervals[i][1] - h * d} при γ: {γ} ')
c1 = 0
for i in range(k):
    if t1 > intervals[i][1]:
        c1 += f[i] * h
    else:
        print(f'Ймовірність безвідмовної роботина час {t1} годин, складає {1 - c1 - f[i] * (t1 - intervals[i][0])}')
        break
c2 = 0
for i in range(k):
    if (t2 > intervals[i][1]):
        c2 += f[i] * h
    else:
        print(f'Інтенсивність відмов на час {t2} годин cкладає {f[i] / (1 - c2 - f[i] * (t2 - intervals[i][0]))}')
        break