import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from urllib.parse import quote

async def is_url_valid(url: str) -> bool:
    encoded_url = quote(url)  # URL'yi URL encode edin
    url = f"https://transparencyreport.google.com/safe-browsing/search?url={encoded_url}"

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(url)

        # Sayfanın tam yüklenmesini beklemek için bir süre bekleyin.
        await page.wait_for_load_state("networkidle")

        page_content = await page.content()
        await browser.close()

    soup = BeautifulSoup(page_content, "html.parser")

    clean_html = soup.prettify()
    if "No available data" not in clean_html:
        return True
    else:
        return False


