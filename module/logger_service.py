"""logger_service.py - Non-Functional Logging & Activity Tracker Module
CSE1021 Algorithmic Toolkit"""

from datetime import datetime

def log_operation(operation: str, details: str, log_file: str = "execution.log") -> None: #Appends timestamped operational log entries to a local log file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] - {operation}: {details}\n"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception as e:
        print(f"Warning: Logging failed - {e}")

def read_logs(log_file: str = "execution.log") -> list[str]: #Reads and returns the last 10 log entries from the log file, or an empty list if the file does not exist
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            return ["NO log history found yet.\n"]

        return lines[-8:]  # Return the last 8 entries

    except FileNotFoundError:
        return ["NO log history found yet.\n"]
    