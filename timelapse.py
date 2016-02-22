import subprocess
import time
import sys

def main():
    time_between = int(sys.argv[1])
    duration = int(sys.argv[2])
    shots = duration // time_between
    
    for i in range(shots):
        subprocess.call(["uvccapture", "-o" + str(i) + ".jpg" ,"-x1280", "-y720"])
        time.sleep(time_between)
    
if __name__ == "__main__":
    main()
