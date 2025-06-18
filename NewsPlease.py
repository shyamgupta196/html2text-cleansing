import json
import multiprocessing
import os

from newsplease import NewsPlease

# Define the base directory path where HTML files are located
BASE_URI = 'html/'


def news_it(filename):
    """
    Extracts news information from HTML files and creates a JSON object.

    Args:
        filename (str): The name of the HTML file to process.

    Returns:
        dict: A dictionary containing extracted news information or an empty dictionary if extraction fails.
    """
    json_object = {}  # Initialize an empty dictionary to store news information
    print(filename)

    # Open and read the HTML file
    with open(BASE_URI + filename, 'r', encoding='utf-8') as file:
        try:
            # Use NewsPlease to parse the HTML content and extract news information
            news = NewsPlease.from_html(file.read())
            json_object['title'] = news.title
            json_object['description'] = news.description
            json_object['main_text'] = news.maintext
            json_object['language'] = news.language
            json_object['filename'] = filename
        except Exception as e:
            print("Error processing", filename)
            print("Exception:", str(e))

    return json_object


if __name__ == '__main__':
    # Create a multiprocessing pool with the number of available CPU cores
    pool = multiprocessing.Pool(os.cpu_count())

    # Process the list of HTML files using the news_it function in parallel
    res = pool.map(news_it, os.listdir(BASE_URI))

    # Write the extracted news information to a JSON file
    with open('html_json_news.json', 'w', encoding='utf-8') as f:
        # Serialize the list of dictionaries as a JSON array in the output file
        json.dump(res, f, ensure_ascii=False, indent=4)

    print("JSON data written to 'html_json_news.json'")
