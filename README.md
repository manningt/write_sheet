# Write drill & game scores to google sheets
 
## What it does


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
cd write_sheets
python3 -m pip install virtualenv
pip3 install oauth2client
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
pip3 install PyOpenSSL
pip3 install gspread
```


## installation at the site
* this requires creating a file named 'score_update_config.json' which configures the name of the sheet to be appended to
* an exanple is in this repository