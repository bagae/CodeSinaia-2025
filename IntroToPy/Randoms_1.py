import random
import numpy as np
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
# Read input parameters from the console
count = 100 # int(input("Number of values?> "))
min_value = 10 # int(input("Minimum value?> "))
max_value = 200 # int(input("Maximum value?> "))
print(f"Generating {count} randoms in the range [{min_value}, {max_value}]")

# Generate count values in the range [min_value, max_value] and store them in a the values map
# randoms_map - associates each random value to the zero-based index/iteration where it was generated
# <key=random_value, value=[index1, index2, index3, ...]> 
randoms_map = {}
vec=[]
for i in range(0, count):
    r = random.randint(min_value, max_value)
    vec.append(r)
    #r = int(min_value + i) if i < 9 * count/10 else min_value + 1000 + i
    if r not in randoms_map:
        randoms_map[r] = []
    randoms_map[r].append(i)
Max_value=0
Min_value=max_value+1
# Write a text file "randoms_db.txt" with each random on a line, its value followed by the indexes where it occurred
with open("IntroToPy/randoms_dbceva.txt", "w") as data_file:
    for r in randoms_map.keys():
        data_file.write(f"{r} {randoms_map[r]}\n")
        if r>Max_value: Max_value=r
        if r<Min_value: Min_value=r
        print(r)
        
        
number_of_randoms = len(randoms_map.keys())

print(number_of_randoms)
print(Max_value)
print(Min_value)
print(np.mean(vec))
print(np.median(vec))
print(statistics.stdev(vec))



topN = 5  
top_randoms = sorted(randoms_map.items(), key=lambda item: len(item[1]), reverse=True)[:topN]
print(f"Top {topN} cele mai frecvent generate valori:")
for value, occurrences in top_randoms:
    print(f"Valoare: {value}, Frecvență: {len(occurrences)}, Indici: {occurrences}")

plt.figure(figsize=(10,5))
values = list(randoms_map.keys())
counts = [len(randoms_map[v]) for v in values]
plt.bar(values, counts)
plt.xlabel("Valoare generată")
plt.ylabel("Număr de apariții")
plt.title("Frecvența fiecărei valori generate")
plt.show()

# 6. Plot: iterație vs valoare generată
plt.figure(figsize=(10,5))
iteration_vals = [0]*count
for val, idxs in randoms_map.items():
    for idx in idxs:
        iteration_vals[idx] = val
plt.plot(range(count), iteration_vals, marker='o', linestyle='-', markersize=3)
plt.xlabel("Iterație")
plt.ylabel("Valoare generată")
plt.title("Valoarea generată la fiecare iterație")
plt.show()

# 7. Boxplot: quartilele valorilor generate
plt.figure(figsize=(8,5))
sns.boxplot(x=vec)
plt.xlabel("Valori generate")
plt.title("Boxplot pentru valorile generate (quartile)")
plt.show()


#8
intervale = np.linspace(min_value, max_value, 11)
labels = [f"{int(intervale[i])}-{int(intervale[i+1]-1)}" for i in range(10)]
bins = np.digitize(vec, intervale) - 1  # bins: 0..9

media = []
stddev = []
quartiles = []

for i in range(10):
    vals = [v for v, b in zip(vec, bins) if b == i]
    if vals:
        media.append(np.mean(vals))
        stddev.append(np.std(vals))
        quartiles.append(np.percentile(vals, [25, 50, 75]))
    else:
        media.append(0)
        stddev.append(0)
        quartiles.append([0,0,0])
plt.figure(figsize=(12,6))
plt.bar(labels, media, alpha=0.6, label='Media')
plt.plot(labels, stddev, color='red', marker='o', label='StdDev')
for i, q in enumerate(quartiles):
    plt.scatter([labels[i]]*3, q, color='green', marker='x', label='Quartile' if i==0 else "")
plt.xlabel("Sub-interval")
plt.ylabel("Valori statistice")
plt.title("Statistici pe sub-intervale")
plt.legend()
plt.show()