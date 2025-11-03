"""
Example usage of google-search-scraper package
"""

from google_search_scraper import search, GoogleSearchScraper
from google_search_scraper.exceptions import GoogleSearchError
import time


def example_basic_usage():
    """Basic usage example"""
    print("\n" + "="*70)
    print("Example 1: Basic Usage")
    print("="*70)
    
    results = search("python tutorial")
    
    print(f"\nQuery: {results.query}")
    print(f"Search time: {results.search_time:.2f}s")
    
    if results.answer:
        print(f"\nAnswer: {results.answer[:200]}...")
    
    print(f"\nTop {len(results.urls)} URLs:")
    for i, url in enumerate(results.urls[:5], 1):
        print(f"{i}. {url}")


def example_custom_scraper():
    """Custom scraper example"""
    print("\n" + "="*70)
    print("Example 2: Custom Scraper Configuration")
    print("="*70)
    
    scraper = GoogleSearchScraper(
        max_results=5,
        timeout=20000,
        headless=True,
        stealth_mode=True
    )
    
    results = scraper.search("machine learning", extract_answer=True)
    
    print(f"\nFound {results.total_results} results")
    print(f"Time: {results.search_time:.2f}s")
    print("\nURLs:")
    for url in results.urls:
        print(f"  - {url}")


def example_multiple_searches():
    """Multiple searches example"""
    print("\n" + "="*70)
    print("Example 3: Multiple Searches")
    print("="*70)
    
    queries = ["python", "javascript", "rust"]
    
    for query in queries:
        print(f"\nSearching: {query}")
        results = search(query, max_results=3)
        print(f"  Results: {len(results.urls)}")
        if results.urls:
            print(f"  Top result: {results.urls[0]}")
        
        # Be respectful - add delay
        time.sleep(2)


def example_error_handling():
    """Error handling example"""
    print("\n" + "="*70)
    print("Example 4: Error Handling")
    print("="*70)
    
    try:
        # This might fail with very short timeout
        results = search("test query", timeout=1000)
        print(f"Success! Found {len(results.urls)} results")
    except GoogleSearchError as e:
        print(f"Caught error (expected): {type(e).__name__}")
        print(f"Message: {e}")


def example_result_dict():
    """Convert results to dictionary example"""
    print("\n" + "="*70)
    print("Example 5: Convert to Dictionary")
    print("="*70)
    
    results = search("web scraping", max_results=3)
    
    # Convert to dict for JSON serialization
    result_dict = results.to_dict()
    
    print(f"\nResult dictionary keys: {list(result_dict.keys())}")
    print(f"Query: {result_dict['query']}")
    print(f"Total results: {result_dict['total_results']}")
    print(f"First URL: {result_dict['urls'][0] if result_dict['urls'] else 'N/A'}")


def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("Google Search Scraper - Usage Examples")
    print("="*70)
    
    examples = [
        ("Basic Usage", example_basic_usage),
        ("Custom Scraper", example_custom_scraper),
        ("Multiple Searches", example_multiple_searches),
        ("Error Handling", example_error_handling),
        ("Result Dictionary", example_result_dict),
    ]
    
    for name, example_func in examples:
        try:
            example_func()
            time.sleep(3)  # Delay between examples
        except KeyboardInterrupt:
            print("\n\nExamples cancelled by user")
            break
        except Exception as e:
            print(f"\nExample '{name}' failed: {e}")
    
    print("\n" + "="*70)
    print("Examples completed!")
    print("="*70)


if __name__ == "__main__":
    main()