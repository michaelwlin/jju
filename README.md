

## Getting Started

Clone the repo and install the required dependencies:

```bash
git clone https://github.com/michaelwlin/jju.git
cd microservice
pip install Django requests
```

Start the Django app:

```bash
python3 manage.py runserver
```

The microservice will be available at http://localhost:8000/.

## Requesting Data

To request data from the microservice, you can use a GET request to the /microservice/yelp endpoint. Pass in the params: 'limit' (how many items returned), 'location', 'price' (1, 2, 3, or 4), and 'term' (search term) to get results.
ie:
limit = 10
location = tokyo
price = 3
term = sushi

Example URL
http://localhost:8000/microservice/yelp?&limit=10&location=tokyo&price=3&term=sushi


## Receiving Data

The response from the GET request will be a JSON object containing a condensed list of businesses within the specified limit.

Sample response from http://localhost:8000/microservice/yelp?&limit=3&location=new+york+city&price=3&term=pizza:

```json
{
    "businesses": [
        {
            "name": "L'Antica Pizzeria Da Michele NYC",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/I8YyoJeyozTWf8fLXZV--Q/o.jpg",
            "url": "https://www.yelp.com/biz/l-antica-pizzeria-da-michele-new-york?adjust_creative=z8zzFMKCnavBY5_-_vzi9w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=z8zzFMKCnavBY5_-_vzi9w",
            "price": "$$$",
            "rating": 4.5,
            "phone_number": "+19295246682",
            "google_maps_url": "https://maps.google.com/?q=40.737052,-74.001571"
        },
        {
            "name": "Barano",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/Y6mlGG1H0V2ZeUtpBsxsEg/o.jpg",
            "url": "https://www.yelp.com/biz/barano-brooklyn?adjust_creative=z8zzFMKCnavBY5_-_vzi9w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=z8zzFMKCnavBY5_-_vzi9w",
            "price": "$$$",
            "rating": 4.5,
            "phone_number": "+13479874500",
            "google_maps_url": "https://maps.google.com/?q=40.710372,-73.96794"
        },
        {
            "name": "Leuca",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/LbRIs0mXGex3QpwHlN4Ykg/o.jpg",
            "url": "https://www.yelp.com/biz/leuca-brooklyn?adjust_creative=z8zzFMKCnavBY5_-_vzi9w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=z8zzFMKCnavBY5_-_vzi9w",
            "price": "$$$",
            "rating": 4.0,
            "phone_number": "",
            "google_maps_url": "https://maps.google.com/?q=40.722121,-73.956678"
        }
    ]
}
```