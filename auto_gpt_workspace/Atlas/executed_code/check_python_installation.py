import subprocess

output = subprocess.check_output("ls /usr/bin | grep python3", shell=True)

if b"python3" in output:
    print("Python is installed on this system.")
else:
    print("Python is not installed on this system.")