# Write drill & game scores to google sheets
This was a development directory.  The .json example files are still relevant and need to be part of the installation.  (Maybe they should be moved to boomer_supporting_files.  '''sheet.py''' has been supplanted by '''boomer_supporting_files/score_update.py''' and '''update_sheet.sh''' has been incorporated into '''boomer_supporting_files/scp_logs.py'''
 
## What it does
When bbase (the boomer application) ends a drill, it writes a file into /run/shm/score_update.csv with the drill performance statistics.
The file watch utility (icron) detects the write to the file, and runs the scp_log.sh script, which then runs update_sheet.py.  Both of these scripts are in boomer_supporting_files.

## Useful links
* 'how-to' page: https://www.makeuseof.com/tag/read-write-google-sheets-python/
* Google Developers Console: https://console.developers.google.com/
  * the console is required to enable the sheets API as a project
  * it can also be used to get usage metric
* rust upgrade needed to install OpenSSL: 
  * https://www.rust-lang.org/tools/install


# Installation of required software
1. clone this repository (write_sheets)
2. execute the following commands:
```
sudo apt-get install libssl-dev
python3 -m pip install virtualenv

cd boomer_supporting_files

python3 -m virtualenv venv_sheets
source ./venv_sheets/bin/activate

pip3 install oauth2client
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
pip3 install PyOpenSSL
pip3 install gspread
```


## installation at the site
* this requires creating a file named 'score_update_config.json' which configures the name of the sheet to be appended to
* an exanple is in this repository
