import subprocess
import sys
import time
from datetime import datetime


RUN_INTERVAL_SECONDS = 60


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


def start_scheduler():
    print("OpsFlow scheduler started.")
    print(f"The workflow will run every {RUN_INTERVAL_SECONDS} seconds.")
    print("Press CTRL + C to stop the scheduler.\n")

    try:
        while True:
            run_opsflow_pipeline()

            print(f"\nNext run in {RUN_INTERVAL_SECONDS} seconds...")
            time.sleep(RUN_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")


if __name__ == "__main__":
    start_scheduler()