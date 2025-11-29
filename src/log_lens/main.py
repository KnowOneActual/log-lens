import argparse
import sys
from pathlib import Path
from log_lens.parser import LogParser
from log_lens.exporter import export_to_json  # Import the new module

def process_log_file(file_path, export_path=None):
    log_path = Path(file_path)
    
    if not log_path.exists():
        print(f"❌ Error: The file '{file_path}' was not found.")
        return

    print(f"🔍 Analyzing {log_path.name}...")
    
    parser = LogParser()
    total_lines = 0
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                total_lines += 1
                parser.parse_line(line)
        
        # Get results
        report = parser.get_report()
        
        # Add metadata to the report
        report['metadata'] = {
            "source_file": str(log_path),
            "total_lines": total_lines
        }

        # --- HANDLE EXPORT ---
        if export_path:
            export_to_json(report, export_path)
            # We return here to avoid printing the huge text block if they asked for a file
            # (Optional design choice, but keeps the console clean)
            return 

        # --- STANDARD CONSOLE OUTPUT ---
        level_counts = report["levels"]
        ip_counts = report["ips"]
        
        print("\n--- Summary Report ---")
        print(f"Total Lines Processed: {total_lines}")
        
        print("\n--- Log Levels ---")
        if level_counts:
            for level, count in level_counts.items():
                print(f"{level:<10}: {count}")
        else:
            print("No standard log levels found.")

        print("\n--- Top IP Addresses ---")
        if ip_counts:
            sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
            for ip, count in sorted_ips[:5]:
                print(f"{ip:<15}: {count}")
        else:
            print("No IP addresses found.")
            
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Log Lens - A simple log file analyzer.")
    
    parser.add_argument("file", help="Path to the log file you want to analyze")
    
    # New optional argument
    parser.add_argument("--export", help="Path to save the report as JSON (e.g., report.json)")
    
    args = parser.parse_args()
    
    # Pass the export argument to our function
    process_log_file(args.file, export_path=args.export)

if __name__ == "__main__":
    main()