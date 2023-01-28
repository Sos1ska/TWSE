from ..important_func import path_os
class Generate:
    protocols = ["http", "https", "socks4", "socks5"]
    def __init__(self, lang):
        from requests import get
        from bs4 import BeautifulSoup
        from json import loads, dump
        if lang == "RUS":
            print(f"Выберите протокол {self.protocols}")
            user_protocol = input("> ")
            if user_protocol == "http":
                send_request = get("https://www.proxyscan.io/api/proxy?type=http")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"http": f"http://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            elif user_protocol == "https":
                send_request = get("https://www.proxyscan.io/api/proxy?type=https")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"https": f"https://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            elif user_protocol == "socks4":
                send_request = get("https://www.proxyscan.io/api/proxy?type=socks4")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"socks4": f"socks4://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            elif user_protocol == "socks5":
                send_request = get("https://www.proxyscan.io/api/proxy?type=socks5")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"socks5": f"socks5://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            else:
                print('Возвращаюсь обратно')
        elif lang == "ENG":
            print(f"Select protocol {self.protocols}")
            user_protocol = input("> ")
            if user_protocol == "http":
                send_request = get("https://www.proxyscan.io/api/proxy?type=http")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"http": f"http://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            elif user_protocol == "https":
                send_request = get("https://www.proxyscan.io/api/proxy?type=https")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"https": f"https://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            elif user_protocol == "socks4":
                send_request = get("https://www.proxyscan.io/api/proxy?type=socks4")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"socks4": f"socks4://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            elif user_protocol == "socks5":
                send_request = get("https://www.proxyscan.io/api/proxy?type=socks5")
                answer = send_request
                soup_json = BeautifulSoup(answer.text, 'html.parser').text.strip()
                site_json = loads(soup_json)
                for proxies in site_json:
                    host = proxies["Ip"]
                    port = proxies["Port"]
                proxy_load = {"socks5": f"socks5://{host}:{port}"}
                with open(path_os(r"files/cache/proxy_generate.json"), "w") as file_cache : dump(proxy_load, file_cache)
                with open(path_os(r"files/config/proxy.json"), "w") as file_config : dump(proxy_load, file_config)
                print('[ generation_proxy ] - [ Generated ]')
            else:
                print('I\'m coming back')

class Load:
    pass
