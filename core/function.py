import os





def ensure_directories_exist():
    # List of directories to check and potentially create
    directories = ['result', 'cms']
    
    # Iterate through the directory list
    for directory in directories:
        # Check if the directory exists
        if not os.path.exists(directory):
            # Directory does not exist, create it
            os.makedirs(directory)
            pass
        else:
            # Directory exists
            pass

def read_domains_from_file(file_path):
    """
    Read domains from a file and return a list of unique domains.

    Args:
    file_path (str): The path to the file containing the domain names.

    Returns:
    list: A list of unique domain names.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                # قراءة الأسطر وإزالة الأسطر الفارغة والمكررة
                domains = set(line.strip() for line in file if line.strip())
            return list(domains)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    else:
        return [file_path]


# coding=utf-8
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'

def Rez(site, i):
    try:
        if 'YES' in str(i):
            print(' {}[+] {}{} {}--> {}{} {}YES!{}'.format(g, w, site, c, y, i[2], g, w))
        else:
            print(' {}[-] {}{} {}--> {}{} {}NO!{}'.format(r, w, site, c, y, i[2], r, w))
    except:
        print(' {}- {}{} {}--> {}{} {}NO!{}'.format(r, w, site, c, y, i[2], r, w))