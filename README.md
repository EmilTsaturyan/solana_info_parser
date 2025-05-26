# 📊 Solana Validator Stats & Uptime Collector

This repository contains Python scripts for collecting and storing **Solana validator performance data** and **uptime history** into your local database.

## 📂 Files Overview

### `get_validator_stat.py`

Collects and stores validator **APY** and **stake data per epoch** from [solanacompass.com](https://solanacompass.com).

- Fetches all validators from the local repository.
- Sends requests to `https://solanacompass.com/stats?validator=<vote_address>`.
- Parses `epochCharts` and `epochTrends` for:
  - Epoch number
  - Activated stake
  - APY (Annual Percentage Yield)
- Saves multiple records at once using `validator_stat_repository`.

### `get_validator_uptime.py`

Fetches and stores validator **uptime** data from [stakewiz.com](https://stakewiz.com).

- Sends requests to `https://api.stakewiz.com/validator_delinquencies/<vote_address>`.
- Parses:
  - Date of the record
  - Delinquent (offline) minutes
- Stores daily uptime statistics using `validator_uptime_repository`.

---
