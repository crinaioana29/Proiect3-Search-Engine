from api.web_crawler.load_properties import load_properties


def test_hostname_retrieval():
    assert load_properties('../../resources/ConfigFile.properties',
                           'RequestSection',
                           'request.hostname') == 'https://lajumate.ro/cauta_'


def test_params_retrieval():
    assert load_properties('../../resources/ConfigFile.properties',
                           'RequestSection',
                           'request.params') == '_ordonare-dupa-data-descrescator.html'


def test_useragent_retrieval():
    assert load_properties('../../resources/ConfigFile.properties',
                           'RequestSection',
                           'request.user-agent') == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
