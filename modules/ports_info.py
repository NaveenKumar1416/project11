import subprocess
from prettytable import PrettyTable

def list_ports(port):
    if port == "all":
        result = subprocess.getoutput("sudo ss -tulpen")
        print(result)
    else:
        print(f"Details for port {port}:")
        cmd = f"sudo ss -tulpen | grep :{port}"
        print(subprocess.getoutput(cmd))
