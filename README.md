# [ipwscup2024](https://www.iwsec.org/pws/ipws2024/)

## How to play

### Anonymization

### Attack

## Programs & Data
- sample_data/sampleBi.csv
  - A sample data of distribution data Bi.
- tools/genHash.py
  - Calculate the hash value (SHA-256) of distribution data Bi.
  - Integrity check against the pre-published hash value of Bi.
  - Argument : filename_of_Bi
- tools/split.py
  - Output subset data files Bi_0.csv, Bi_1.csv, ... , Bi_9.csv from Bi.
  - They are the original data of anonymized data Ci_0, Ci_1, ... , Ci_9. 
