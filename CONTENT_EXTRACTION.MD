# Content Extraction Feature - README Addendum

## 🆕 New Feature: Page Content Extraction

The package now supports extracting the actual content from search result pages!

### Quick Example

```python
from google_search_scraper import search

# Enable content extraction
results = search("python tutorial", max_results=3, extract_content=True)

# Access extracted content
for content in results.contents:
    print(f"Title: {content.title}")
    print(f"URL: {content.url}")
    print(f"Words: {content.word_count}")
    print(f"Content: {content.content[:500]}...")
```

### Features

✅ **Async Content Extraction** - Fetches multiple pages simultaneously for speed
✅ **Clean Content** - Removes navigation, buttons, ads, scripts automatically  
✅ **Smart Parsing** - Finds main content area (article, main, etc.)
✅ **Word Count** - Get word count for each page
✅ **Error Handling** - Gracefully handles failed extractions
✅ **Optional** - Disabled by default for speed

### Parameters

#### Python API

```python
results = search(
    query="python tutorial",
    max_results=10,
    extract_answer=True,      # Get Google's answer
    extract_content=True,     # NEW: Extract page content
    headless=True,
    timeout=30000
)
```

#### Command Line

```bash
# With content extraction
google-search "python tutorial" --extract-content

# With content extraction + save to file
google-search "machine learning" --extract-content --output results.txt

# JSON output with content
google-search "data science" --extract-content --format json > results.json
```

### What Gets Extracted

**Included:**
- Main article/content text
- Paragraphs and headings
- Lists and important text
- Page title

**Excluded (automatically removed):**
- Navigation menus
- Buttons and forms
- Advertisements
- Scripts and styles
- Sidebars and footers
- Comments

### PageContent Object

Each extracted page has:

```python
content.url          # The page URL
content.title        # Page title
content.content      # Cleaned text content
content.word_count   # Number of words
content.error        # Error message (if failed)
```

### Performance

- **Without content extraction**: 2-5 seconds
- **With content extraction (3 pages)**: 5-10 seconds
- **With content extraction (10 pages)**: 15-25 seconds

Content extraction uses async processing to fetch multiple pages simultaneously.

### Advanced Usage

```python
from google_search_scraper import GoogleSearchScraper

# Create scraper with content extraction enabled
scraper = GoogleSearchScraper(
    max_results=5,
    extract_content=True,  # Enable content extraction
    timeout=30000
)

results = scraper.search("artificial intelligence")

# Process results
for i, content in enumerate(results.contents, 1):
    if content.error:
        print(f"{i}. Failed: {content.error}")
    else:
        print(f"{i}. {content.title} ({content.word_count} words)")
        
        # Save to file
        with open(f"content_{i}.txt", "w", encoding="utf-8") as f:
            f.write(f"Title: {content.title}\n")
            f.write(f"URL: {content.url}\n\n")
            f.write(content.content)
```

### Use Cases

1. **Content Analysis** - Analyze content across multiple pages
2. **Research** - Gather information from search results
3. **Data Collection** - Extract text data for processing
4. **Summarization** - Get content for AI summarization
5. **Comparison** - Compare content across different sources

### Limitations

- Content extraction adds time (async helps)
- Some pages may block automated access
- Dynamic JavaScript content may not fully load
- Paywalled content cannot be accessed

### Tips

1. **Start small** - Test with 2-3 results first
2. **Use headless mode** - Faster than visible browser
3. **Handle errors** - Check `content.error` for failed extractions
4. **Adjust timeout** - Increase for slow-loading pages
5. **Add delays** - Respect rate limiting between searches

### Example Output

```python
results = search("python", max_results=2, extract_content=True)

# results.urls
['https://www.python.org/', 'https://docs.python.org/3/tutorial/']

# results.contents[0]
PageContent(
    url='https://www.python.org/',
    title='Welcome to Python.org',
    content='Python is a programming language that lets you work...',
    word_count=1250,
    error=None
)
```

### Installation

The feature requires `beautifulsoup4` which is automatically installed:

```bash
pip install google-search-scraper
```

All dependencies (playwright, beautifulsoup4) install automatically!

### Comparison

| Feature | extract_content=False | extract_content=True |
|---------|----------------------|---------------------|
| Speed | Fast (2-5s) | Slower (5-25s) |
| Returns | URLs only | URLs + content |
| Use case | Quick searches | Content analysis |
| Data size | Minimal | Detailed |

Choose based on your needs:
- **URLs only**: Fast lookups, link collection
- **With content**: Research, analysis, data extraction