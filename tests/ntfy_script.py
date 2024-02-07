# Simple script that curls information via the ntfy.sh website to notify of the status of the run_provider_checks() method.
import requests
import time
from stockstir import Stockstir

stockstir = Stockstir()

# Print out the current date and time (this will be put into the logfile.txt file, which contains the logs dumped by chron).
print("EXECUTION DATE: " + time.strftime("%m/%d/%Y %H:%M:%S") + "\n")

num_tries = 3
for i in range(num_tries):
  if stockstir.providers.run_provider_checks(exit_on_failure=False):
    message = "Stockstir Providers WORKING"
    break
  message = "!!Stockstir Providers FAILED!!"

requests.post("https://ntfy.sh/stockstirRPO",
  data=message.encode(encoding='utf-8'))