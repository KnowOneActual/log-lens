import argparse
import sys
from pathlib import Path
from log_lens.parser import LogParser  # Import our new class

def process_log_file(file_path):
    log_path = Path(file_path)
    
    if not log_path.exists():
        print(f"❌ Error: The file '{file_path}' was not found.")
        return

    print(f"🔍 Analyzing {log_path.name}...")
    
    # Initialize our parser
    parser = LogParser()
    total_lines = 0
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                total_lines += 1
                parser.parse_line(line)  # Delegate logic to the parser
        
        # Get results
        counts = parser.get_report()
        
        print("\n--- Summary Report ---")
        print(f"Total Lines Processed: {total_lines}")
        print("-" * 22)
        
        # Dynamically print whatever levels we found
        if counts:
            for level, count in counts.items():
                print(f"{level:<10}: {count}")
        else:
            print("No standard log levels found.")
            
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Log Lens - A simple log file analyzer.")
    parser.add_argument("file", help="Path to the log file you want to analyze")
    args = parser.parse_args()
    process_log_file(args.file)

if __name__ == "__main__":
    main()