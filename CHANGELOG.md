# Changelog - HTA Schema Tools

All notable changes to HTA Schema Tools will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned for v1.1
- PSA computation in viewer
- One-way sensitivity analysis
- Tornado diagrams
- Cost-effectiveness plane visualization

### Planned for v1.2
- Excel export of results
- CSV export of parameters
- Batch model processing

### Planned for v2.0
- Support for HTA Schema v0.2 (Markov models)
- Interactive tree visualization
- Graphical model editor (beta)

## [1.0.0] - 2024-12-12

### Added - Web Viewer
- Initial release of web-based viewer
- Model loading via drag-and-drop
- Base case deterministic analysis
  - Backward induction through decision tree
  - Expected value calculation at chance nodes
  - Cost accumulation with discounting
  - QALY calculation with discounting
- ICER computation
- Results display
  - Strategy comparison cards
  - Cost and QALY breakdowns
  - Incremental cost-effectiveness ratio
- Model visualization
  - Metadata display
  - Node structure viewer (simplified)
  - Parameter table with sources
- Professional styling with custom design
- Browser-based (no installation required)
- Works offline after initial load
- Supports HTA Schema v0.1 (decision trees)

### Added - Python Validator
- Command-line validation tool
- Structural validation
  - JSON Schema conformance
  - Tree properties (no cycles, single root)
  - Node connectivity
  - Path termination
- Probability validation
  - Chance node probability sums
  - Probability ranges [0, 1]
- Parameter validation
  - Reference resolution
  - Type checking
  - Bounds validation
  - Distribution parameter validation
- Semantic validation
  - Cost reasonableness checks
  - Utility range warnings
  - Parameter source documentation
- Detailed error reporting
- Warning system for potential issues

### Added - Examples
- Stroke thrombolysis vs standard care
  - Complete model with 31 parameters
  - Based on NINDS trial data
  - Demonstrates all schema features
  - Expected ICER ~£7,500/QALY

### Documentation
- Viewer user guide
- Demo presentation script
- Contributing guidelines
- README with roadmap

## Tool Versioning

Tool versions are independent of schema versions:

- **Schema v0.1** → Supported by Viewer v1.x, Validator v1.x
- **Schema v0.2** → Will be supported by Viewer v2.x, Validator v2.x

### Compatibility Matrix

| Tool Version | Schema v0.1 | Schema v0.2 | Schema v1.0 |
|--------------|-------------|-------------|-------------|
| Viewer 1.0   | ✓          | ✗           | ✗           |
| Validator 1.0| ✓          | ✗           | ✗           |

## Release Notes

### v1.0.0 - Initial Release

**Viewer Features:**
- Drag-and-drop model loading
- Instant ICER calculation
- Professional interface
- Works in all modern browsers

**Validator Features:**
- Comprehensive structural checks
- Parameter validation
- Clear error messages
- Fast execution (< 1 second)

**Limitations:**
- No PSA computation yet
- No sensitivity analysis visualization
- Simplified tree display
- No model editing

**Next Priority:**
Adding PSA computation and sensitivity analysis visualization in v1.1

---

For the schema specification, see [hta-schema repository](https://github.com/[username]/hta-schema)
