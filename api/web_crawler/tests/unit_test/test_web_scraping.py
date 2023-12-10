from unittest.mock import patch
from api.web_crawler.main import web_scraping


def test_web_scraping():
    mock_string = [{'Price': '25 LEI',
                    'Title': 'Stationery set SANTORO Gorjus, Kori Kumi, Breloc, Cana, pix'},
                   {'Price': '50 LEI', 'Title': 'Cana cu filtru apa-Brita'},
                   {'Price': '85.000 EUR',
                    'Title': 'PROMOTIE Duplex finalizat cu teren 350mp apa curenta si cana'},
                   {'Price': '140 LEI',
                    'Title': 'Cadou Craciun pentru fetita/sotie cana papusa handmade'},
                   {'Price': '50 LEI', 'Title': 'Cana Star Wars Disney'},
                   {'Price': '1.000 LEI', 'Title': 'Ceainic cu cana pictat manual Kazakhstan'},
                   {'Price': '73 LEI',
                    'Title': 'Conducta gaze 2.7 3.0 tdi cana ccw cdya 059131525al Audi Q7 4L '
                             '(faceli'},
                   {'Price': '73 LEI',
                    'Title': 'Conducta gaze 2.7 3.0 tdi cana ccw cdya 059131525al Porsche '
                             'Cayenne 95'},
                   {'Price': '73 LEI',
                    'Title': 'Conducta gaze 2.7 3.0 tdi cana ccw cdya 059131525al Audi A4 B8/8K '
                             '[200'},
                   {'Price': '73 LEI',
                    'Title': 'Conducta gaze 2.7 3.0 tdi cana ccw cdya 059131525al Audi A6 4F/C6 '
                             '(fac'},
                   {'Price': '73 LEI',
                    'Title': 'Conducta gaze 2.7 3.0 tdi cana ccw cdya 059131525al Volkswagen VW '
                             'Toua'},
                   {'Price': '631 LEI',
                    'Title': 'Injector injectoare  2.7 3.0 tdi cana ccw cdya 059130277be '
                             '0445116023'},
                   {'Price': '97 LEI',
                    'Title': 'Capac protectie distributie  2.7 tdi cana CGK 059109123ad '
                             'Volkswagen V'},
                   {'Price': '97 LEI',
                    'Title': 'Capac protectie distributie  2.7 tdi cana CGK 059109123ad Audi A4 '
                             'B7 ['},
                   {'Price': '97 LEI',
                    'Title': 'Capac protectie distributie  2.7 tdi cana CGK 059109123ad Audi A6 '
                             '4F/C'},
                   {'Price': '97 LEI',
                    'Title': 'Capac protectie distributie  2.7 tdi cana CGK 059109123ad '
                             'Volkswagen V'},
                   {'Price': '97 LEI',
                    'Title': 'Capac protectie distributie  2.7 tdi cana CGK 059109123ad Audi A4 '
                             'B8/8'},
                   {'Price': '97 LEI',
                    'Title': 'Capac protectie distributie  2.7 tdi cana CGK 059109123ad Audi Q7 '
                             '4L ('},
                   {'Price': '631 LEI',
                    'Title': 'Injector injectoare  2.7 3.0 tdi cana ccw cdya 059130277be '
                             '0445116023'},
                   {'Price': '631 LEI',
                    'Title': 'Injector injectoare  2.7 3.0 tdi cana ccw cdya 059130277be '
                             '0445116023'},
                   {'Price': '631 LEI',
                    'Title': 'Injector injectoare  2.7 3.0 tdi cana ccw cdya 059130277be '
                             '0445116023'},
                   {'Price': '631 LEI',
                    'Title': 'Injector injectoare  2.7 3.0 tdi cana ccw cdya 059130277be '
                             '0445116023'},
                   {'Price': '97 LEI',
                    'Title': 'Teava conducta egr 2.7 3.0 tdi cana ccw cdya 059131530c Audi Q7 4L '
                             '(fa'},
                   {'Price': '97 LEI',
                    'Title': 'Teava conducta egr 2.7 3.0 tdi cana ccw cdya 059131530c Volkswagen '
                             'VW'},
                   {'Price': '97 LEI',
                    'Title': 'Teava conducta egr 2.7 3.0 tdi cana ccw cdya 059131530c Porsche '
                             'Cayenn'},
                   {'Price': '97 LEI',
                    'Title': 'Teava conducta egr 2.7 3.0 tdi cana ccw cdya 059131530c Audi A4 '
                             'B8/8K'},
                   {'Price': '97 LEI',
                    'Title': 'Teava conducta egr 2.7 3.0 tdi cana ccw cdya 059131530c Audi A6 '
                             '4F/C6'},
                   {'Price': '2.000 EUR',
                    'Title': 'Cana portelan MS Regele Mihai copil 1927, Antichitate'}]

    with open("mock_html.html", "rb") as file:
        mock_html_content = file.read().decode("utf-8")

    with patch('api.web_crawler.main.web_scraping') as mocked_get:
        mocked_response = mocked_get.return_value
        mocked_response.content = mock_html_content.encode('utf-8')

        result = web_scraping("cana")
        assert result == mock_string
