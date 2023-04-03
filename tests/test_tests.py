import pytest
import requests


def get_data_from_website(url):
    response = requests.get(url)
    return response.json()


def test_get_data_from_website(mocker):
    expected_data = {'foo': 'bar'}
    mocked_response = mocker.Mock()
    mocked_response.json.return_value = expected_data
    mocker.patch('requests.get', return_value=mocked_response)

    data = get_data_from_website('http://example.com/api/data')

    assert data == expected_data



Class