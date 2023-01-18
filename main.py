import time
from playwright.sync_api import sync_playwright
import neotermcolor
from tabulate import tabulate

def login(db_id,username,password):
    page.query_selector("#selectBranch").click()
    time.sleep(1)

    page.query_selector(".select2-search__field").fill(db_id)
    time.sleep(1)

    page.keyboard.press("Enter")

    page.get_by_label("Username").fill(username)
    time.sleep(2)
    page.get_by_label("Password").fill(password)
    time.sleep(1)

    page.query_selector(".sign-in").click()
    time.sleep(3)
    

def IPODict(list_):
    ipoData = [i.inner_text().split('\n') for i in list_]

    IPOs = [[ipoData.index(ipo) + 1,ipo[0], f'{ipo[4]} {ipo[3]}'] for ipo in ipoData]

    return IPOs

def gotoAsba():
    
    page.query_selector('xpath=//*[@id="sideBar"]/nav/ul/li[8]/a').click()
    
    time.sleep(5)
    print(page.url)
    share = page.query_selector_all(".company-name")
    columns = ["Options","Company","Type"]
    data = IPODict(share)
    neotermcolor.cprint(tabulate(data,headers=columns,tablefmt="grid"),"green")
    return len(data)

def ipo_selector(total,ind=''):
    if (total == 1):
        iposelector_index = ''
    else:
        iposelector_index = '[{}]'.format(ind)
    
    xpath_string = '//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div' + iposelector_index +'/div/div[2]/div/div[4]/button'
    apply_btn = page.query_selector(f"xpath ={xpath_string}")
    time.sleep(2)
    apply_btn.click()
    time.sleep(2)
    neotermcolor.cprint("IPO Selected Successfully")

def apply_share(bank,kitta,crn,txn_no):
    page.query_selector("#selectBank").select_option(bank)
    time.sleep(2)
    page.query_selector("#appliedKitta").click()
    page.query_selector("#appliedKitta").type(kitta)
    page.query_selector("#crnNumber").fill(crn)
    time.sleep(1)
    page.query_selector("#disclaimer").click()
    time.sleep(3)
    # print(page.query_selector("button[type=submit]").inner_text())
    page.get_by_role("button",name="Proceed").click()

    page.query_selector("#transactionPIN").type(txn_no)

    page.get_by_role("button",name="Apply").click()
    neotermcolor.cprint("IPO Applied Successfully","green")

    # below code to logout the current user
    page.query_selector(".header-menu__link").click()


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
    browser = p.chromium.launch(headless=False)
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
        login(dp_id,username,password)
        time.sleep(2)
        try:
            total = gotoAsba()
        except:
            neotermcolor.cprint(f"Login Error, recheck credentials of {name}","red")
            neotermcolor.cprint("-------------------------------------------","red")
            continue
        position = int(input("Enter the OPTION NUMBER you want to apply IPO for : "))
        ipo_selector(total,position)
        time.sleep(2)
        apply_share(bank,kitta,crn,txn_pin)
        time.sleep(5)
        neotermcolor.cprint("-------------------------------------------","green")

    browser.close()