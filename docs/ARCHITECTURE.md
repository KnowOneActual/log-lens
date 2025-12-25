# Log Lens Architecture

## Project Structure

```
log-lens/
├── src/log_lens/
│   ├── __init__.py              # Package initialization
│   ├── cli.py                  # Click CLI entry point
│   ├── main.py                 # Main orchestration logic
│   ├── parser.py               # Log parsing and format detection
│   ├── exporter.py             # JSON/CSV export functionality
│   ├── models/                 # Data models (Pydantic)
│   │   ├── __init__.py
│   │   ├── log_entry.py            # LogEntry dataclass
│   │   ├── analysis.py             # Analysis result models
│   │   └── config.py               # Configuration models
│   ├── core/                   # Core analytics engine
│   │   ├── __init__.py
│   │   ├── analyzer.py             # Analysis orchestration
│   │   ├── filters.py              # Filtering logic
│   │   └── stats.py                # Statistical aggregation
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── logging.py              # Logging configuration
│   │   └── validators.py           # Input validation
│   ├── config/                 # Configuration files
│   │   ├── __init__.py
│   │   ├── patterns.yaml           # Regex patterns for log formats
│   │   └── defaults.yaml           # Default configuration
│   ├── api/                    # (Future) FastAPI backend
│   └── web/                    # (Future) Vue.js frontend
├── tests/
│   ├── __init__.py
│   ├── fixtures/               # Test data and log samples
│   │   ├── apache_access.log
│   │   ├── nginx_combined.log
│   │   └── generic.log
│   ├── test_parser.py          # Parser unit tests
│   ├── test_cli.py             # CLI integration tests
│   ├── test_analyzer.py        # Analytics engine tests
│   └── test_exporter.py        # Export functionality tests
├── docs/
│   ├─┐ ARCHITECTURE.md         # This file
│   ├── ROADMAP.md
│   └── examples/               # Usage examples
├── pyproject.toml          # Poetry configuration
├── README.md               # Project overview
├── CONTRIBUTING.md         # Contribution guidelines
├── CHANGELOG.md            # Version history
└── LICENSE                 # MIT License
```

---

## Data Flow

```
User Input (CLI)
     │
     │ └─ cli.py (Click entry point)
     │
     │ └─ main.py (load file)
     │
     v
  parser.py (detect format + parse)
     │
     └─ Regex matching against patterns
     └─ Yield LogEntry objects
     └─ Handle errors gracefully
     │
     v
  core/analyzer.py (aggregate statistics)
     │
     └─ core/stats.py (count, aggregate)
     └─ core/filters.py (apply user filters)
     │
     v
  models/analysis.py (AnalysisResult)
     │
     v
  exporter.py or CLI display
     │
     └─ JSON export
     └─ Rich CLI tables
     │
     v
  Output to user
```

---

## Core Modules

### 1. **parser.py** - Log Parsing Engine

**Responsibility:** Auto-detect log format and parse entries

**Key functions:**
```python
def detect_format(file_path: Path) -> str:
    """Auto-detect log format (apache, nginx, generic)"""
    # Read first N lines and match against patterns
    pass

def parse_log(file_path: Path, format_hint: Optional[str] = None) -> Iterator[LogEntry]:
    """Parse log file yielding LogEntry objects"""
    # Lazy evaluation: process line-by-line
    pass

def extract_line(line: str, pattern: str) -> Optional[LogEntry]:
    """Extract structured data from single line"""
    # Use regex to parse
    pass
```

**Supported formats (v0.2+):**
- Apache Combined Log Format
- Apache Common Log Format
- Nginx Combined Format
- Nginx Common Format
- Generic/Custom format (configurable)

---

### 2. **core/analyzer.py** - Analysis Engine

**Responsibility:** Aggregate statistics and apply transformations

**Key functions:**
```python
def analyze(entries: Iterator[LogEntry], config: AnalysisConfig) -> AnalysisResult:
    """Run analysis pass over log entries"""
    # 1. Apply filters (IP, status, path, time range)
    # 2. Aggregate statistics
    # 3. Return AnalysisResult
    pass

def count_by_key(entries: Iterator[LogEntry], key: str) -> Dict[str, int]:
    """Count occurrences by key (ip, status, path, method)"""
    pass

def get_top_n(counts: Dict[str, int], n: int) -> Dict[str, int]:
    """Get top N entries by count"""
    pass
```

