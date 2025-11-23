import argparse
import sys
from pathlib import Path

def process_log_file(file_path):
    """
    Reads a log file and prints basic stats.
    """
    log_path = Path(file_path)
    
    if not log_path.exists():
        print(f"❌ Error: The file '{file_path}' was not found.")
        return

    print(f"🔍 Analyzing {log_path.name}...")
    
    # Basic counters
    line_count = 0
    error_count = 0
    
    try:
        # We use 'utf-8' with 'ignore' to prevent crashing on weird binary characters in logs
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line_count += 1
                if "ERROR" in line:
                    error_count += 1
        
        print("\n--- Summary Report ---")
        print(f"Total Lines Processed: {line_count}")
        print(f"Error Count:           {error_count}")
        
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Log Lens - A simple log file analyzer.")
    
    # This argument is required
    parser.add_argument("file", help="Path to the log file you want to analyze")
    
    args = parser.parse_args()
    
    process_log_file(args.file)

if __name__ == "__main__":
    main()