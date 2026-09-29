"""
charts.py
Regenerates the three chart PNGs.
Chart 1 reads data/debt_maturities.csv; charts 2 and 3 read outputs/model_outputs.csv,
which is exported from the Export sheet of the Excel model.
"""
import os

import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/charts", exist_ok=True)

# Chart 1: debt maturity profile
mat = pd.read_csv("data/debt_maturities.csv")
mat = mat[mat["carrying_value"] > 0]

plt.figure(figsize=(8, 4))
plt.bar(mat["maturity"], mat["carrying_value"])
plt.title("ITV Debt Maturity Profile (at 31 Dec 2025)")
plt.xlabel("Maturity")
plt.ylabel("£m")
plt.tight_layout()
plt.savefig("outputs/charts/debt_maturity.png", dpi=150)
plt.close()

# Chart 2: covenant leverage
model = pd.read_csv("outputs/model_outputs.csv")
limit = model["CovenantLimit"].iloc[0]

plt.figure(figsize=(8, 4))
plt.plot(model["Year"], model["CovenantLeverage_Base"], marker="o", label="Covenant leverage")
plt.axhline(y=limit, linestyle="--", color="grey", label=f"Covenant limit {limit:.1f}x")
plt.title("ITV Covenant Leverage (Net Debt / Covenant Adjusted EBITDA)")
plt.xlabel("Year")
plt.ylabel("x")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/charts/leverage_trend.png", dpi=150)
plt.close()

# Chart 3: net debt under scenarios
plt.figure(figsize=(8, 4))
plt.plot(model["Year"], model["NetDebt_Base"], marker="o", label="Base")
plt.plot(model["Year"], model["NetDebt_Downside"], marker="s", label="Downside")
plt.plot(model["Year"], model["NetDebt_Upside"], marker="^", label="Upside")
plt.axhline(y=0, linewidth=0.5, color="black")
plt.title("ITV Projected Net Debt Under Scenarios")
plt.xlabel("Year")
plt.ylabel("Net debt (£m)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/charts/scenarios.png", dpi=150)
plt.close()

print("All 3 charts saved to outputs/charts/")
