import os, sys
os.system("git pull")
try:
    __import__("MATAL6T9").menu()
except Exception as e:
    exit(str(e))
