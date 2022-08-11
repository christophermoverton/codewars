import re
def domain_name(url):
    #)|(?<=\.)([^.]+)(?:\.(?:co\.uk|ac\.us|[^.]+(?:$|\n)))
    res=re.findall(r'(?<=www\.|s://|p://)([a-zA-z0-9_-]+)',url)
    if len(res) > 1:
        return res[1]
    elif len(res) == 0:
        res=re.findall(r'([a-zA-z0-9_-]+)(?:\.)',url)
        print(res)
        return res[0]
    return res[0]
    print(res)

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
print(domain_name("https://hyphen-site.org"))
print(domain_name("http://www.codewars.com/kata/"))
print(domain_name("icann.org"))