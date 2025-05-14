# Web-Scraping-w-Python from https://brightdata.com
The goal of this tutorial is to learn how to extract all quote data from the website. For each quote, you will learn how to scrape the text, author, and list of tags. Then the scraped data will be converted to CSV.
As you can see, Quotes to Scrape is nothing more than a sandbox for web scraping. Specifically, it contains a paginated list of quotes. The Python web scraper you are going to build will retrieve all the citations contained on each page and return them as CSV data.
___________
Requests simplify HTTP requests
Beautifu lSoup allows you to parse & interact with HTML & XML documents
Selenium automates browser actions

1. Determine which scraping libraries should be used for the project
   Visit the target website & inspect page, check if site relies on JavaScript for data retrieval.
      Beautiful Soup & Requests are ideal for static content sites.
2. Intialize python project and install/import necessary libraries
3. Connect to the target URL (page = requests.get('url_here'))
4. Parse HTML content using Beautiful Soup
5. Select HTML elements
