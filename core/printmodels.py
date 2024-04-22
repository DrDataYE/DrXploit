from rich.console import Console
from rich.table import Table

console = Console()

# coding=utf-8
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'

def Print_Scanning(url, CMS):
    console.print(f"[bold blue][*][/] [white]{url}[/] -> [ [white]{CMS}[/] ]")

def Timeout(url):
    console.print(f"[bold red][-][/] [white]{url}[/] -> [red][ TimeOut!!/NotValid Url ][/]")

def Print_NotVuln(NameVuln, site):
    console.print(f"[bold red][-][/] [white]{site}[/] -> [yellow]{NameVuln}[/] [cyan] [Not Vuln][/]")

def Print_Username_Password(username, Password):
    console.print(f"[bold green][+][/] [white]Username: [/][bold green]{username}[/]")
    console.print(f"[bold green][+][/] [white]Password: [/][bold green]{Password}[/]")

def Print_Vuln(NameVuln, site):
    console.print(f"[bold green][+][/] [white]{site}[/] -> [bold white]{NameVuln}[/] [bold green][Vuln!!][/]")

def Print_Vuln_index(indexPath):
    console.print(f"[bold green][+][/] [white]{indexPath}[/] -> [bold green][Index Uploaded!][/]")

def Print_vuln_Shell(shellPath):
    console.print(f"[bold green][+][/] [white]{shellPath}[/] -> [bold green][Shell Uploaded!][/]")

def Print_vuln_Config(site):
    console.print(f"[bold green][+][/] [white]{site}[/] -> [bold green][Config Downloaded!][/]")


def returnYes(target, CVE, Name, CMS):
    return ['{}{}{}'.format(y, target, w), '{}{}{}'.format(c, CVE, w),
            '{}{}{}'.format(w, Name, w), '{}YES{}'.format(g, w), '{}{}{}'.format(c, CMS, w)]

def returnNo(target, CVE, Name, CMS):
    return ['{}{}{}'.format(y, target, w), '{}{}{}'.format(c, CVE, w),
            '{}{}{}'.format(w, Name, w), '{}NO{}'.format(r, w), '{}{}{}'.format(c, CMS, w)]

def print_table(scanned_results):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("TARGET", style="dim")
    table.add_column("CVE")
    table.add_column("Name")
    table.add_column("Vulnerable", style="green")
    table.add_column("CMS")
    for result in scanned_results:
        if result[3] == "YES":
            result[3] = f"[bold green]{result[3]}[/]"
        else:
            result[3] = f"[bold red]{result[3]}[/]"
        table.add_row(*result)
    console.print(table)



# Print_Scanning("www.example.com", "WordPress")

# Timeout("www.example.com")

# Print_NotVuln("SQL Injection", "www.example.com")

# Print_Username_Password("admin", "admin1234")

# Print_Vuln("XSS", "www.example.com")

# Print_Vuln_index("/path/to/index")
# Print_vuln_Shell("/path/to/shell")

# Print_vuln_Config("www.example.com")

# # # Example usage of the print_table function
# # ScannedRez = [
# #     ['google.com','CVE-2015-1579','revslider', 'YES', 'Wordpress'],
# #     ['google.com','CVE-2015-1579','revslider', 'NO', 'Wordpress'],
# #     ['google.com','CVE-2015-1579','revslider', 'NO', 'Wordpress']
# # ]

# # print_table(ScannedRez)
