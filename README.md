# Amazon Creditcard Balance Checker

The `cc.py` script opens up a selenium browser instance and gets your current balance from the lbb.de Site. 

Set the following in the file `config.ini` before running the script

- `cc_username` : your_Creditcard_number
- `cc_password` : your_Password
- `url` : URL for moodle authentication / Where you type in your credentials


NOTE: You need to change the path to your geckodriver in the cc.py script. If you've already included geckodriver path to your PATH, than just erase the argument in the bracket.


#### REQUIREMENTS

- Python 2.7
- selenium - `sudo apt-get install selenium`


Important Disclaimer: Since the credentials are in plaintext in your config, i'll take no responsebility for that. This programm is only a proof-of-concept. Don't use it, if you are not able to keep your data safe from data theft. 
