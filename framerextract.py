import requests
import zipfile
from urllib.parse import urljoin

BASE_URL = input("The (framer.website) url with a trailing slash in the end, like (https://mysite.framer.website/): ")
URL_PATHS = input("Enter valid urls like (/about or just / for home) seperted by spaces: ".split(" "))
SNIPPET_TO_REMOVE = input("Enter the snippet to remove: ")
OUTPUT_ZIP_FILE = "htmltemplates.zip"

print("Starting extraction")

def fetch_and_zip():
    with zipfile.ZipFile(OUTPUT_ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for path in URL_PATHS:
            full_url = urljoin(BASE_URL, path)
            try:
                response = requests.get(full_url)
                response.raise_for_status()
                
                html_content = response.text
                clean_html = html_content.replace(SNIPPET_TO_REMOVE, "")
                
                clean_path = path.strip("/")
                
                archive_name = clean_path if clean_path else "index"
                
                if not archive_name.endswith(".html"):
                    archive_name += ".html"
                
                zip_file.writestr(archive_name, clean_html)
            except requests.RequestException:
                pass

print("Suceeded! Check htmltemplates.zip!")

if __name__ == "__main__":
    fetch_and_zip()
