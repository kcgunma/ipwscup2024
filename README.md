# [ipwscup2024](https://www.iwsec.org/pws/ipws2024/)

## How to play

### Anonymization
1. Receive three sets of distribution data from the organizer.
2. Select one set of data to be anonymized from the three sets of distribution data.
3. Commit the ID (e.g. 00) of the selected distribution data to [the thread in the Forum tab](https://www.codabench.org/forums/3178/507/).
4. Rename the file names of the selected distribution dataset to include your Team ID.
   - For example, if the team ID is 99, iBi00.csv, iBi00_0.csv, ... iBi00_9.csv must be renamed to iB99.csv, iB99_0.csv, ... , iB99_9.csv (note that the third character 'i' is removed).
5. Anonymize the selected distribution dataset.
   - For example, if the team ID is 99, then iB99_0.csv, ... , iB99_9.csv are anonymized and 10 files are created: iC99_0.csv, ... , iC99_9.csv.
6. Use checkCi.py to check that the 10 anonymized files are in the correct format.
   - Usage : python checkCi.py iB99_0.csv iC99_0.csv
7. Create an id.txt file with the team ID (e.g. 99).
8. Zip 10 anonymized files (e.g. iC99_0.csv, iC99_1.csv, ... , iC99_9.csv) and id.txt into one zip file.
   - The file can be named freely (e.g., submit.zip). Note that, the 10 anonymized files and id.txt are placed directly below the zip file. Including folders will result in an error.
9. Click on the My Submissions tab of [iPWS Cup 2024 competition site on codabench](https://www.codabench.org/competitions/3260/), then click on the clip icon a little further down to bring up the file selection window, select the zip file you created earlier and submit it.
   - Before selecting the file, write a comment in the comment box just above the clip icon, and the comment will be displayed on the leaderboard (which appears when you press the Results tab) along with the results.
10. The status of the submitted zip file is displayed at the bottom of the screen; if the Status column is Ready, the process is complete.
      - Please be patient as this may take more than five minutes. If there are any errors, the status may change to 'Failed' or remain 'Submitting' or 'Running' for a long time. If the status does not change to 'Finished' for a long time, please contact the organizer (pwscup2024-info(at)csec.ipsj.or.jp (replace '(at)' with the at sign '@')).
12. Press the left icon (Add to Leaderboard when hovered over) of the two icons that appear in the Actions column when the Status column is Ready.
13. When the icon changes to a tick icon, the process is complete. This will be reflected in the leaderboard.
- If you want to modify the anonymized files, re-zip the 10 modified files and the id.txt and resubmit.
- If you want the previously submitted results to be reflected in the leaderboard, click on the icon to the left of the Actions column of the previously submitted results to change it to a check mark icon.

### Attack
- TBA

## Programmes & Data
- codabench/
  - Directory of programmes and data for input into codabench.
- codabench/iB99.zip
  - Zip file of sample distribution dataset and its attack evaluation dataset for utility and anonymity evaluation.
- codabench/id.txt
  - File with your team's ID number.
- codabench/metadata
  - Command to run run_anonymisation.py, to be loaded into codabench.
- codabench/run_anonymization.py
  - Reads a zip file consisting of an anonymized data file and id.txt and outputs the utility score, sample anonymity score and the total score.
  - The zip file is entered via the codabench GUI.
- codabench/submit.zip
  - Sample zip file to be loaded into run_anonymization.py.
- data/A.csv
  - Original data for creation of synthetic data. 
- data/sampleBi.csv
  - A sample data of distribution data Bi.
- sample_code/randomization.py
  - Read a csv file and randomize the data for a given attribute.
  - Each value in the specified attribute does not change with probability p, but changes to a random value with probability 1-p.
  - Usage : python randomization.py \<inputfilename> \<outputfilename> \<attribute name> \<probability p>
- sample_code/randomShuffle.py
  - Read a csv file and randomly replace the order of records (rows).
  - Usage : python randomShuffle.py \<inputfilename> \<outputfilename>
- sample_code/recoding.py
  - Read a csv file, specify the attribute name (only one), the value before the change and the value after the change, and batch convert the value before the change to the value after the change.
  - Usage : python recoding.py \<inputfilename> \<outputfilename> \<pre-conversion value name> \<post-conversion value name>
- sample_code/sampleAttack.py
  - An attack sample code.
  - Enter the ID number (e.g. 99) and run the code. The attack result file E99.csv is output.
  - The output files B99a.csv and B99b.csv from maketest.py and the anonymized data file C99.csv must be placed in the same directory.
  - Usage : python samleAttack.py --id \<id number>
- sample_code/swapping.py
  - Read a csv file, specify the attribute name(s) and the number of times n, select two random pieces of data for the specified attribute and swap the values (repeat this n times).
  - Usage : python swapping.py \<inputfilename> \<outputfilename> \<attribute name 1> ... \<attribute name m> \<n>
- tools/answerCheck.py (Renamed attackScore.py)
  - Reads two files (distribution data and anonymized data) and returns the number of matches.
  - Usage : python answerCheck.py \<prefix of file1> \<prefix of file2>
- tools/checkCi.py
  - Check the validity of anonymized data formats.
  - Usage : python checkCi.py \<filename of Ci>
- tools/genHash.py
  - Calculate the hash value (SHA-256) of distribution data Bi.
  - Integrity check against the pre-published hash value of Bi.
  - Usage : python genHash.py \<filename of Bi>
- tools/maketest.py
  - Read Bi and create data for attacks.
  - For example, for input B00.csv, output B00s.csv, B00a.csv, B00b.csv and B00ans.csv.
    - B00s.csv : 50 lines randomly selected from B00.csv.
    - B00a.csv : Data in the basic attributes (Name, Gender, Age, Occupation, ZIP-code) extracted from B00s.csv.
    - B00b.csv : Movie ratings data from B00s.csv modified by random shuffling and partially redacted.
    - B00ans.csv : Answer data showing how B00b.csv was shuffled and where it was redacted.
  - Usage : python maketest.py \<prefix of Bi>
- tools/split.py
  - Output subset data files iB99_0.csv, iB99_1.csv, ... , iB99_9.csv from iB99.csv.
  - They are the original data of anonymized data iC99_0, iC99_1, ... , iC99_9.
  - Usage : python split.py \<prefix of Bi> 
- tools/utilityScore.py
  - Enter the ID number (e.g. 99) and run (iB99_0.csv, iC99_0.csv), ... , (iB99_9.csv, iC99_9.csv), each of which is fed into utilityScoreSingle.py and run to output the lowest utility score obtained.
  - Usage : python utilityScore.py id.txt 
- tools/utilityScoreSingle.py
  - Input files before and after anonymization, calculate the MAE (Mean Absolute Error) of all cross-tabulations of basic attributes (Gender, Age, Occupation, ZIP-code) x movie rating data and movie rating data x movie rating data, and output a utility score (1-w)*100 for the worst MAE value w.
  - Usage : python utilityScoreSingle.py \<file1> \<file2> 
