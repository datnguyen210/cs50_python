import csv
from collections import Counter

with open("favorite-languages.csv") as file:
    reader = csv.DictReader(file)
    counts = Counter()
    for row in reader:
        favorite = row["language"]
        counts[favorite] += 1

for favorite, count in counts.most_common():
    print(f"{favorite}: {count}")