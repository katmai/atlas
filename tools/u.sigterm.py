import os
import signal
import sys

if len(sys.argv) < 2:
    print("Please provide the PID of the Python script as a command-line argument.")
    sys.exit(1)

pid = int(sys.argv[1])
os.kill(pid, signal.SIGTERM)
