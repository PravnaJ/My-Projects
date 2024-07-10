import requests
from bs4 import BeautifulSoup
def extract_data(url):
    # Send a GET request to the URL
    response = requests.get(url)    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')     
        # Example: Extracting main data parts
        # Replace these with the actual elements you want to extract
        main_title = soup.find('h1').text.strip() if soup.find('h1') else 'No title found'
        main_paragraph = soup.find('p').text.strip() if soup.find('p') else 'No paragraph found'
        # Return the extracted data (you can format it as needed)
        return {
            'title': main_title,
            'paragraph': main_paragraph
        }
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example usage:
    n = int(input("Enter how many websites data do you want scrap: "))
    urls = []
    for i in range(n):
        input_url = input(f"Enter URL NO.{i}: ")
        urls.append(input_url)
    e_data = []
    for i in range(len(urls)):
        data = extract_data(urls[i])
        if data:
            e_data.append(data)
    if e_data:
        print("Extracted Data:")
        for data in e_data:
            print(f"Title: {data['title']}")
            print(f"Main Paragraph: {data['paragraph']}")
            print()
