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
- Used for: 2026H1 financials, latest debt carrying values, latest net debt, updated liquidity, updated guidance

### FY2025 Full Year Results RNS
- Exact title: ITV plc Full-Year results for the twelve months ended 31 December 2025
- Publisher: ITV plc
- Published: 5 March 2026
- URL: https://www.itvplc.com/investors/results-reports-and-presentations/
- Retrieved: 15 September 2026
- Used for: FY2025 reported financials cross-check, FY2026 guidance

### Sky M&E Transaction RNS
- Exact title: "Sale of ITV M&E Business to Sky for up to £1.6 billion - Unlocking Significant Value for Shareholders"
- RNS Number: 0606L
- Publisher: ITV plc
- Published: 6 July 2026, 07:00
- URL: https://www.itvplc.com/investors/results-reports-and-presentations/
- Retrieved: 15 September 2026
- Used for: Sky transaction terms (total consideration up to £1.6bn, £200m Love Productions contribution, contingent consideration, expected completion, net cash return)

## Figure-to-source map

### `data/itv_financials.csv`
| Column | FY2024 | FY2025 | 2026H1 |
|---|---|---|---|
| revenue | FY2025 AR p.126 | FY2025 AR p.126 | H1 2026 p.26 |
| adjusted_ebita | FY2025 AR p.36 | FY2025 AR p.36 | H1 2026 p.26 |
| adjusted_ebitda | FY2025 AR p.35 | FY2025 AR p.35 | H1 2026 p.17 |
| net_income | FY2025 AR p.126 | FY2025 AR p.126 | H1 2026 p.26 |
| finance_costs | FY2025 AR p.126 | FY2025 AR p.126 | H1 2026 p.26 |
| cash | FY2025 AR p.127 | FY2025 AR p.127 | H1 2026 p.28 |
| gross_debt | FY2025 AR p.127 | FY2025 AR p.127 | H1 2026 p.28 |
| lease_liabilities | FY2025 AR p.175 | FY2025 AR p.175 | H1 2026 p.28 |
| operating_cash_flow | FY2025 AR p.130 | FY2025 AR p.130 | H1 2026 p.31 |
| capex | FY2025 AR p.130 | FY2025 AR p.130 | H1 2026 p.31 |
| dividends | FY2025 AR p.130 | FY2025 AR p.130 | H1 2026 p.31 |

### `data/debt_maturities.csv`
Source: FY2025 AR Note 4.2 (p.165).

### `data/liquidity_profile.csv`
- 31 Dec 2025 rows: FY2025 AR Note 4.1 (p.165)
- 30 Jun 2026 rows: H1 2026 Interim Report Note 4.1 (p.40)
- Reconciliation check: cash + undrawn facilities = £1,327m (31 Dec 2025) and £1,304m (30 Jun 2026), both tying to ITV's reported total liquidity. At 31 Dec 2025 this requires the £300m term loan to count as a committed, undrawn facility (it is contractually in place, drawable from 26 June 2026) and the £200m bilateral loan to show £75m drawn / £125m undrawn -- both now reflected in the CSV.

## Sky transaction terms (cross-checked against the RNS)

Total consideration up to £1.6bn: £1.2bn initial cash consideration + £200m Love Productions contribution (non-cash) + up to £200m contingent consideration. Net cash return to shareholders ~£950m (H1 2026 Interim Results), used first to de-lever ITV Studios post-completion to approximately 1.5x. Deal does not require ITV shareholder approval under UK Listing Rules; subject to CMA/regulatory review.

## Basis of EBITA / EBITDA figures

Two bases are used and are labelled separately:

- **Headline basis (ITV reported):** Group adjusted EBITA of 542 (FY2024) and 534 (FY2025). Used in `adjusted_ebita` in `itv_financials.csv`.
- **Covenant basis:** EBITA of 526 / 533 feeding covenant adjusted EBITDA of 548 / 555 (and 555 for H1 2026 rolling). Used in the Excel model's `Historicals` sheet and in `adjusted_ebitda` in `itv_financials.csv`.

ITV's own reported net debt / adjusted EBITDA (0.7x FY2024, 1.0x FY2025, 1.0x H1 2026) uses the headline basis, so it will not match covenant-basis leverage.

## Key figures

### Debt (carrying value at 31 Dec 2025)
- €360m Eurobond (remaining of €600m): £313m
- €500m Eurobond: £436m
- £300m term loan: £0 (available from 26 June 2026; undrawn at 30 June 2026)
- Other loans: £16m
- Total loans and facilities: £765m

### Credit metrics
- Net debt FY2025: £566m
- Reported net debt / adjusted EBITDA FY2025: 1.0x
- Covenant net debt / adjusted EBITDA FY2025: 0.9x
- Covenant terms: leverage < 3.5x, interest cover > 3.0x

### Liquidity
- At 31 Dec 2025: £1,327m
- At 30 Jun 2026: £1,304m

### FY2026 guidance
- Capex: ~£60m
- Profit-to-cash conversion: ~80% medium term
- Adjusted financing costs: ~£40m
- Adjusted effective tax rate: ~27% medium term
- Dividend: 1.7p interim, at least 5.0p full year

## Net debt reconciliation

### FY2024
Reported: £431m
Calculated: £733m + £105m - £427m = £411m
Difference: £20m currency swap component (liability)

### FY2025
Reported: £566m
Calculated: £765m + £111m - £302m = £574m
Difference: £8m currency swap component (asset)

### H1 2026
Reported: £652m
Calculated: £807m + £109m - £264m = £652m
Difference: none

### Approach
Use reported net debt as anchor. Model calculates `net_debt = gross_debt + lease_liabilities - cash`. Swap difference disclosed in Assumptions.

## Model architecture notes

### Time axis
FY2024A -> FY2025A -> H1 2026A -> FY2026H2E -> FY2026E -> FY2027E -> FY2028E. H1 2026A is the opening actual for the forecast, so FY2026E net debt moves only by H2 flows.

### Covenant adjustments
Covenant adjusted EBITDA = EBITA + Depreciation - ROU depreciation - Interest on lease liabilities

### Financing trigger
Analyst-defined cash-floor trigger: projected cash < £250m. ITV's actual policy is cash + undrawn committed facilities.

### Scenario structure
Base, Downside, Upside, Liquidity Stress. Base links to the Forecast; the other three are calculated in a scenario engine that reconciles to the Forecast in the Base case.

### Transaction-adjusted case
Sky M&E sale excluded from the standalone base; shown separately as a strategic overlay.

### Export-to-Python flow
Excel -> Export sheet -> model_outputs.csv -> charts.py -> PNG charts
