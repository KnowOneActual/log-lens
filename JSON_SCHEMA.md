# Log Lens JSON Schema

The `--export` flag outputs structured JSON for dashboards, alerting, or further processing.

## Schema v0.3.0

```json
{
  "format": "apache|unknown",
  "summary": {
    "total": 1234
  },
  "ips": {
    "192.168.1.1": 156,
    "10.0.0.15": 89
  },
  "levels": {
    "INFO": 892,
    "ERROR": 45
  },
  "status_codes": {
    "200": 892,
    "404": 45,
    "500": 12
  },
  "top_paths": {
    "/": 156,
    "/api/login": 23,
    "/dashboard": 12
  },
  "methods": {
    "GET": 1000,
    "POST": 234
  }
}
```

## Example Usage

```bash
log-lens access.log -e report.json
jq '.status_codes."404"' report.json  # Count 404s
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `format` | string | Detected log format (`apache`, `unknown`)
| `ips` | object | IP → request count
| `status_codes` | object | HTTP status → count
| `top_paths` | object | Top 10 paths → count
| `methods` | object | HTTP method → count

---

**Stable schema** - backward compatible across versions.