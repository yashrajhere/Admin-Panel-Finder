import requests
from colorama import Fore, Style, init
import sys

init(autoreset=True)

BANNER = Fore.RED + r"""
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝

        Admin Panel Finder
"""

FOOTER = """
Example:
python admin_panel_finder.py https://example.com

Developed by:
Yashraj (@yashrajhere)

Note: Use only on systems you own or have permission to test.
"""

COMMON_PATHS = [
"/admin","/admin/","/administrator","/login","/admin/login",
"/cpanel","/dashboard","/user/login","/adminpanel",
"/admin.php","/admin.html","/wp-admin","/backend"
]

def check_panels(base_url):
    if base_url.endswith("/"):
        base_url = base_url[:-1]

    print("\nScanning for common admin panels...\n")

    found = False
    for path in COMMON_PATHS:
        url = base_url + path
        try:
            r = requests.get(url, timeout=5)
            if r.status_code in [200, 301, 302]:
                print(Fore.GREEN + "[FOUND] " + url)
                found = True
            else:
                print("[...] " + url)
        except:
            print("[x] " + url)

    if not found:
        print("\nNo common admin panels detected.")

if __name__ == "__main__":
    print(BANNER)
    print(Style.RESET_ALL)
    print(FOOTER)

    if len(sys.argv) != 2:
        print("Usage: python admin_panel_finder.py <website_url>")
        sys.exit()

    target = sys.argv[1]
    check_panels(target)
