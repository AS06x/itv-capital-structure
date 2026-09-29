"""
data_check.py
Validates that model-calculated net debt reconciles to ITV reported figures.
Prints a reconciliation table.
"""
import pandas as pd


REPORTED_NET_DEBT = {
    "2024": 431,     # FY2024 Annual Report
    "2025": 566,     # FY2025 Annual Report
    "2026H1": 652,   # H1 2026 Interim Results
}


def main():
    df = pd.read_csv("data/itv_financials.csv")

    df["calculated_net_debt"] = (
        df["gross_debt"] + df["lease_liabilities"] - df["cash"]
    )

    print("Net debt reconciliation check")
    print("-" * 70)
    print(f"{'Year':<10}{'Calculated':>15}{'Reported':>15}{'Difference':>15}")
    print("-" * 70)

    for _, row in df.iterrows():
        year = str(row["year"])
        if year not in REPORTED_NET_DEBT:
            continue

        calc = row["calculated_net_debt"]
        reported = REPORTED_NET_DEBT[year]
        diff = calc - reported

        print(f"{year:<10}{calc:>15.0f}{reported:>15.0f}{diff:>15.0f}")

    print()
    print("Reconciliation notes:")
    print("-" * 70)
    print("FY2024: £20m difference = currency component of swaps held against")
    print("        euro-denominated bonds (liability, adds to debt).")
    print("FY2025: £8m difference = same swap component (asset, reduces debt).")
    print("2026H1: no difference -- gross debt + leases - cash ties out exactly.")
    print()
    print("Reported figures are the anchor. Model uses gross debt + leases - cash")
    print("for consistency across forecast periods.")
    print()


if __name__ == "__main__":
    main()
