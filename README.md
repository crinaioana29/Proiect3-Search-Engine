# Proiect 3 - Search Engine
Status: In development.

Proiectul este bazat pe un ideea unui search-engine.

# Cum functioneaza? 


Soft-ul preia din input-ul user-ului un cuvant. Cuvantul este pasat catre un REST API scris in Django (microserviciu), iar apoi catre web-crawler. Microserviciul din urma are rolul de a scana un site web si de a prelua informatiile referitoare la produsul dat ca input (titlu, pret etc).

# Tehnologii

<ul>
<li>Django - Pentru server-ul web si implicit pentru REST API</li>
<li>Python + BeautifulSoup - web scraping si parsare DOM</li>
</ul>
