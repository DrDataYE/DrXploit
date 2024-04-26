import requests
import threading
from multiprocessing.dummy import Pool
import os,sys,time
import re
from colorama import Fore								
from colorama import Style								
from colorama import init												
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN											
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}




class other():
    def cms(self,i):
        if str(os.path.exists('CMS')) == 'False':
            os.system('mkdir CMS')
        else:
            pass
        i = i.rstrip()
        wordpress = i+'/wp-login.php'
        joomla = i+'/administrator'
        drupal = i +'/user/login'
        dr = requests.get(drupal,headers=user)
        rb = requests.get(wordpress,headers=user)
        jo = requests.get(joomla ,headers=user)
        pr = requests.get(i,headers=user)
        pre = 'prestashop' in pr.content or 'Prestashop' in pr.content or 'PrestShop' in pr.content
        joo = 'joomla' in jo.content or 'Joomla' in jo.content or 'joomla' in pr.content
        wor = 'wordpress' in rb.content or 'Wordpress' in rb.content or 'WordPress' in rb.content or 'wordprss' in pr.content
        druu= 'drupal' in dr.content or 'Drupal' in dr.content or 'drupal' in pr.content
        if pre:
        #if True:
            with open('CMS/PrestShop.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}PrestaShop').format(fy,sb)
        elif joo:
        #elif True:
            with open('CMS/Joomla.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}Joomla').format(fg,sb)
        elif joo:
        #elif True:
            with open('CMS/Joomla.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}Joomla').format(fg,sb)
        elif wor:
        #elif True:
            with open('CMS/WordPress.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}WordPress').format(fbl,sb)

        elif druu:
        #elif True:
            with open('CMS/Drupal.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}Drupal').format(fr,sb)



        else:
            with open('CMS/Unknown.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}UnkNown').format(fr,sn)

    def correct(self,i):
        try:
            pack.cms(i)
        except:
            print '.'
    def runcms(self):
        try:
            ThreadPool = Pool(15)
            Threads = ThreadPool.map(pack.correct, ooo)
        except:
            pass
            
    def ip(self,i):
        i = i.rstrip()
        i = i.replace("http://", "")
        i = i.replace("https://", "")
        i = i.replace("/", "")
        i = i.replace("\n", "")
        data = socket.gethostbyname(i)
        ok.append(data)

    def runip(self):
        ThreadPool = Pool(15)
        Threads = ThreadPool.map(pack.ip, ooo)



    def grabber(self):
        gr = raw_input('\t        '+('{}{} Give me List Servers: ').format(fr,sb))
        gr = open(gr,'r')
        for done in gr:
            remo = []
            page = 1
            while page < 251:
                bing = "http://www.bing.com/search?q=ip%3A"+done+"+&count=50&first="+str(page)
                opene = requests.get(bing,verify=False,headers=headers)
                read = opene.content
                findwebs = re.findall('<h2><a href="(.*?)"', read)
                for i in findwebs:
                    o = i.split('/')
                    if (o[0]+'//'+o[2]) in remo:
                        pass
                    else:
                        remo.append(o[0]+'//'+o[2])
                        print '{}[XxX]'.format(fg,sb),(o[0]+'//'+o[2])
                        with open('Sites.txt','a') as s:
                            s.writelines((o[0]+'//'+o[2])+'\n')
                page = page+50



pack = other()
pack.grabber()
