import requests
from ..output import emit


def fetch():
    data = requests.get("https://dissenter.com/url").json()

    # We currently ignore trending comments.
    # The pagination here is opaque/doesn't seem to be meaningful, so we only pull once
    for url in data["trendingUrls"]:
        emit(url)
