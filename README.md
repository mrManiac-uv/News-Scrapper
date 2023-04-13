# News-Scrapper

### for OceanFrogs task

This is a Django web application that fetches news data from the NewsAPI service for the BBC News and Reuters sources.
<br>

## Installation

1. Clone the repository to your local machine:<br>
   `git clone https://github.com/your_username/news-api.git`
2. Set up your NewsAPI key by adding it to the newsAPI.py file:<br>
   `API_KEY = 'your_api_key'`
3. Run the server by running:<br>
   `python manage.py runserver`
4. Run<br>
   `curl http://127.0.0.1:8000/api/news/ -H "Accept: application/json"`

<br>

## Usage

The web application provides news data in JSON format for the BBC News and Reuters sources. To retrieve the data, simply visit the [http://localhost:8000/api/news/] URL in your web browser.
The returned JSON data contains the following fields for each news item:

- title: The title of the news item
- details: A brief description of the news item
- postedAt: The date and time when the news item was published, in ISO format (e.g. 2023-04-13T07:23:18.947898Z)

_P.s: The applicaiton will be modified to store the JSON response into a table in SQLite_
<br>

## Contributing

If you would like to contribute to this project, please open a pull request or submit an issue. We welcome any feedback or suggestions!
