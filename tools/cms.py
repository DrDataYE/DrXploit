import requests
import logging
import random
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Renkli terminal çıktısı için renk kodları
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'

# Kullanıcı ajanı listesi
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/537.36'
]

# HTTP Header'ı oluşturuluyor
Headers = {'User-Agent': random.choice(user_agents)}

# CMS tespitinde kullanılacak URL'ler
def get_with_retry(url):
    session = requests.Session()
    retry = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get(url, timeout=10, headers=Headers)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving {url}: {e}")
        return None

# Loglama ayarları
logging.basicConfig(filename='cms_detection.log', level=logging.INFO)

def log_cms_detection(site, cms):
    logging.info(f"Detected CMS: {cms} on site: {site}")
    print(f"{g}[+] Detected {cms} on {site}{w}")

# CMS tespit fonksiyonu
def DetectCMS(site):
    Joomla = f'http://{site}/administrator/help/en-GB/toc.json'
    Joomla2 = f'http://{site}/administrator/language/en-GB/install.xml'
    Joomla3 = f'http://{site}/plugins/system/debug/debug.xml'
    Joomla4 = f'http://{site}/administrator/'

    Wordpress = f'http://{site}'
    Wordpress2 = f'http://{site}/wp-includes/js/jquery/jquery.js'
    
    Drupal = f'http://{site}/misc/ajax.js'
    Drupal2 = f'http://{site}'
    
    Opencart = f'http://{site}/admin/view/javascript/common.js'
    OsCommerce = f'http://{site}/admin/includes/general.js'
    
    vBulletin = f'http://{site}/images/editor/separator.gif'
    vBulletin2 = f'http://{site}/js/header-rollup-554.js'
    
    Magento = f'http://{site}/skin/frontend/base/default/js/prototype/prototype.js'
    Typo3 = f'http://{site}/typo3conf/ext/'

    # CMS tespiti için kontrol etme
    try:
        # WordPress
        CheckWp = get_with_retry(Wordpress)
        if '/wp-content/' in CheckWp or '/wp-inclues/' in CheckWp:
            log_cms_detection(site, 'wordpress')
            return 'wordpress'
        
        CheckWp2 = get_with_retry(Wordpress2)
        if '(c) jQuery Foundation' in CheckWp2:
            log_cms_detection(site, 'wordpress')
            return 'wordpress'

        # Joomla
        CheckJom = get_with_retry(Joomla)
        if '"COMPONENTS_BANNERS_BANNERS"' in CheckJom:
            log_cms_detection(site, 'joomla')
            return 'joomla'
        
        CheckJom2 = get_with_retry(Joomla2)
        if '<author>Joomla!' in CheckJom2:
            log_cms_detection(site, 'joomla')
            return 'joomla'

        CheckJom3 = get_with_retry(Joomla3)
        if '<author>Joomla!' in CheckJom3:
            log_cms_detection(site, 'joomla')
            return 'joomla'

        CheckJom4 = get_with_retry(Joomla4)
        if 'content="Joomla!' in CheckJom4:
            log_cms_detection(site, 'joomla')
            return 'joomla'

        # Drupal
        CheckDrupal = get_with_retry(Drupal)
        if 'Drupal.ajax' in CheckDrupal:
            log_cms_detection(site, 'drupal')
            return 'drupal'

        CheckDrupal2 = get_with_retry(Drupal2)
        if '/sites/default/files' in CheckDrupal2:
            log_cms_detection(site, 'drupal')
            return 'drupal'

        # Opencart
        CheckOpencart = get_with_retry(Opencart)
        if 'getURLVar(key)' in CheckOpencart:
            log_cms_detection(site, 'opencart')
            return 'opencart'

        # OsCommerce
        CheckOsCommerce = get_with_retry(OsCommerce)
        if 'function SetFocus()' in CheckOsCommerce:
            log_cms_detection(site, 'oscommerce')
            return 'oscommerce'

        # vBulletin
        Checkvb = get_with_retry(vBulletin)
        if 'GIF89a' in Checkvb:
            log_cms_detection(site, 'vBulletin')
            return 'vBulletin'

        Checkvb2 = get_with_retry(vBulletin2)
        if 'js.compressed/modernizr.min.js' in Checkvb2:
            log_cms_detection(site, 'vBulletin')
            return 'vBulletin'

        # Magento
        CheckMagento = get_with_retry(Magento)
        if 'Prototype JS' in CheckMagento:
            log_cms_detection(site, 'Magento')
            return 'Magento'

        # Typo3
        CheckTypo3 = get_with_retry(Typo3)
        if 'typo3conf/ext/' in CheckTypo3:
            log_cms_detection(site, 'Typo3')
            return 'Typo3'

        # Eğer hiçbir CMS tespit edilmezse
        log_cms_detection(site, 'unknown')
        return 'unknown'

    except requests.exceptions.Timeout:
        print(f"Timeout occurred while trying to connect to {site}.")
        log_cms_detection(site, 'deadTarget')
        return 'deadTarget'
    except requests.exceptions.TooManyRedirects:
        print(f"Too many redirects encountered for {site}.")
        log_cms_detection(site, 'deadTarget')
        return 'deadTarget'
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while processing {site}: {e}")
        log_cms_detection(site, 'deadTarget')
        return 'deadTarget'
    except Exception as e:
        print(f"Unexpected error: {e}")
        log_cms_detection(site, 'deadTarget')
        return 'deadTarget'

