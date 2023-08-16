#!/usr/bin/python3
import sys
import signal

# Initialize variables to hold metrics
total_file_size = 0
status_code_counts = {}

# Function to print metrics
def print_metrics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")

# Handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        
        # Check if the line has enough parts to match the input format
        if len(parts) >= 7:
            ip_address = parts[0]
            date = parts[2] + " " + parts[3]
            status_code = parts[-3]
            file_size = int(parts[-2])
            
            total_file_size += file_size
            
            # Check if the status code is a valid integer
            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1
            
            line_count += 1
            
            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()
        
except KeyboardInterrupt:
    # Print metrics upon keyboard interruption
    print_metrics()
