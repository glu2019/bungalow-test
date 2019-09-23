import pytest
from drf.models import Bungalow


class TestBungalow:
    BUNGALOW_TEST_DATA = {
        "area_unit": "SqFt",
        "bathrooms": "5.0",
        "bedrooms": 5,
        "home_size": 8348,
        "home_type": "SingleFamily",
        "link": "https://www.zillow.com/homedetails/4440-Vanceboro-Ct-Woodland-Hills-CA-91364/19946042_zpid/",
        "price": "$2.95M",
        "property_size": 17545,
        "rent_price": 12354.0,
        "rentzestimate_amount": 10000,
        "rentzestimate_last_updated": "2017-08-25T00:00:00Z",
        "tax_value": 2590269,
        "tax_year": 2017,
        "year_built": 1990,
        "zestimate_amount": 2915567,
        "zestimate_last_updated": "2017-08-25T00:00:00Z",
        "zillow_id": 19946042,
        "address": "4440 Vanceboro Ct",
        "city": "Woodland Hills",
        "state": "CA",
        "zipcode": "91364",
    }
    TEST_API_ENDPOINT = "/api/bungalow/"

    @pytest.fixture(autouse=True)
    def setUp(self, db, set_client_authentication):
        self.client = set_client_authentication 
    
    def test_get_bungalow(self):
        response = self.client.get(self.TEST_API_ENDPOINT)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.all().count()
    
    def test_bungalow_filter_by_bedrooms(self):

        url = f"{self.TEST_API_ENDPOINT}?bedrooms__gt=3"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(bedrooms__gt=3).order_by('id').count()
  
    def test_bungalow_filter_by_bathrooms(self):

        url = f"{self.TEST_API_ENDPOINT}?bathrooms__gt=2.5"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(bathrooms__gt=2.5).order_by('id').count()

    def test_bungalow_filter_by_year_built(self):

        url = f"{self.TEST_API_ENDPOINT}?year_built__gt=2017"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(year_built__gt="2017").order_by('id').count()
    
    def test_bungalow_filter_by_home_size(self):

        url = f"{self.TEST_API_ENDPOINT}?home_size__gt=8000"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(home_size__gt="8000").order_by('id').count()
    
    def test_bungalow_filter_by_rent_price(self):

        url = f"{self.TEST_API_ENDPOINT}?rent_price__gt=8000"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(rent_price__gt="8000").order_by('id').count()
    
    def test_bungalow_filter_by_zillow_id(self):

        url = f"{self.TEST_API_ENDPOINT}?zillow_id=19946042"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(zillow_id="19946042").order_by('id').count()

    def test_bungalow_filter_by_state(self):

        url = f"{self.TEST_API_ENDPOINT}?state=CA"
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["count"] == Bungalow.objects.filter(state="CA").order_by('id').count()

    def test_create_bungalow(self):
        old_count = Bungalow.objects.all().count()
        response = self.client.post(self.TEST_API_ENDPOINT, data=self.BUNGALOW_TEST_DATA)
        assert response.status_code == 201
        assert Bungalow.objects.all().count() == old_count + 1