<div align="center">

# MEROSHARE BOT

[![Playwright](https://img.shields.io/pypi/v/playwright.svg)](https://pypi.python.org/pypi/playwright)
[![License Badge](https://img.shields.io/github/license/tprototype/meroshare-bot?color=2b9348)](https://github.com/tprototype/meroshare-bot/blob/master/README.md)
[![Releases](https://img.shields.io/badge/version-0.0.1-blue)](https://github.com/tprototype/meroshare-bot/releases)

</div>


**This is meroshare bot, which will auto apply IPO of different company which are open.**

## Get Started

To get started, you need to download this project or can clone this repo on your machine.
And you can simply run the main.py file. But before that you need to setup the environment.

### 1. Install the dependencies

```
pip install -r requirments.txt
# or
python3 -m pip install -r requirements.txt
```

### 2. Run following code in the terminal

```
playwright install chromium
```

### 3. Edit demats.txt file to setup your information in the serial order as given

```
Name,CapitalID,Username,Password,Bank Name,Kitta,CRN,TXN_PIN

For example:
Ram,13700,0124525,password123,NIC ASIA BANK LTD.,10,JYU8281811,1234

"Ram" here is just a placeholder to denote the account, it can be anything you like

Bank Name can be : "NIC ASIA BANK LTD.", "Nabil Bank Limited.", "CIVIL BANK LTD.", "Nepal Investment Bank Ltd." ,"GARIMA BIKAS BANK LTD.", "NMB BANK LTD." (i.e Official Name)
```

### 4. Now just run main.py file to run the script

```
python main.py
# or
python3 main.py
```

### Please :star: Star us on GitHub — it motivates us a lot!

### You can raise issues or send message to ask if there is any problem you faced in any step
### And suggestion are welcome :)

