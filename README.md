# ITV plc — Capital Structure & Financing Options Analysis

**Analysis date: 15 September 2026**

## Objective

Assess whether ITV plc requires additional external financing over FY2026–FY2028, and evaluate the relative merits of debt refinancing, equity issuance, dividend reduction, asset disposal and maintaining the existing capital structure.

## Key findings

- ITV's only material near-term maturity, the €360m remaining Eurobond due September 2026, is addressed by a £300m term loan facility secured in the first half of 2025, with the balance funded from existing liquidity.
- Under base, downside and upside scenarios, no new external financing beyond ITV's existing committed facilities is required. Cash generation covers distributions and continues to reduce net debt.
- The model-derived financing trigger — projected cash below the £250m minimum liquidity floor — is not breached in the base case unless EBITA margin falls to approximately 12%, roughly 300bps below FY2025 levels and just under ITV's guided 13–15% range.
- Dividend reduction provides the most credible discretionary liquidity lever under stress. Equity issuance is not justified under the base case given dilution of ~10% and substantial existing headroom. Even the Liquidity Stress scenario stays within committed liquidity.
- The announced M&E sale to Sky (expected completion H2 2027) is treated as a separate transaction-adjusted case, not folded into the standalone base forecast.

## Methodology

The analysis is built from primary-source investor materials:

- FY2025 Annual Report and Accounts (published 23 March 2026)
- H1 2026 Interim Results (published 31 July 2026)
- FY2025 Full Year Results RNS (published 5 March 2026)
- Sky M&E transaction RNS (published 6 July 2026)

Information cutoff: 15 September 2026. No materials published after this date are used.

The Excel model is the primary analytical product. It covers:

1. Historical financials (FY2024A, FY2025A, H1 2026A)
2. Forecast (FY2026E, FY2027E, FY2028E)
3. Cash bridge and debt roll-forward
4. Covenant-adjusted EBITDA and covenant net debt
5. Debt maturity schedule and liquidity reconciliation
6. Five financing options
7. Base / Downside / Upside / Liquidity Stress scenarios
8. EBITA margin sensitivity with defined financing trigger

The model determines the recommendation. No conclusion is predetermined.

## Repository structure

```text
itv-capital-structure/
├── data/
│   ├── itv_financials.csv
│   ├── debt_maturities.csv
│   ├── liquidity_profile.csv
│   └── SOURCES.md
├── src/
│   ├── charts.py
│   ├── metrics.py
│   └── data_check.py
├── outputs/
│   ├── itv_model.xlsx
│   ├── model_outputs.csv
│   ├── charts/
│   │   ├── debt_maturity.png
│   │   ├── leverage_trend.png
│   │   └── scenarios.png
│   └── memo/
│       └── itv_financing_memo.pdf
└── README.md
```

## Python scripts

- `src/charts.py` — regenerates the three chart PNGs from `outputs/model_outputs.csv`
- `src/metrics.py` — calculates historical credit metrics from `data/itv_financials.csv`; reports covenant-basis leverage alongside ITV's own reported leverage figures rather than conflating the two
- `src/data_check.py` — reconciles model-calculated net debt against ITV's reported figures

All scripts read from CSV or Excel exports. No forecast values are hardcoded in Python.

## How to run

```text
pip install -r requirements.txt
python src/metrics.py
python src/data_check.py
python src/charts.py
```

Charts regenerate from `outputs/model_outputs.csv`, which is exported from the Excel model.

## Data sources

See [data/SOURCES.md](data/SOURCES.md) for full source log, figure-to-source mapping, covenant adjustment definitions, and model architecture notes.

## Net debt reconciliation

- FY2024: Reported £431m. Calculated £733m gross debt + £105m leases − £427m cash = £411m. £20m difference = currency swap component.
- FY2025: Reported £566m. Calculated £765m + £111m − £302m = £574m. £8m difference = currency swap component.
- H1 2026: Reported £652m. Calculated £807m + £109m − £264m = £652m. No difference.

## Positioning

This is an independently-built finance work sample demonstrating:

- Financial statement interpretation and primary-source data extraction
- Debt and liquidity analysis
- Forecast modelling with a proper cash bridge
- Covenant metric reconstruction (adjusted EBITDA, covenant net debt)
- Scenario and sensitivity analysis
- Evidence-based recommendation without predetermination

Built alongside a Computer Science degree at Newcastle University.

## License

No license. Independent student project, not investment advice.
