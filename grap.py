# this takes a URL and places it, with it's expaned CSS, into the clipboard so that it cab be pasted into JSFiddle for debugging

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import subprocess

def fetch_and_inline_css(url):
    response = requests.get(url)
    response.raise_for_status()
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    head = soup.head or soup.new_tag("head")
    css_blocks = []

    for link_tag in soup.find_all('link', rel='stylesheet'):
        href = link_tag.get('href')
        full_url = urljoin(url, href)
        try:
            css_response = requests.get(full_url)
            css_response.raise_for_status()
            css_blocks.append(css_response.text)
        except Exception as e:
            print(f"⚠️ Could not fetch CSS from {full_url}: {e}")
        link_tag.decompose()

    if css_blocks:
        style_tag = soup.new_tag('style')
        style_tag.string = '\n\n'.join(css_blocks)
        head.append(style_tag)

    final_html = f"<!DOCTYPE html>\n<html>\n{str(head)}\n{str(soup.body)}\n</html>"
    return final_html

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 inline_page.py https://example.com")
    else:
        url = sys.argv[1]
        result = fetch_and_inline_css(url)

        # Save to file
        with open("inlined.html", "w", encoding="utf-8") as f:
            f.write(result)
        print("✅ Inlined page saved to inlined.html")

        # Copy to clipboard using xclip
        try:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=result.encode('utf-8'), check=True)
            print("📋 Inlined HTML copied to clipboard.")
        except Exception as e:
            print(f"❌ Could not copy to clipboard: {e}")