**Output:** `AnalysisResult` object containing:
- Total entries processed
- Detected format
- Status code distribution
- Top IPs (with counts)
- Top paths (with counts)
- HTTP method breakdown
- Timestamps (earliest, latest)

---

### 3. **exporter.py** - Output Formatting

**Responsibility:** Export analysis results in various formats

**Supported formats:**
- JSON (v0.1+)
- Rich CLI tables (v0.1+)
- CSV (v0.3+)
- HTML reports (v0.3+)

**Key functions:**
```python
def export_json(result: AnalysisResult, output_path: Path) -> None:
    """Export AnalysisResult as JSON"""
    pass

def export_csv(result: AnalysisResult, output_path: Path) -> None:
    """Export as CSV (v0.3+)"""
    pass

def render_tables(result: AnalysisResult) -> None:
    """Display Rich-formatted tables in terminal"""
    pass
```

---

### 4. **cli.py** - Command-Line Interface

**Responsibility:** Parse CLI arguments and orchestrate execution

**Main command:**
```bash
log-lens <log-file> [options]

Options:
  --top-ips N              Show top N IPs
  --top-paths N            Show top N paths
  --format {apache,nginx}  Force log format
  --filter-ip IP           Include only requests from IP
  --filter-status CODE     Include only specific HTTP status
  --export FILE            Export results to JSON
  --verbose, -v            Enable debug output
```

---

## Data Models

### LogEntry
```python
@dataclass
class LogEntry:
    timestamp: datetime
    ip_address: str
    method: str
    path: str
    status_code: int
    response_size: int
    referrer: Optional[str] = None
    user_agent: Optional[str] = None
    duration_ms: Optional[float] = None  # For logs that include timing
```

### AnalysisResult
```python
@dataclass
class AnalysisResult:
    total_entries: int
    detected_format: str
    status_codes: Dict[int, int]
    top_ips: Dict[str, int]
    top_paths: Dict[str, int]
    methods: Dict[str, int]
    earliest_time: datetime
    latest_time: datetime
    errors: List[str] = field(default_factory=list)
```

---

## Design Principles

1. **Lazy Evaluation**
   - Parse logs line-by-line (don't load entire file into memory)
   - Use generators to process large files efficiently

2. **Composability**
   - Each module has a single responsibility
   - Easy to extend (e.g., add new log formats, export types)

3. **Configuration-Driven**
   - Log format patterns in external YAML (not hardcoded)
   - Allows user-defined formats

4. **Error Resilience**
   - Skip unparseable lines (log warning, continue)
   - Graceful degradation if optional fields missing

5. **Performance**
   - Single-pass analysis when possible
   - Optimized regex compilation
   - Tested on 1GB+ files

---

## Testing Strategy

### Unit Tests
- **parser.py**: Test each format detection and parsing
- **core/analyzer.py**: Test filtering, aggregation logic
- **exporter.py**: Test JSON/CSV generation

### Integration Tests
- **cli.py**: End-to-end CLI tests with fixtures
- Real log files from different servers

### Fixtures
- Sample Apache, Nginx, generic logs in `tests/fixtures/`
- Real-world logs from production servers (anonymized)

### Performance Tests
- Benchmark on 100MB, 1GB log files
- Target: <5s for 100MB, <30s for 1GB

---

## Dependencies

**Core:**
- `click` - CLI framework
- `rich` - Terminal formatting
- `pydantic` - Data validation
- `pyyaml` - Config file parsing

**Optional:**
- `pandas` - Advanced analytics (v0.3+)
- `plotly` - HTML charts (v0.3+)
- `fastapi` - Web API (v0.4+)

**Dev:**
- `pytest` - Testing
- `black` - Code formatting
- `isort` - Import sorting
- `mypy` - Type checking
- `pre-commit` - Git hooks

---

## Future Roadmap

See [ROADMAP.md](./ROADMAP.md) for v0.2+ features:
- Web dashboard with real-time updates
- Advanced filtering and querying
- Security anomaly detection
- Email/Slack alerting

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for development setup and PR guidelines.
