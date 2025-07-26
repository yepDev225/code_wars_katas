import re
def domain_name(url):
    matches = re.search("^((http|https)://)?(www\.)?([\w-]+)\..*$", url, re.IGNORECASE)
    return matches.group(4)