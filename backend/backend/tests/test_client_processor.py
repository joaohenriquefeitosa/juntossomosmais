import pytest
import os
from backend.parsers.csv_parser import parse_csv
from backend.parsers.json_parser import parse_json
from backend.services.client_processor import ClientProcessor

@pytest.fixture
def processor():
    return ClientProcessor()

@pytest.fixture
def source_folder():
    return os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data'))

@pytest.fixture
def csv_data(source_folder):
    return parse_csv(os.path.join(source_folder, 'data.csv'))

@pytest.fixture
def json_data(source_folder):
    return parse_json(os.path.join(source_folder, 'data.json'))['results']

@pytest.mark.django_db
def test_process_client_data_with_csv(processor, csv_data):
    processed_data = processor.process(csv_data[0])

    assert processed_data['gender'] == 'f'

    assert processed_data['name']['title'] == 'mrs'
    assert processed_data['name']['first'] == 'ione'
    assert processed_data['name']['last'] == 'da costa'

    assert processed_data['location']['region'] == 'norte'
    assert processed_data['location']['street'] == '8614 avenida vinícius de morais'
    assert processed_data['location']['city'] == 'ponta grossa'
    assert processed_data['location']['state'] == 'rondônia'
    assert processed_data['location']['postcode'] == '97701'
    assert processed_data['location']['coordinates']['latitude'] == '-76.3253'
    assert processed_data['location']['coordinates']['longitude'] == '137.9437'
    assert processed_data['location']['timezone']['offset'] == '-1:00'
    assert processed_data['location']['timezone']['description'] == 'Azores, Cape Verde Islands'

    assert processed_data['name']['title'] == 'mrs'
    assert processed_data['name']['first'] == 'ione'
    assert processed_data['name']['last'] == 'da costa'

    assert processed_data['email'] == 'ione.dacosta@example.com'
    assert processed_data['birthday'] == '1968-01-24T18:03:23Z'
    assert processed_data['registered'] == '2004-01-23T23:54:33Z'

    assert processed_data['telephoneNumbers'][0] == '+550154155648'
    assert processed_data['mobileNumbers'][0] == '+551082645550'

    assert processed_data['picture']['large'] == 'https://randomuser.me/api/portraits/women/46.jpg'
    assert processed_data['picture']['medium'] == 'https://randomuser.me/api/portraits/med/women/46.jpg'
    assert processed_data['picture']['thumbnail'] == 'https://randomuser.me/api/portraits/thumb/women/46.jpg'

    assert processed_data['nationality'] == 'BR'

@pytest.mark.django_db
def test_process_client_data_with_json(processor, json_data):
    processed_data = processor.process(json_data[0])

    assert processed_data['gender'] == 'f'

    assert processed_data['name']['title'] == 'mrs'
    assert processed_data['name']['first'] == 'ione'
    assert processed_data['name']['last'] == 'da costa'

    assert processed_data['location']['region'] == 'norte'
    assert processed_data['location']['street'] == '8614 avenida vinícius de morais'
    assert processed_data['location']['city'] == 'ponta grossa'
    assert processed_data['location']['state'] == 'rondônia'
    assert processed_data['location']['postcode'] == 97701
    assert processed_data['location']['coordinates']['latitude'] == '-76.3253'
    assert processed_data['location']['coordinates']['longitude'] == '137.9437'
    assert processed_data['location']['timezone']['offset'] == '-1:00'
    assert processed_data['location']['timezone']['description'] == 'Azores, Cape Verde Islands'

    assert processed_data['name']['title'] == 'mrs'
    assert processed_data['name']['first'] == 'ione'
    assert processed_data['name']['last'] == 'da costa'

    assert processed_data['email'] == 'ione.dacosta@example.com'
    assert processed_data['birthday'] == '1968-01-24T18:03:23Z'
    assert processed_data['registered'] == '2004-01-23T23:54:33Z'

    assert processed_data['telephoneNumbers'][0] == '+550154155648'
    assert processed_data['mobileNumbers'][0] == '+551082645550'

    assert processed_data['picture']['large'] == 'https://randomuser.me/api/portraits/women/46.jpg'
    assert processed_data['picture']['medium'] == 'https://randomuser.me/api/portraits/med/women/46.jpg'
    assert processed_data['picture']['thumbnail'] == 'https://randomuser.me/api/portraits/thumb/women/46.jpg'

    assert processed_data['nationality'] == 'BR'

@pytest.mark.django_db
def test_process_client_data_with_invalid_csv(processor):
    invalid_data = [{'invalid_field': 'data'}]
    with pytest.raises(KeyError):
        processor.process(invalid_data[0])

@pytest.mark.django_db
def test_process_client_data_with_invalid_json(processor):
    invalid_data = [{'invalid_field': 'data'}]
    with pytest.raises(KeyError):
        processor.process(invalid_data[0])
