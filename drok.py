import argparse
from googlesearch import search
from urllib.parse import urlparse
import time

from googlesearch import search
from urllib.parse import urlparse
import os

def fetch_sites_and_save(site, inurl):
    query = f"site:ye inurl:gov"
    domains = set()  # لتخزين النطاقات بدون تكرار

    # البحث عن المواقع باستخدام جوجل
    for result in search(query):
        # تحليل عنوان URL لاستخراج النطاق
        parsed_url = urlparse(result)
        domain = parsed_url.netloc
        domains.add(domain)

    # كتابة النطاقات في ملف
    with open("sites.txt", "a") as file:
        for domain in sorted(domains):
            file.write(f"{domain}\n")

    print(f"Saved {len(domains)} unique domains to sites.txt")


def main():
    parser = argparse.ArgumentParser(description="Fetch and save domains based on Google search.")
    parser.add_argument("--site", type=str, required=True, help="The site domain to search for.")
    parser.add_argument("--inurl", type=str, required=True, help="The URL part to include in the search.")
    args = parser.parse_args()
    fetch_sites_and_save(args.site, args.inurl)

if __name__ == "__main__":
    main() 

