# Quick Start Guide - Google Search Scraper Package

## 📦 Package Structure

```
google-search-scraper/
├── google_search_scraper/          # Main package
│   ├── __init__.py                 # Package exports
│   ├── scraper.py                  # Core scraping logic
│   ├── cli.py                      # Command-line interface
│   └── exceptions.py               # Custom exceptions
├── tests/                          # Test suite
│   ├── __init__.py
│   └── test_scraper.py
├── setup.py                        # Setup configuration
├── pyproject.toml                  # Modern Python packaging
├── README.md                       # Documentation
├── LICENSE                         # MIT License
├── MANIFEST.in                     # Package manifest
├── .gitignore                      # Git ignore rules
├── examples.py                     # Usage examples
└── PUBLISHING.md                   # Publishing guide

```

## 🚀 For End Users

### Installation

```bash
pip install google-search-scraper
```

### Quick Usage

```python
from google_search_scraper import search

# Simple search
results = search("python tutorial")
print(results.urls)

# Get more details
print(f"Answer: {results.answer}")
print(f"Found {results.total_results} results in {results.search_time:.2f}s")

# With content extraction
results = search("machine learning", extract_content=True)
for content in results.contents:
    print(f"{content.title}: {content.word_count} words")

# Auto-save to file
results = search("AI tutorial", extract_content=True, save_to_file=True)
# Results automatically saved to search_results.txt
```

### Command Line

```bash
# Simple search
google-search "python tutorial"

# Advanced options
google-search "machine learning" --max-results 20 --output results.txt
```

## 👨‍💻 For Developers

### Development Installation

1. **Clone/download the package:**
```bash
cd google-search-scraper
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install in development mode:**
```bash
pip install -e .
```

4. **Install Playwright browsers:**
```bash
playwright install chromium
```

5. **Install development dependencies (optional):**
```bash
pip install -e ".[dev]"
```

### Testing Your Installation

```python
# Test Python API
python -c "from google_search_scraper import search; r = search('test', max_results=3); print(f'Success! Found {len(r.urls)} results')"

# Test CLI
google-search "test query"
```

### Running Examples

```bash
python examples.py
```

### Running Tests

```bash
pytest tests/ -v
```

## 📤 Publishing to PyPI

### First Time Setup

1. **Create PyPI account:** https://pypi.org/account/register/

2. **Install build tools:**
```bash
pip install build twine
```

3. **Generate API token:** https://pypi.org/manage/account/token/

### Publishing Steps

1. **Update version** in:
   - `setup.py`
   - `pyproject.toml`
   - `google_search_scraper/__init__.py`

2. **Clean and build:**
```bash
rm -rf build/ dist/ *.egg-info
python -m build
```

3. **Upload to PyPI:**
```bash
twine upload dist/*
```

See `PUBLISHING.md` for detailed instructions.

## 🎯 Package Features

### What Makes This Package Special

✅ **Zero Configuration**
- Playwright auto-installs during package installation
- Works out of the box with sensible defaults

✅ **Dual Interface**
- Python API for programmatic use
- CLI for quick command-line searches

✅ **Stealth Mode**
- Built-in anti-detection features
- Mimics human browsing behavior

✅ **Developer Friendly**
- Clean, intuitive API
- Comprehensive error handling
- Well-documented code

✅ **Production Ready**
- Proper exception handling
- Configurable timeouts
- Result validation

## 📝 API Overview

### Main Function

```python
from google_search_scraper import search

results = search(
    query="python tutorial",
    max_results=10,           # Limit results
    extract_answer=True,      # Get Google's answer
    headless=True,            # Run invisibly
    timeout=30000             # 30 second timeout
)
```

### Advanced Usage

```python
from google_search_scraper import GoogleSearchScraper

scraper = GoogleSearchScraper(
    max_results=20,
    timeout=60000,
    headless=False,    # Visible browser for debugging
    stealth_mode=True
)

results = scraper.search("machine learning")
```

### Error Handling

```python
from google_search_scraper import search
from google_search_scraper.exceptions import RateLimitError, SearchTimeoutError

try:
    results = search("query")
except RateLimitError:
    print("Rate limited by Google")
except SearchTimeoutError:
    print("Search timed out")
```

## 🔧 Customization

### Custom User Agent

```python
scraper = GoogleSearchScraper(
    user_agent="Mozilla/5.0 (custom user agent string)"
)
```

### Adjust Timeouts

```python
# Short timeout for fast queries
results = search("quick query", timeout=10000)

# Long timeout for slow connections
results = search("complex query", timeout=60000)
```

### Skip Answer Extraction (Faster)

```python
results = search("query", extract_answer=False)
```

## 📊 Result Object

```python
results.query          # The search query
results.answer         # Google's direct answer (or None)
results.urls           # List of result URLs
results.total_results  # Number of URLs found
results.search_time    # Time taken in seconds
results.timestamp      # Unix timestamp

# Convert to dictionary
data = results.to_dict()
```

## 🎨 CLI Examples

```bash
# Basic search
google-search "python tutorial"

# Limit results
google-search "restaurants" --max-results 20

# Save to file
google-search "data science" --output results.txt

# JSON output
google-search "machine learning" --format json

# No answer extraction (faster)
google-search "quick query" --no-answer

# Visible browser (debugging)
google-search "test" --visible

# Increase timeout
google-search "slow query" --timeout 60000

# Quiet mode (results only)
google-search "query" --quiet
```

## 🐛 Troubleshooting

### Playwright Installation Issues

If Playwright doesn't auto-install:
```bash
python -m playwright install chromium
```

### Rate Limiting

If getting rate limited:
- Add delays between searches (5-10 seconds)
- Use `headless=False` for visible mode
- Consider using proxies for large-scale scraping

### Import Errors

If module not found:
```bash
pip uninstall google-search-scraper
pip install google-search-scraper
```

## 📚 Additional Resources

- **Full README:** See `README.md` for complete documentation
- **Publishing Guide:** See `PUBLISHING.md` for PyPI publishing
- **Examples:** Run `python examples.py` for usage examples
- **Tests:** Check `tests/test_scraper.py` for test examples

## 🤝 Contributing

Want to contribute?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if needed
5. Submit a pull request

## 📄 License

MIT License - see `LICENSE` file

---

**Need help?** Open an issue on GitHub or check the documentation!