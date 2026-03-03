# Log Lens Development Roadmap

## Project Overview

**Log Lens** is a lightweight CLI for analyzing web server logs (Apache/Nginx). The project has matured significantly since its initial release, with core features now validated by a modular architecture and Pydantic models.

---

## Phase 1: MVP Polish (v0.1 → v0.2)
**Goal:** Stabilize core features and improve reliability
**Status:** ✅ Completed (March 2026)

### Completed
- ✅ **Refactor parser module**: Extracted logic and integrated with Pydantic.
- ✅ **Expand test coverage**: Reached 95% test coverage for core modules.
- ✅ **Improved CLI**: Enhanced reporting with Rich tables and Click integration.
- ✅ **Documentation**: Finalized `ARCHITECTURE.md`, `DEVELOPMENT.md`, and added `GEMINI.md`.

---

## Phase 2: Extended Analysis (v0.2 → v0.3+)
**Goal:** Add deeper analytics and filtering
**Status:** 🟡 In Progress

### Completed
- ✅ **Advanced analytics**: Status code distribution, IP counts, and top paths.
- ✅ **Modular Reporter**: Separated terminal display logic into `reporter.py`.
- ✅ **Type Safety**: Full migration to type hints and Mypy compliance.

### In Progress / Todo
- [ ] **Filtering and querying**
  - `--filter-ip` to exclude/include specific IPs
  - `--filter-status` to focus on specific HTTP codes
  - `--filter-path` for path-based queries
- [ ] **Export enhancements**
  - Re-integrate JSON export for the new architecture.
  - CSV export option.
  - HTML report generation.
- [ ] **Nginx-specific patterns**: While Apache combined format works for most Nginx logs, explicit Nginx patterns are planned for v0.8.0.

---

## Phase 3: Web Dashboard (v0.3 → v0.4)
**Goal:** Interactive visualization and real-time monitoring
**Timeline:** 3–4 weeks

### Features
- [ ] **Local web dashboard**
  - FastAPI backend with WebSocket support
  - Vue.js or React frontend
  - Real-time log tailing (WebSocket)
  - Interactive charts (Chart.js or D3.js)
  - Drill-down analytics (click IP → see all requests from that IP)
- [ ] **Log file watching**
  - Auto-detect new logs and stream updates
  - Configurable watch directory
- [ ] **Session management**
  - Save analysis sessions
  - Export/share session reports

### Architecture
```
log-lens/
├── src/log_lens/
│   ├── core/          # Core parsing, filtering, analytics
│   ├── cli/           # CLI commands (existing)
│   ├── api/           # FastAPI backend (new)
│   │   ├── routes/
│   │   ├── models/
│   │   └── websocket/
│   └── web/           # Frontend assets (new)
│       ├── src/
│       └── public/
└── ...
```

---

## Phase 4: Advanced Features (v0.4 → v1.0)
**Goal:** Production-ready tool for DevOps/Security teams
**Timeline:** 4–6 weeks

### Features
- [ ] **Security analysis**
  - Suspicious activity detection (brute-force patterns, SQL injection signatures)
  - Anomaly detection (unusual request patterns)
  - Threat level scoring per IP
  - GeoIP lookups (optional)
- [ ] **Scheduled reports**
  - Email digest generation
  - Slack/Teams webhook integration
  - S3/GCS export for archival
- [ ] **Alerting**
  - Threshold-based alerts (e.g., 404 rate > 10%)
  - Custom rule engine
  - Integration with monitoring systems (Prometheus, Grafana)
- [ ] **Multi-file analysis**
  - Combine logs from multiple servers
  - Distributed analysis (optional)

### Release Criteria
- 100% test coverage for core modules
- Official Docker image on Docker Hub
- Comprehensive documentation with examples
- Performance tested on 1GB+ logs
- Security audit completed

---

## Post-v1.0 (Future Enhancements)

### Nice-to-have features
- [ ] Machine learning-based anomaly detection
- [ ] Compliance reports (GDPR, PCI-DSS, HIPAA)
- [ ] Multi-tenant SaaS deployment guide
- [ ] Kubernetes operator for log aggregation
- [ ] gRPC API for high-performance integrations
- [ ] Mobile app for monitoring

---

## Testing & Quality Assurance

Maintained at each phase:
- **Unit tests:** Target 90%+ code coverage
- **Integration tests:** Test CLI end-to-end with fixtures
- **Performance tests:** Ensure sub-second analysis on 100MB+ logs
- **Security:** Regular dependency scanning (Dependabot)
- **Code quality:** Black, isort, pylint, mypy

---

## Release Schedule

| Version | Target Date | Status |
|---------|-------------|--------|
| v0.1.0  | Dec 2025    | Initial release |
| v0.4.0  | Dec 2025    | Performance & CI |
| v0.6.0  | Feb 2026    | Click & Ruff migration |
| v0.7.1  | Mar 2026    | Current Stable |
| v1.0.0  | Apr 2026    | Production-ready |

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines. We follow:
- Semantic versioning
- Conventional commits
- GitHub flow (feature branches)
- Code review required for all PRs

---

## Questions?

Open an issue with the `question` label or start a discussion in the GitHub repo.
