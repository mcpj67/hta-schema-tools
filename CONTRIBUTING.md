# Contributing to HTA Schema

Thank you for your interest in contributing to HTA Schema! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest features
- Check existing issues before creating a new one
- Provide clear descriptions with examples when possible

### Proposing Schema Changes

Schema changes follow a formal process:

1. **Open a GitHub Issue** describing the proposed change
2. **Discussion Period**: Minimum 30 days for community feedback
3. **Technical Review**: Working group evaluates technical implications
4. **Vote**: Requires majority approval from core contributors
5. **Implementation**: Update schema, documentation, and examples

### Pull Requests

We welcome pull requests for:
- Bug fixes in validators or examples
- Documentation improvements
- New example models
- Tool integrations (R/Python/Excel converters)

**Before submitting:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes with clear commit messages
4. Test your changes (run validators, check examples)
5. Update relevant documentation
6. Submit PR with description of changes

### Example Model Contributions

We're building a library of validated example models. To contribute:

1. Create model in HTA Schema format (JSON)
2. Validate using `hta_validator.py`
3. Include metadata (citations, data sources)
4. Add brief description in PR

**Example model requirements:**
- Based on published research (provide citations)
- Validates without errors
- Demonstrates specific features or clinical areas
- Includes realistic parameter values with sources

### Code Style

**Python:**
- Follow PEP 8
- Use type hints where applicable
- Include docstrings for functions/classes
- Maximum line length: 100 characters

**JSON:**
- Use 2-space indentation
- Keep parameter IDs descriptive but concise
- Include metadata and sources

## Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/hta-schema.git
cd hta-schema

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (when requirements.txt exists)
pip install -r requirements.txt

# Run validator on examples
python hta_validator.py example_stroke_thrombolysis.json
```

## Testing

Before submitting PRs:

1. **Validation**: All example models must pass validation
   ```bash
   python hta_validator.py examples/*.json
   ```

2. **JSON Schema**: Validate against formal schema
   ```bash
   # Using jsonschema (Python)
   python -c "import jsonschema, json; 
   jsonschema.validate(
       json.load(open('example.json')), 
       json.load(open('hta_schema_v0.1.json'))
   )"
   ```

## Documentation

When adding features:
- Update technical specification
- Add examples to README
- Update changelog
- Consider adding tutorial or guide

## Communication

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Mailing List**: [To be set up]

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and harassment-free experience for everyone.

### Our Standards

**Positive behaviors:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Accepting constructive criticism gracefully
- Focusing on what's best for the community

**Unacceptable behaviors:**
- Harassment, trolling, or derogatory comments
- Publishing others' private information
- Other conduct inappropriate in a professional setting

### Enforcement

Violations may be reported to [contact email]. All reports will be reviewed and investigated.

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in release notes
- Credited in academic publications citing the schema

## Questions?

Feel free to:
- Open a GitHub Discussion
- Email: [contact email to be added]
- Join community calls: [schedule to be determined]

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0 for the Community Edition.

**Note:** Advanced features and commercial editions remain proprietary. Open-source contributions apply only to the Community Edition tools. If you're interested in contributing to commercial features, please contact us directly.
