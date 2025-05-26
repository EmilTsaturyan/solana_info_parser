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

## 🧩 Project Structure

```
.
├── get_validator_stat.py
├── get_validator_uptime.py
├── repositories/
│   ├── validator_repository.py
│   ├── validator_stat_repository.py
│   └── validator_uptime_repository.py
└── db/
    └── models.py
```

---

## ⚙️ Requirements

- Python 3.7+
- Dependencies:
  - `requests`
  - Local database access (via repository classes)
  - Defined ORM models in `db.models`

Install requirements:

```bash
pip install requests
```

---

## ▶️ Usage

To collect **validator stats** (APY and stake data):

```bash
python get_validator_stat.py
```

To collect **uptime/delinquency data**:

```bash
python get_validator_uptime.py
```

---

## 🧠 Notes

- The repository classes (`validator_repository`, etc.) and database models (`ValidatorStat`) are expected to be implemented in your project.
- Make sure your database is set up and connected properly before running these scripts.
- Uses batching (`add_many_validator_stats`) for performance when storing large datasets.

---

## 🛠️ Future Improvements

- Add CLI arguments to select date ranges or specific validators
- Include logging and retry logic for failed API calls
- Add unit tests and validation logic

---

Made with 💻 for Solana data hunters.  
**— Emil**
