import requests
from concurrent.futures import *


class Traverse:

    def __init__(self, BASE_URL):
        self.BASE_URL = BASE_URL
        self.token = ''

    def request(self, route):
        link = self.BASE_URL + route
        print(link)

        return requests.get(link, headers={'X-Access-Token': self.token}).json()

    def register(self):
        self.token = self.request('/register')['access_token']
        links = self.request('/home')['link']

        executor = ThreadPoolExecutor(max_workers=6)
        queue = [executor.submit(self.request, links[key]) for key in links]
        response = []

        while queue:
            [done, queue] = wait(queue, return_when=FIRST_COMPLETED)

            for data in done:
                result = data.result()
                response.append(result)

                if 'link' in result and 'msg' not in result:
                    links = result['link']
                    for key in links:
                        queue.add(executor.submit(self.request, links[key]))

                    print(links)

        return response
