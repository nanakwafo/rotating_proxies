import requests

def main():
    proxy = '82.202.160.205:8118'
    proxies={
        'http': proxy,
        'https': proxy
    }
    request = requests.get('https://httpbin.org/ip',proxies=proxies,timeout=3)
    print(request.status_code)


if __name__ == '__main__':
   main()