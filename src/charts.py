import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/charts", exist_ok=True)

mat = pd.read_csv("data/debt_maturities.csv")
mat = mat[mat["carrying_value"] > 0]

plt.figure(figsize=(8, 4))
plt.bar(mat["maturity"], mat["carrying_value"], color="#003366")
plt.title("ITV Debt Maturity Profile (at 31 Dec 2025)")
plt.xlabel("Maturity")
plt.ylabel("£m")
plt.tight_layout()
plt.savefig("outputs/charts/debt_maturity.png", dpi=150)
plt.close()

print("Chart saved to outputs/charts/debt_maturity.png")