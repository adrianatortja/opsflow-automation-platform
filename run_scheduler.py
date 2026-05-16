import subprocess
import sys
import time
from datetime import datetime


DEFAULT_RUN_INTERVAL_SECONDS = 60


def get_run_interval():
    if len(sys.argv) < 2:
        return DEFAULT_RUN_INTERVAL_SECONDS

    try:
        interval = int(sys.argv[1])

        if interval <= 0:
            print("Interval must be greater than 0. Using default interval.")
            return DEFAULT_RUN_INTERVAL_SECONDS

        return interval

    except ValueError:
        print("Invalid interval value. Using default interval.")
        return DEFAULT_RUN_INTERVAL_SECONDS


def run_opsflow_pipeline():
    print("\n==============================")
    print(f"Running OpsFlow pipeline at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("==============================\n")

    try:
        subprocess.run([sys.executable, "main.py"], check=True)
        print("\nOpsFlow pipeline completed successfully.")

    except subprocess.CalledProcessError as error:
        print("\nOpsFlow pipeline failed.")
        print(f"Error code: {error.returncode}")


def start_scheduler(run_interval_seconds):
    print("OpsFlow scheduler started.")
    print(f"The workflow will run every {run_interval_seconds} seconds.")
    print("Press CTRL + C to stop the scheduler.\n")

    try:
        while True:
            run_opsflow_pipeline()

            print(f"\nNext run in {run_interval_seconds} seconds...")
            time.sleep(run_interval_seconds)

    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")


if __name__ == "__main__":
    run_interval = get_run_interval()
    start_scheduler(run_interval)