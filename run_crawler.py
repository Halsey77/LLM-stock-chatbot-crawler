import os
import sys
import subprocess
import shutil
from datetime import datetime

def run_command(command):
    """ Run a shell command and print output in real-time """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print output line by line in real-time
    for line in process.stdout:
        print(line, end='')

    process.stdout.close()
    process.wait()

    # Capture the return code to check for success/failure
    if process.returncode != 0:
        print(f"Error: Command failed with return code {process.returncode}")
        sys.exit(1)

def main():
    # Step 1: Run the Python script to get free proxies
    print("Running get_free_proxies.py...")
    run_command("python get_free_proxies.py")

    # Step 2: Copy 'proxies.txt' to the 'crawler' folder
    output_file = "proxies.txt"
    destination_folder = "crawl_yahoo"

    if not os.path.exists(output_file):
        print(f"Error: {output_file} does not exist.")
        sys.exit(1)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    try:
        shutil.copy(output_file, destination_folder)
        print(f"Copied {output_file} to {destination_folder} successfully.")
    except Exception as e:
        print(f"Error: Could not copy {output_file} to {destination_folder}: {e}")
        sys.exit(1)

    # Step 3: Generate dynamic output file name using current date and time
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    scrapy_output_file = f"output_{current_time}.json"
    scrapy_log_file = f"scrapy_log_{current_time}.txt"

    # Step 4: Run Scrapy command with dynamic output file name
    os.chdir(destination_folder)  # Change to the 'crawler' folder
    print(f"Running Scrapy with output file: {scrapy_output_file} and log file: {scrapy_log_file}")
    run_command(f"scrapy crawl my_crawler -o {scrapy_output_file} --logfile {scrapy_log_file}")

    print("Process completed successfully!")

if __name__ == "__main__":
    main()
