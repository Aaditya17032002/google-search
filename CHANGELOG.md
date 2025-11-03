# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2024-11-03

### Added
- **Auto-save to file**: New `save_to_file` and `output_file` parameters in `search()` function
- **Manual save method**: `SearchResult.save_to_file()` method to save results manually
- Comprehensive file output format with full content extraction
- File includes: query info, Google's answer, all URLs, and complete page content

### Changed
- File saves **replace** previous content (not append) for each new query
- Enhanced documentation with new features

### Features
- Auto-save extracted content to text files
- Customizable output filenames
- Formatted output with sections for easy reading
- Full content storage (not just previews)

## [1.0.3] - 2024-11-03

### Added
- **Content extraction feature**: Extract and analyze full page content from search results
- `extract_content` parameter in `search()` function
- `PageContent` dataclass for storing extracted content
- Async content extraction for better performance
- BeautifulSoup4 dependency for HTML parsing
- Content cleaning and text extraction
- Word count calculation for each page
- Error handling for failed content extraction

### Fixed
- AsyncIO event loop conflict when extracting content
- Added `concurrent.futures.ThreadPoolExecutor` for async operations
- Proper handling of existing event loops

### Dependencies
- Added `beautifulsoup4>=4.12.0` as required dependency

## [1.0.2] - 2024-11-03

### Fixed
- Added missing `beautifulsoup4` dependency to package requirements
- Updated pyproject.toml and setup.py with correct dependencies

## [1.0.1] - 2024-11-03

### Changed
- Updated GitHub repository URLs in package metadata
- Fixed author information in setup.py

## [1.0.0] - 2024-11-03

### Added
- Initial release of google-search-scraper
- Fast Google search scraping with stealth mode
- Python API with simple `search()` function
- Advanced `GoogleSearchScraper` class for customization
- Command-line interface (`google-search` command)
- Automatic Playwright browser installation
- Google's direct answer extraction
- Top N results extraction (configurable)
- Multiple output formats (text and JSON)
- Comprehensive error handling with custom exceptions
- Rate limit detection
- Timeout configuration
- Headless and visible browser modes
- User agent customization
- Result caching with timestamp
- SearchResult dataclass with dict conversion
- MIT License
- Full documentation in README.md
- Usage examples in examples.py
- Test suite with pytest
- Publishing guide for PyPI
- .gitignore for Python projects

### Features
- **Fast Performance**: Optimized for speed with minimal delays (2-5 seconds typical)
- **Stealth Mode**: Anti-detection features to avoid Google blocking
- **Developer Friendly**: Clean, intuitive API with type hints
- **Production Ready**: Proper exception handling and validation
- **Flexible**: CLI and Python API for different use cases
- **Zero Config**: Works out of the box with auto-installation

### Supported
- Python 3.8+
- Windows, macOS, Linux
- Playwright 1.40.0+

## [Unreleased]

### Planned Features
- [ ] Async/await support for concurrent searches
- [ ] Proxy rotation support
- [ ] Custom browser configuration
- [ ] Image search support
- [ ] News search support
- [ ] Video search support
- [ ] Advanced filtering options
- [ ] Search result caching
- [ ] Rate limiting with backoff
- [ ] Progress callbacks
- [ ] Batch search utilities
- [ ] Export to CSV/Excel
- [ ] Google Scholar support
- [ ] More stealth techniques
- [ ] Docker support

### Known Issues
- Playwright auto-install may fail on some systems (manual install required)
- Rate limiting may occur with frequent searches (add delays)
- CAPTCHA detection not implemented (manual resolution needed)

---

## Version History

### Version Numbering

We use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking API changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### How to Report Issues

Found a bug or have a feature request?
1. Check existing issues on GitHub
2. Create a new issue with details
3. Include version, Python version, and OS

### How to Contribute

Contributions welcome! See CONTRIBUTING.md (coming soon) for guidelines.