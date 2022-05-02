# Amazon Creditcard Balance Checker

The `cc.py` script opens up a selenium browser instance and gets your current balance from the lbb.de Site. 

Set the following in the file `config.ini` before running the script

- `cc_username` : your_LBB_username
- `cc_password` : your_Password
- `url` : URL where you type in your credentials


NOTE: You need to change the path to your geckodriver in the cc.py script. If you've already included geckodriver path to your PATH, than just erase the argument in the bracket.

#### IMPORTANT

Due to the new amazon LBB interface, you need to authenticate your machine first. This can be done by running the cc_auth.py script. You need to enter you credentials and logout again. This saves an cookie in a userfolder of selenium. This needs to be done, otherwise amazon lbb will repeat to ask for authentication for "this device".

#### REQUIREMENTS

- Python 3.x
- selenium - `sudo apt-get install selenium`


Important Disclaimer: Since the credentials are in plaintext in your config, i'll take no responsebility for that. This programm is only a proof-of-concept. Don't use it, if you are not able to keep your data safe from data theft. 
