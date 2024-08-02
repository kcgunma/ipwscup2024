# [ipwscup2024](https://www.iwsec.org/pws/ipws2024/)

## How to play

### Anonymization

### Attack

## Programs & Data
- data/A.csv
  - Original data for creation of synthetic data. 
- data/sampleBi.csv
  - A sample data of distribution data Bi.
- tools/genHash.py
  - Calculate the hash value (SHA-256) of distribution data Bi.
  - Integrity check against the pre-published hash value of Bi.
  - Argument : filename_of_Bi
- tools/maketest.py
  - Read Bi and create data for attacks.
  - For input B00.csv, output B00s.csv, B00a.csv, B00b.csv and B00ans.csv.
  - B00s.csv : 50 lines randomly selected from B00.csv.
  - B00a.csv : Data in the basic attributes extracted from B00s.csv.
  - B00b.csv : Movie ratings data from B00s.csv modified by random shuffling and partially redacted.
  - B00ans.csv : Answer data showing how B00b.csv was shuffled and where it was redacted.
- tools/split.py
  - Output subset data files Bi_0.csv, Bi_1.csv, ... , Bi_9.csv from Bi.
  - They are the original data of anonymized data Ci_0, Ci_1, ... , Ci_9. 
