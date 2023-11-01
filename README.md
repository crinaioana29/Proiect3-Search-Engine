# Proiect 3 - Search Engine
Status: In development.

Proiectul este bazat pe un ideea unui search-engine.

# Cum functioneaza? 


Soft-ul preia din input-ul user-ului un cuvant. Cuvantul este pasat catre un REST API scris in Django (microserviciu), iar apoi catre web-crawler. Microserviciul din urma are rolul de a scana un site web si de a prelua informatiile referitoare la produsul dat ca input (titlu, pret etc).

## Work-flow Search Engine
<img width="720" alt="Proiect 3 work flow" src="https://github.com/crinaioana29/Proiect3-Search-Engine/assets/74871618/e70ad9e6-6e35-41cb-b145-44662e58548f">


## Work-flow Web-scraper

<img width="720" alt="Proiect 3 work flow" src="https://github.com/crinaioana29/Proiect3-Search-Engine/assets/74871618/9054cf5f-75ef-4781-83ff-020b6c9ca439">

## Work-flow Search-api REST

<img width="720" alt="Proiect 3 work flow" src="https://github.com/crinaioana29/Proiect3-Search-Engine/assets/74871618/af059dd2-7f47-4667-9d25-84f4c212f194">


# Tehnologii

<ul>
<li>Django - Pentru server-ul web si implicit pentru REST API</li>
<li>Python + BeautifulSoup - web scraping si parsare DOM</li>
<li>RabbitMQ - comunicare intre cele doua microservicii</li>
</ul>
