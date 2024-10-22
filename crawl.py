import asyncio
from urllib.parse import urlparse
from crawl4ai import AsyncWebCrawler

# Dictionary mapping TLDs to wait_for predicates
WAIT_FOR_PREDICATES = {
    "myworkdayjobs.com": """
    () => {
        const element = document.querySelector('div[data-automation-id="jobPostingDescription"]');
        if (!element) return false;
        // Check if the element has content
        const content = element.textContent || element.innerText;
        return content.trim().length > 0;
    }
    """
}

# Default wait_for predicate for domains without a specific one
DEFAULT_WAIT_FOR = """
() => {
    return document.readyState === 'complete';
}
"""


def get_wait_for_predicate(domain):
    for tld, predicate in WAIT_FOR_PREDICATES.items():
        if domain.endswith(tld):
            return tld, predicate
    return "Default", DEFAULT_WAIT_FOR


def get_domain(url):
    return urlparse(url).netloc


def get_user_url():
    return input("Enter the URL to crawl: ").strip()


async def crawl_url(crawler, url):
    domain = get_domain(url)
    print(domain)
    wait_for_name, wait_for_predicate = get_wait_for_predicate(domain)

    result = await crawler.arun(
        url=url,
        wait_for=wait_for_predicate,
        bypass_cache=True
    )

    assert result.success, f"Failed to crawl the page: {url}"

    filename = f"output.md"
    with open(filename, "w") as f:
        f.write(result.markdown or "No content.")

    print(f"Crawled {url} and saved content to {filename}")
    print(f"Used wait_for predicate: {wait_for_name}")


async def main():
    url = get_user_url()

    if not url:
        print("No URL provided. Exiting.")
        return

    async with AsyncWebCrawler(verbose=True) as crawler:
        await crawl_url(crawler, url)


if __name__ == "__main__":
    asyncio.run(main())
