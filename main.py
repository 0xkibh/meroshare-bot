import time
from playwright.sync_api import sync_playwright
import neotermcolor
from bot.func import login,gotoAsba,ipo_selector,apply_share

with sync_playwright() as p:
    # Description Banner for the tool
    print("""
    -----------------------------------------------------------------------------------------
    ███╗   ███╗███████╗██████╗  ██████╗ ███████╗██╗  ██╗ █████╗ ██████╗ ███████╗    ██████╗  ██████╗ ████████╗
    ████╗ ████║██╔════╝██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██╔████╔██║█████╗  ██████╔╝██║   ██║███████╗███████║███████║██████╔╝█████╗      ██████╔╝██║   ██║   ██║   
    ██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║╚════██║██╔══██║██╔══██║██╔══██╗██╔══╝      ██╔══██╗██║   ██║   ██║   
    ██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝███████║██║  ██║██║  ██║██║  ██║███████╗    ██████╔╝╚██████╔╝   ██║   
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                            
    -----------------------------------------------------------------------------------------
    Author: Kishmat Bhattarai
    Github repository: https://github.com/tprototype/meroshare-bot
    Twitter: @tprototypex
    -----------------------------------------------------------------------------------------
        """)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    page.goto("https://meroshare.cdsc.com.np")
    time.sleep(5)

    total = []
    with open("demats.txt", 'r') as f:
        for x in f.readlines():
            x = x[0:-1]
            total.append(x.split(","))


    for account in total:
        name, dp_id, username, password, bank, kitta, crn, txn_pin = account
        print('Working for ' + name + ' :')
        login(page,dp_id,username,password)
        time.sleep(2)
        try:
            total = gotoAsba(page)
        except:
            neotermcolor.cprint(f"Login Error, recheck credentials of {name}","red")
            neotermcolor.cprint("-------------------------------------------","red")
            continue
        position = int(input("Enter the OPTION NUMBER you want to apply IPO for : "))
        ipo_selector(page,total,position)
        time.sleep(2)
        apply_share(page,bank,kitta,crn,txn_pin)
        time.sleep(5)
        neotermcolor.cprint("-------------------------------------------","green")

    browser.close()