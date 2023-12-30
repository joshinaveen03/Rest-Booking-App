from src.constants.api_constants import APIConstants
import requests

def test_case():

    url_class=APIConstants.base_url()
    print(url_class)