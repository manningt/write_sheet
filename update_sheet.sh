#! /bin/bash   

# THIS file is for reference only - it has been implemented in boomer_supporting_files/
if [[ $2 != score_update.json ]] ; then
 printf "skipping handling of file: $2\n"
 exit 0
fi
printf "update_sheet called with {$1} {$2}\n"
cd /home/pi/repos/write_sheet
source venv/bin/activate
python3 sheet.py $1 $2

