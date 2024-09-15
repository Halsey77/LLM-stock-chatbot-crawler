import proxyscrape

collector = proxyscrape.create_collector('default', 'https')  # Create a collector for http resources
proxies = collector.get_proxies({"type": "https"})  # Retrieve a united states proxy
# proxies = collector.get_proxies()

# print(proxies[0])

with open("proxies.txt", "w") as f:
    for proxy in proxies:
        f.write(f"{proxy.host}:{proxy.port}\n")