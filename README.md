# HTA Schema Tools

**Professional tools for working with HTA Schema models**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Schema Version](https://img.shields.io/badge/schema-v0.1-green.svg)](https://github.com/[username]/hta-schema)

## Overview

This repository provides production-ready tools for creating, validating, executing, and visualizing HTA Schema models. These tools implement the [HTA Schema Specification](https://github.com/[username]/hta-schema) and are designed for professional use in health economics research, pharmaceutical submissions, and HTA agency reviews.

## Tools Included

### 1. Web Viewer & Computation Engine 🌐
**File:** `viewer/hta_viewer.html`

Browser-based tool that:
- Loads and displays HTA Schema models
- Computes cost-effectiveness results (ICER, incremental costs/QALYs)
- Shows parameter tables with sources
- Visualizes decision tree structure
- Performs deterministic base case analysis

**No installation required** - works in any modern browser.

### 2. Python Validator ✓
**File:** `validator/hta_validator.py`

Command-line validator that checks:
- JSON Schema conformance
- Structural validity (tree properties, node connectivity)
- Probability constraints (sum to 1.0)
- Parameter references and types
- Semantic validation (reasonable ranges)

```bash
python hta_validator.py model.json
```

### 3. Example Models 📊
**Directory:** `examples/`

Production-quality example models demonstrating best practices:
- Stroke thrombolysis vs standard care
- [More examples coming]

Each example includes:
- Complete model specification
- Parameter sources and citations
- Expected results for validation

## Quick Start

### Option 1: Try the Viewer (Easiest)
1. Download `viewer/hta_viewer.html`
2. Double-click to open in browser
3. Drag an example model onto the page
4. View computed results instantly

### Option 2: Validate a Model
```bash
# Install Python 3.7+
python validator/hta_validator.py examples/stroke_thrombolysis.json
```

### Option 3: Convert Your Model
[Coming soon: Excel/TreeAge/R converters]

## Features by Tool

| Feature | Viewer | Validator | Converter* |
|---------|--------|-----------|------------|
| Load JSON models | ✓ | ✓ | ✓ |
| Validate structure | ✓ | ✓ | ✓ |
| Compute ICER | ✓ | ✗ | ✗ |
| PSA analysis | ✗** | ✗ | ✗ |
| One-way SA | ✗** | ✗ | ✗ |
| Export results | ✗** | ✗ | ✗ |
| Graphical editing | ✗** | ✗ | ✗ |

\* Coming soon  
\*\* Available in Pro version

## Licensing

### Current: Open Source (Apache 2.0)
Basic tools are open source to encourage adoption and community feedback.

### Future: Dual Licensing Model

We're developing advanced features for commercial use:

**Community Edition (Free & Open Source):**
- Basic viewer
- Validation tools
- Simple examples
- Import/export for basic models

**Professional Edition (Commercial License):**
- Advanced computation engine with PSA
- Sensitivity analysis visualization (tornado, CE plane)
- Graphical model builder
- Batch processing
- API access
- Priority support

**Enterprise Edition (Commercial License + Services):**
- On-premise deployment
- Custom integrations (TreeAge, R, Excel, Simul8)
- Consulting services
- Training and workshops
- SLA guarantees

## Roadmap

### Completed ✓
- Web viewer with base case computation
- Python validator
- Basic example models
- Documentation

### Q1 2025
- [ ] PSA computation engine
- [ ] R package for import/export
- [ ] Excel add-in (beta)
- [ ] 10+ example models across therapeutic areas

### Q2 2025
- [ ] Graphical model builder (web-based)
- [ ] Cloud API for validation and execution
- [ ] Sensitivity analysis visualizations
- [ ] TreeAge converter

### Q3 2025
- [ ] Support for Markov models (schema v0.2)
- [ ] Advanced optimization features
- [ ] Component marketplace (beta)
- [ ] Enterprise deployment options

### Q4 2025
- [ ] EVPI calculations
- [ ] Automated report generation
- [ ] Multi-model comparisons
- [ ] v1.0 stable release

## Commercial Services

We offer professional services for organizations:

### Consulting
- Model development and review
- Migration from existing tools
- Custom tool development
- Training and workshops

### Pilot Programs
Currently seeking partners for:
- Pharmaceutical submissions
- HTA agency reviews
- Academic research projects
- Consultancy integrations

**Contact:** [email to be added]

## Installation

### Viewer (No Installation)
Download `viewer/hta_viewer.html` and open in browser.

### Validator
```bash
# Clone repository
git clone https://github.com/[username]/hta-schema-tools.git
cd hta-schema-tools

# Run validator
python validator/hta_validator.py examples/stroke_thrombolysis.json
```

### Future: Python Package
```bash
pip install hta-schema-tools  # Coming Q1 2025
```

## Documentation

- **Viewer Guide:** `docs/VIEWER_GUIDE.md`
- **Validator Guide:** `docs/VALIDATOR_GUIDE.md`
- **Demo Script:** `docs/DEMO_SCRIPT.md`
- **API Documentation:** Coming soon

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Bug reports and feature requests
- Code contributions
- Example model submissions
- Documentation improvements

**Note:** Commercial features remain proprietary. Open-source contributions apply to Community Edition only.

## Business Model

### Why Open Core?
- **Open specification** drives adoption
- **Open basic tools** build community trust
- **Commercial advanced tools** sustain development

### Revenue Streams
1. **SaaS subscriptions** (Pro/Enterprise tiers)
2. **Professional services** (consulting, training)
3. **Component marketplace** (revenue sharing with creators)
4. **Enterprise licenses** (on-premise deployment)

This model ensures:
- Free tools for researchers and students
- Sustainable development funding
- Continuous innovation
- Professional support for commercial users

## Support

### Community Support (Free)
- GitHub Issues for bugs
- GitHub Discussions for questions
- Community forum [coming soon]

### Professional Support (Paid)
- Email support with SLA
- Priority bug fixes
- Custom feature development
- Training and consultation

Contact: [email to be added]

## Comparison to Existing Tools

| Feature | HTA Schema Tools | TreeAge | Excel | R (heemod) |
|---------|------------------|---------|-------|------------|
| Open format | ✓ | ✗ | Partial | ✓ |
| Validation | ✓ | Partial | ✗ | Partial |
| Version control | ✓ | ✗ | ✗ | ✓ |
| Web-based | ✓ | ✗ | ✗ | ✗ |
| Graphical UI | Coming | ✓ | ✓ | ✗ |
| Cost | Free/Paid | $$$ | $ | Free |

## Citation

```
McMeekin P. (2024). HTA Schema Tools: Professional Tools for Health 
Technology Assessment Modeling. https://github.com/[username]/hta-schema-tools
```

## License

**Community Edition:** Apache License 2.0 (see LICENSE)

**Professional/Enterprise Editions:** Commercial license required (contact for pricing)

Advanced features and commercial services are proprietary.

## Partners & Customers

[Space for logos once you have paying customers]

## Media & Publications

- Methods paper (in preparation)
- ISPOR presentation (planned)
- Blog post: "Why HTA Needs Standardization"

---

**For the specification:** See [hta-schema](https://github.com/[username]/hta-schema)  
**For commercial inquiries:** [contact to be added]  
**For collaboration:** Open an issue or discussion

## Schema Support

- **v0.1.1**: Full support including expression language validation
- **v0.1.0**: Full support (backward compatible)

### Expression Language (v0.1.1+)

The enhanced validator supports complex expressions:
```python
# Validate models with expressions
from validator.expression_validator import validate_model_expressions

is_valid, errors = validate_model_expressions(model)
```

See [Implementation Summary](docs/IMPLEMENTATION_SUMMARY.md) for details.