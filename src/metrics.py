"""
metrics.py
Calculates historical credit metrics from ITV financials CSV.
Prints a summary table for verification.

Note on EBITDA basis: this CSV's adjusted_ebitda column (548/555/555) is on
a COVENANT basis -- it matches the Excel model's "Covenant adjusted EBITDA"
row exactly. It is NOT the same figure behind ITV's own separately-disclosed
reported net debt / adjusted EBITDA (1.0x FY2025, 0.7x FY2024, 1.0x H1 2026).
The two use different EBITDA definitions, so this script labels its own
output "covenant_leverage_approx" rather than calling it "reported leverage"
and prints ITV's actual reported figures alongside it for comparison.
"""
import pandas as pd

# ITV's own reported net debt / adjusted EBITDA, stated directly in its
# results -- not recomputed here, since this CSV doesn't carry the headline
# EBITDA figure needed to reproduce it.
ITV_REPORTED_LEVERAGE = {
    "2024": 0.7,
    "2025": 1.0,
    "2026H1": 1.0,
}


def main():
    df = pd.read_csv("data/itv_financials.csv")

    # Net debt = gross debt + lease liabilities - cash
    df["net_debt"] = df["gross_debt"] + df["lease_liabilities"] - df["cash"]

    # Covenant-basis leverage (see note above -- not ITV's headline figure)
    df["covenant_leverage_approx"] = df["net_debt"] / df["adjusted_ebitda"]

    # Dividend cover (adjusted EBITA / dividends) -- adjusted_ebita in this
    # CSV is on ITV's headline basis, so this ratio is fine as-is
    df["dividend_cover"] = df["adjusted_ebita"] / df["dividends"]

    print("Historical credit metrics")
    print("-" * 80)

    cols = [
        "year",
        "revenue",
        "adjusted_ebita",
        "adjusted_ebitda",
        "net_debt",
        "covenant_leverage_approx",
        "dividend_cover",
    ]

    print(df[cols].to_string(index=False))
    print()
    print("dividend_cover for 2026H1 compares half-year EBITA with the FY2025 final")
    print("dividend paid in H1, so it is not comparable with the full-year figures.")
    print()
    print("covenant_leverage_approx uses this CSV's adjusted_ebitda column,")
    print("which is on a covenant basis and will not match ITV's own")
    print("reported net debt / adjusted EBITDA disclosure. For reference,")
    print("ITV's own reported figures:")
    for year, lev in ITV_REPORTED_LEVERAGE.items():
        print(f"  {year}: {lev}x")
    print()

    row_2025 = df[df["year"].astype(str) == "2025"]  # year column is text ("2026H1")
    if not row_2025.empty:
        nd = row_2025["net_debt"].iloc[0]
        print(f"FY2025 net debt: £{nd:.0f}m")
        print("Note: 2026H1 adjusted EBITDA is a rolling 12-month figure.")


if __name__ == "__main__":
    main()
