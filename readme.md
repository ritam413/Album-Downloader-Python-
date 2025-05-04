# Image Downloader from Website

This Python script downloads all images from a specified web page and saves them into a designated folder on your local machine.

## Features

- Extracts all image (`<img>`) tags from a given URL.
- Resolves relative image paths into absolute URLs.
- Downloads and saves images in a specified folder.
- Supports downloading from multiple websites by calling the function multiple times.

## Dependencies

This script requires the following Python libraries:

- `requests` — for making HTTP requests
- `beautifulsoup4` — for parsing HTML content
- `lxml` (optional, but recommended for faster HTML parsing)
  
You can install the dependencies using pip:

```bash
pip install requests beautifulsoup4 lxml
