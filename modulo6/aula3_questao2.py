urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = []

for url in urls:
    dominio = url[4:-4]
    dominios.append(dominio)

print("URLs:", urls)
print("Domínios:", dominios)
