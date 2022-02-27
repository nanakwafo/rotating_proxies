import requests

def main():
    proxy = '164.100.130.128:8080'
    proxies={
        'http': proxy,
        'https': proxy
    }
    request = requests.get('',proxies=proxies,timeout={})
    print(request.json())


if __name__ == '__main__':
   main()