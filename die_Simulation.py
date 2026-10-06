import numpy as np
import matplotlib.pyplot as plt

rolls = np.random.randint(1, 7, size=1000)

print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)

print("\nFace  Count  Empirical P     Theoretical P")

print(1, "    ", counts[0], "   ", counts[0] / 1000, "    ", 1 / 6)
print(2, "    ", counts[1], "   ", counts[1] / 1000, "    ", 1 / 6)
print(3, "    ", counts[2], "   ", counts[2] / 1000, "    ", 1 / 6)
print(4, "    ", counts[3], "   ", counts[3] / 1000, "    ", 1 / 6)
print(5, "    ", counts[4], "   ", counts[4] / 1000, "    ", 1 / 6)
print(6, "    ", counts[5], "   ", counts[5] / 1000, "    ", 1 / 6)

plt.hist(rolls, bins=6)
plt.title("Die Rolls Distribution")
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.savefig("die_rolls.png")
plt.show()
print("\nSaved die_rolls.png")