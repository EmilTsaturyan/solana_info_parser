#📊 Solana Validator Stats & Uptime Collector
This repository contains Python scripts for collecting and storing Solana validator performance data and uptime history into your local database.

#📂 Files Overview
1.get_validator_stat.py
I.Collects and stores validator APY and stake data per epoch from solanacompass.com.
II.Fetches all validators from the local repository.
III.Sends requests to https://solanacompass.com/stats?validator=<vote_address>.
IV.Parses epochCharts and epochTrends for:
Epoch number
Activated stake
APY (Annual Percentage Yield)
V.Saves multiple records at once using validator_stat_repository.

2.get_validator_uptime.py
I.Fetches and stores validator uptime data from stakewiz.com.
II.Sends requests to https://api.stakewiz.com/validator_delinquencies/<vote_address>.
III.Parses:
Date of the record
Delinquent (offline) minutes

IV.Stores daily uptime statistics using validator_uptime_repository.
