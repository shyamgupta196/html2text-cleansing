import json
import multiprocessing
import os
import re

import trafilatura as trafilatura

BASE_URI = 'html/'


def clean_text(text):
    cleaned_text = re.sub(r"\s+", " ", text)
    cleaned_text = cleaned_text.strip()
    cleaned_text = cleaned_text.replace("- ", "")
    return cleaned_text


def extract_text(filename):
    json_object = {}
    print(filename)
    with open(BASE_URI + filename, 'r', encoding='utf-8') as file:
        try:
            html_content = file.read()
            result = trafilatura.extract(html_content, no_fallback=True, include_links=False, include_comments=False,
                                         include_tables=False, include_images=False, include_formatting=True)
            metadata = trafilatura.extract_metadata(html_content)
            json_object['title'] = metadata.title
            json_object['main_text'] = clean_text(result)
            json_object['filename'] = filename
        except Exception as e:
            print("Error processing", filename)
            print("Exception:", str(e))

    return json_object


if __name__ == '__main__':
    pool = multiprocessing.Pool(os.cpu_count())
    res = pool.map(extract_text, os.listdir(BASE_URI))
    with open('html_json_trafilatura.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
    print("JSON data written to 'html_json_trafilatura.json'")
