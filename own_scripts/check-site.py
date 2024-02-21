import requests
import time

# URLs list
# url_list = [
#     "http://107.20.94.234",
#     "http://107.20.94.234/state-by-state",
#     "http://107.20.94.234/bonus",
#     "http://107.20.94.234/slots/free",
#     "http://107.20.94.234/land-based-casinos",
#     "http://107.20.94.234/reviews",
#     "http://107.20.94.234/slots",
#     "http://107.20.94.234/online-poker"
# ]
url_list = [
    "http://gamblespot.us",
    "http://gamblespot.us/state-by-state",
    "http://gamblespot.us/bonus",
    "http://gamblespot.us/slots/free",
    "http://gamblespot.us/land-based-casinos",
    "http://gamblespot.us/reviews",
    "http://gamblespot.us/slots",
    "http://gamblespot.us/online-poker"
]
# Maximum requests quantity
max_requests = 10
# Max requests per second
requests_per_second = 50

def check_sites(url_list, max_requests, requests_per_second):
    for url in url_list:
        for _ in range(max_requests):
            response = requests.get(url)
            if response.status_code == 200:
                print(url + " Success (HTTP 200)")
            elif response.status_code == 500:
                print(url + " Server error (HTTP 500)")
            elif response.status_code == 503:
                print(url + " Timeout (HTTP 503)")
            else:
                print(f"Unexpected HTTP code: {response.status_code}")

            # Pause between requests
            time.sleep(1 / requests_per_second)


if __name__ == "__main__":
    check_sites(url_list, max_requests, requests_per_second)