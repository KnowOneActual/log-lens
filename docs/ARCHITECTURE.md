# Log Lens Architecture

## Project Structure

```
log-lens/
├── src/log_lens/
│   ├── __init__.py              # Package initialization
│   ├── cli.py                  # Click CLI entry point
│   ├── parser.py               # Log parsing with Pydantic validation
│   ├── core/                   # Core analytics engine
│   │   ├── __init__.py
│   │   └── reporter.py             # Rich terminal reporting
│   ├── models/                 # Data models (Pydantic)
│   │   ├── __init__.py
│   │   └── log_entry.py            # LogEntry Pydantic model
│   └── config/                 # (Future) Configuration files
├── tests/
│   ├── __init__.py
│   ├── fixtures/               # Test data and log samples
│   ├── test_parser.py          # Parser unit tests
│   └── test_cli.py             # CLI integration tests
├── docs/
│   ├─┐ ARCHITECTURE.md         # This file
│   ├── roadmap.md
│   └── PROJECT_SUMMARY.md
├── pyproject.toml          # Poetry configuration
├── GEMINI.md               # AI context and standards (local-only)
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
     v
  parser.py (LogParser / ApacheParser)
     │
     └─ Validates line with LogEntry Pydantic model
     └─ Aggregates statistics into Counters
     │
     v
  core/reporter.py (Rich terminal output)
     │
     └─ Formats report into tables
     │
     v
  Output to user
```

---

## Core Modules

### 1. **parser.py** - Log Parsing Engine

**Responsibility:** Auto-detect log format and parse entries with validation.

**Key components:**
- `ApacheParser`: Specifically handles Apache Combined log format using regex and Pydantic validation.
- `LogParser`: Main entry point that orchestrates format detection and fallback to generic log parsing.

### 2. **core/reporter.py** - Reporting Engine

**Responsibility:** Format and display analysis results.

**Key functions:**
- `render_report`: Uses the `Rich` library to display summary statistics, top IPs, status codes, and paths in a readable terminal format.

### 3. **models/log_entry.py** - Data Validation

**Responsibility:** Define structured data and enforce type safety.

**Key model:**
- `LogEntry`: A Pydantic model that validates IPs, status codes (as integers), and request details.

---

## Supported Formats (v0.7.1)
- **Apache Combined Log Format** (Fully supported with Pydantic validation)
- **Generic/Fallback format** (Supports basic level and IP extraction)
- **Nginx Combined Format** (Supported via Apache patterns)

---

## Design Principles

1. **Lazy Evaluation**
   - Process logs line-by-line using generators or incremental parsing.
   - Minimal memory footprint for large files.

2. **Type-Safe Validation**
   - Leverage Pydantic for automated data conversion and validation.
   - Ensure reliable analysis by catching malformed data early.

3. **Rich Visual Feedback**
   - Terminal-first design with interactive tables and formatted output.

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
