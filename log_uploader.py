import datetime
import os

# Terminal Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

print(BLUE + "Creating log entry..." + RESET)

# Create to local log
log_entry = f"[{datetime.datetime.now()}] New log entry created.\n"

with open("local_log.txt", "a") as f:
    f.write(log_entry)

print(GREEN + "Log entry written to local_log.txt" + RESET)

# Create unique timestamped filename for S3 upload
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
s3_filename = f"log-{timestamp}.txt"

print(BLUE + f"Uploading log to S3 as {s3_filename}..." + RESET)

# Upload using AWS CLI
exit_code = os.system(f"aws s3 cp local_log.txt s3://cloud-greeter-1234/{s3_filename}")

if exit_code == 0:
    print(GREEN + f"Uploaded as {s3_filename}" + RESET)
else:
    print(RED + "Error: upload failed!" + RESET)
