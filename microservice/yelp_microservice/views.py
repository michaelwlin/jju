from django.http import JsonResponse
import requests


def get_yelp(request):
    location = request.GET.get("location")
    price = request.GET.get("price")
    term = request.GET.get("term")
    limit = request.GET.get("limit")
    key = "MergTpamdvmf3ImBMiydH267Mg6jwmSfUbkieOmu9ESUaGgC9k_lj0QFAebZj5ULEtmwyt5UuY9kL7-SvP9peX_kV6TMe4PVO6ydo-6evrVyRUoRQMSkEznECkxYZHYx"

    url = (
        "https://api.yelp.com/v3/businesses/search?location={}&price={}&term={}".format(
            location, price, term
        )
    )

    headers = {"accept": "application/json", "Authorization": "Bearer {}".format(key)}

    response = requests.get(url, headers=headers)

    obj = response.json()
    condensed_obj = {"businesses": []}
    for business in obj["businesses"][0 : int(limit)]:
        latitude =  str(business['coordinates']['latitude'])
        longitude = str(business['coordinates']['longitude']) 
        new_bus = {
            "name" : business["name"],
            "image_url" : business["image_url"],
            "url" : business["url"],
            "price" : business["price"],
            "rating" : business['rating'],
            "phone_number" : business['phone'],
            "google_maps_url" : "https://maps.google.com/?q={},{}".format(latitude, longitude)
        }
        condensed_obj['businesses'].append(new_bus)

    return JsonResponse(condensed_obj)
