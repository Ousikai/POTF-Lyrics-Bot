import datetime
import sys
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sys.stdout.write(str(timestamp)+"\n")
