import json
from pathlib import Path

def export_to_json(data, output_path):
    """
    Saves the analysis data to a JSON file.
    """
    path = Path(output_path)
    
    try:
        print(f"💾 Exporting report to {path.name}...")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print("✅ Export successful.")
    except Exception as e:
        print(f"❌ Failed to export report: {e}")