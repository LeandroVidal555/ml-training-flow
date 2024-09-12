import shutil
from datetime import datetime

# Specify the source file path and destination file path
src = "/opt/ml/processing/input-data/test.txt"
dst = "/opt/ml/processing/output-data/test_out.txt"
nbk = "/opt/ml/processing/ml-training-flow/notebook.py"

# Copy the file
shutil.copy(src, dst)

# Get current time
ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# Write to the out file
with open(nbk, 'r') as f_src, open(dst, 'a') as f_dst:
    f_dst.write(f"CHECK {ts}\n")

    # Read the first 10 lines from the source file
    for i in range(10):
        line = f_src.readline()
        # Break if we've reached the end of the file
        if not line:
            break
        # Write the line to the destination file
        f_dst.write(line)