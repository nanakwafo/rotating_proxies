import requests

def main():
    proxy = '82.202.160.205:8118'
    proxies={
        'http': proxy,
        'https': proxy
    }
    try:
        request = requests.get('https://httpbin.org/ip',proxies=proxies,timeout=3)
        print(request.status_code)
    except:
        print("An Exceptional Error Occured")
    else:
        print("Everything worked well")


if __name__ == '__main__':
   main()