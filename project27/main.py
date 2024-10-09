import sys
from datetime import datetime


args = sys.argv

start_date = args[1]
end_date = args[2]

start_date = datetime.strptime(start_date, "%m-%d-%Y")
end_date = datetime.strptime(end_date, "%m-%d-%Y")

print(start_date - end_date)