import datetime
import os

# Create or append to local log
log_entry = f"[{datetime.datetime.now()}] New log entry created.\n"

with open("local_log.txt", "a") as f:
    f.write(log_entry)

print("Log entry written to local_log.txt")

# Create unique timestamped filename for S3 upload
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
s3_filename = f"log-{timestamp}.txt"

# Upload using AWS CLI
os.system(f"aws s3 cp local_log.txt s3://cloud-greeter-1234/{s3_filename}")

print(f"Uploaded as {s3_filename}")
