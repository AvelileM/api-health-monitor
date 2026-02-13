import json #WHY this is here? I don't see it being used anywhere in the code. Maybe it's for future use.
with open('config.json') as f:
    urls = f.read().splitlines() # This reads the config.json file and splits it into a list of URLs, which will be used for monitoring the health of these APIs. Each URL is expected to be on a new line in the config.json file.
    for url in urls:
        print(url)