
# HTML to Text Cleansing

## Description
When mining text from web pages, an important preprocessing step is to strip the respective HTML page of all structural elements (e.g., tags, scripts, styles) and extract the plain textual content. **HTML Information Extraction** is a Python-based toolkit that automates this process and provides a structured JSON object for each HTML file, containing key components like the title, description, and main text.

By distilling the essence of a web page into a concise and meaningful representation, this toolkit offers a brief yet informative overview of the story or context behind the content. It employs two extraction methods—**NewsPlease** and **Trafilatura**—to ensure flexibility and accuracy across diverse content types. Whether analyzing news articles, building text corpora, or conducting sentiment analysis, this tool serves as a powerful preprocessing resource for social science researchers, computational linguists, and data scientists.

## Use Cases
- To study media bias in online news articles. The toolkit to extract and analyze HTML files to analyze patterns of bias in reporting styles across different sources
- To investigate the evolution of public discourse on climate change. The textual data is collected as HTML files from various online news sources, facilitating sentiment analysis and topic modeling
- To build a corpus of web-scraped articles for training models on natural language understanding 

## Input Data
Downloaded webpages as HTML files. Sample input files are in `html/` directory.

## Output Data
`html_json_trafilatura.json`: A JSON file with the extracted main text and metadata.

A sample entry in the JSON output:
  
  ```json
  {
     "title": "Sample News Article",
     "description": "A brief overview of the article content.",
     "main_text": "This is the main body of the article...",
     "filename": "sample.html"
  }
  ```

## Environment Setup
- Python version: **3.6 or higher** is required.
- Install the dependencies listed in `requirements.txt`:

  ```bash
    pip install -r requirements.txt
  ```

**Dependencies**

- [NewsPlease](https://github.com/fhamborg/news-please): For extracting news content.
- [Trafilatura](https://github.com/adbar/trafilatura): For general text extraction from HTML.

### How to Use
**(a) Using NewsPlease**

1. Place your HTML files in the `html/` directory.
2. Run the script with the following command:
  
  ```bash
    python NewsPlease.py
  ```

3. Output:
   - `html_json_news.json`: A JSON file containing extracted news information (title, description, main text).

**(b) Using Trafilatura**

1. Place your HTML files in the `html/` directory.
2. Execute the script with:
  
  ```bash
    python Trafilatura.py
  ```

3. Output:
   - `html_json_trafilatura.json`: A JSON file with the extracted main text and metadata.

**error handling**
- Both scripts include basic error handling to skip files that cannot be processed.
- If issues arise, error messages will be printed, and the script will continue processing the remaining files.

## Acknowledgements
Special thanks to the developers of **NewsPlease** and **Trafilatura** for providing powerful libraries that make HTML content extraction straightforward and efficient.
If you use this tool for research purposes, please consider citing the respective libraries:
- [NewsPlease](https://github.com/fhamborg/news-please)
- [Trafilatura](https://github.com/adbar/trafilatura)
  
## Disclaimer
This tool is provided as-is for academic and research purposes. Users are responsible for ensuring compliance with applicable laws and website terms of service when scraping content.

## Contact Details
For further queries, please contact [Po-Chun.Chang@gesis.org](Po-Chun.Chang@gesis.org)
