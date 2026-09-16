# Data Sources

## Information cutoff
Absolute: 15 September 2026. No materials published after this date.

## Analysis date
15 September 2026

## Primary sources

### Annual Report and Accounts 2025
- Exact title: ITV plc Annual Report and Accounts 2025
- Publisher: ITV plc
- Published: 23 March 2026
- URL: https://www.itvplc.com/investors/results-reports-and-presentations/
- Retrieved: 15 September 2026
- Used for: FY2024 and FY2025 historical financials, debt maturity profile, facility structure, covenant terms

### H1 2026 Interim Results
- Exact title: Half year results for the period ended 30 June 2026
- Publisher: ITV plc
- Published: 31 July 2026
- URL: https://www.itvplc.com/investors/results-reports-and-presentations/
- Retrieved: 15 September 2026
- Used for: 2026H1 financials row, latest debt carrying values, latest net debt position, updated liquidity, updated guidance

### FY2025 Full Year Results RNS
- Exact title: ITV plc Full-Year results for the twelve months ended 31 December 2025
- Publisher: ITV plc
- Published: 5 March 2026
- URL: https://www.itvplc.com/investors/results-reports-and-presentations/
- Retrieved: 15 September 2026
- Used for: FY2025 reported financials cross-check, FY2026 guidance

## Figure-to-source map

### `data/itv_financials.csv`
| Column | FY2024 | FY2025 | 2026H1 |
|---|---|---|---|
| revenue | FY2025 AR p.126 | FY2025 AR p.126 | H1 2026 report p.26 |
| adjusted_ebita | FY2025 AR p.36 | FY2025 AR p.36 | H1 2026 report p.26 |
| adjusted_ebitda | FY2025 AR p.35 | FY2025 AR p.35 | H1 2026 report p.17 (rolling 12m) |
| net_income | FY2025 AR p.126 | FY2025 AR p.126 | H1 2026 report p.26 |
| finance_costs | FY2025 AR p.126 | FY2025 AR p.126 | H1 2026 report p.26 |
| cash | FY2025 AR p.127 | FY2025 AR p.127 | H1 2026 report p.28 |
| gross_debt | FY2025 AR p.127 | FY2025 AR p.127 | H1 2026 report p.28 |
| lease_liabilities | FY2025 AR p.175 | FY2025 AR p.175 | H1 2026 report p.28 |
| operating_cash_flow | FY2025 AR p.130 | FY2025 AR p.130 | H1 2026 report p.31 |
| capex | FY2025 AR p.130 | FY2025 AR p.130 | H1 2026 report p.31 |
| dividends | FY2025 AR p.130 | FY2025 AR p.130 | H1 2026 report p.31 |

### `data/debt_maturities.csv`
All from FY2025 AR Note 4.2 (p.165). Carrying values match the "Fair value versus book value" table.

### `data/liquidity_profile.csv`
Rows dated 31 Dec 2025: FY2025 AR Note 4.1 (p.165).
Rows dated 30 Jun 2026: H1 2026 Interim Report Note 4.1 (p.40).

## Key figures

### Debt (carrying value at 31 Dec 2025)
- €360m Eurobond (remaining of €600m): £313m
- €500m Eurobond: £436m
- £300m term loan: £0 at 31 Dec 2025 (drawn 26 June 2026)
- Other loans: £16m
- Total loans and facilities: £765m

### Credit metrics
- Net debt FY2025: £566m
- Reported net debt / adjusted EBITDA FY2025: 1.0x
- Covenant net debt / adjusted EBITDA FY2025: 0.9x
- Covenant terms: leverage < 3.5x, interest cover > 3.0x
- Tested: 30 June and 31 December each year

### Liquidity
- At 31 Dec 2025: £1,327m total (per Annual Report Note 4.1)
- At 30 Jun 2026: £1,304m total (per H1 2026 report)

### FY2026 guidance
- Capex: ~£60m
- Profit-to-cash conversion: ~80% medium term
- Adjusted financing costs: ~£40m
- Adjusted effective tax rate: ~27% medium term
- Dividend: 1.7p interim, at least 5.0p full year (~£190m)

## Net debt reconciliation

### FY2024
- Reported net debt: £431m
- Calculated: £733m gross debt + £105m leases − £427m cash = £411m
- Difference: £20m = currency component of swaps held against euro-denominated bonds (a liability in 2024, adds to debt)
- Check: £411m + £20m = £431m ✓ Ties to reported

### FY2025
- Reported net debt: £566m
- Calculated: £765m gross debt + £111m leases − £302m cash = £574m
- Difference: £8m = currency component of swaps held against euro-denominated bonds (an asset in 2025, reduces debt)
- Check: £574m − £8m = £566m ✓ Ties to reported

### Reconciliation approach for the model
Use reported net debt as the anchor. The currency swap component is a non-cash FX translation item.
For the forecast model:
`net_debt = gross_debt + lease_liabilities − cash`
Disclose the difference between this and reported net debt in the Assumptions sheet.

