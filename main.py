import requests
import concurrent.futures


def make_request(route, token=''):
    BASE_URL = "http://127.0.0.1:5000"
    link = BASE_URL + route
    print(link)
    return requests.get(link, headers={"X-Access-Token": token}).json()


def main():
    accessToken = make_request('/register')["access_token"]
    links = make_request('/home', accessToken)["link"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        queue = [executor.submit(make_request, links[key], accessToken) for key in links]
        results = []

        while queue:
            response = queue.pop(0).result()
            results.append(response)

            if 'link' in response and 'msg' not in response:
                links = response['link']
                for key in links:
                    queue.append(executor.submit(make_request, links[key]))
                    print(key)


main()
