from backend.utils.geolocation import process_coordinates, get_region_by_state
from backend.utils.phone_formatter import format_phone_number

class ClientProcessor:

    def __init__(self):
        self.nationality = 'BR'

    def format_client_data(self, raw_data: dict) -> dict:
        """Format raw data from JSON or CSV into a common client format."""

        return {
            "type": self.set_type(raw_data),
            "gender": self.set_gender(raw_data),
            "name": {
                "title": raw_data.get("name__title") or raw_data["name"]["title"],
                "first": raw_data.get("name__first") or raw_data["name"]["first"],
                "last": raw_data.get("name__last") or raw_data["name"]["last"]
            },
            "location": {
                "region": self.set_region(raw_data),
                "street": raw_data.get("location__street") or raw_data["location"]["street"],
                "city": raw_data.get("location__city") or raw_data["location"]["city"],
                "state": raw_data.get("location__state") or raw_data["location"]["state"],
                "postcode": raw_data.get("location__postcode") or raw_data["location"]["postcode"],
                "coordinates": {
                    "latitude": raw_data.get("location__coordinates__latitude") or raw_data["location"]["coordinates"]["latitude"],
                    "longitude": raw_data.get("location__coordinates__longitude") or raw_data["location"]["coordinates"]["longitude"]
                },
                "timezone": {
                    "offset": raw_data.get("location__timezone__offset") or raw_data["location"]["timezone"]["offset"],
                    "description": raw_data.get("location__timezone__description") or raw_data["location"]["timezone"]["description"]
                }
            },
            "email": raw_data.get("email"),
            "birthday": raw_data.get("dob__date") or raw_data["dob"]["date"],
            "registered": raw_data.get("registered__date") or raw_data["registered"]["date"],
            "telephoneNumbers": [self.set_phone_numbers(raw_data.get("phone"))],
            "mobileNumbers": [self.set_phone_numbers(raw_data.get("cell"))],
            "picture": {
                "large": raw_data.get("picture__large") or raw_data["picture"]["large"],
                "medium": raw_data.get("picture__medium") or raw_data["picture"]["medium"],
                "thumbnail": raw_data.get("picture__thumbnail") or raw_data["picture"]["thumbnail"]
            },
            "nationality": self.nationality
        }

    def set_type(self, raw_data: dict) -> str:
        """Classify the client based on their location coordinates."""

        latitude = float(raw_data.get("location__coordinates__latitude") or raw_data["location"]["coordinates"]["latitude"])
        longitude = float(raw_data.get("location__coordinates__longitude") or raw_data["location"]["coordinates"]["longitude"])

        return process_coordinates(latitude, longitude)

    def set_gender(self, raw_data: dict) -> str:
        """Extract and clean the gender field."""
        
        gender_key = next((key for key in raw_data.keys() if "gender" in key.lower()), None)
        if gender_key:
            return raw_data.get(gender_key).strip('\"')[0]
        return ""

    def set_phone_numbers(self, phone_data:str) -> str:
        """Format the phone number."""

        return format_phone_number(phone_data)

    def set_region(self, raw_data: dict) -> str:
        """Extract the region based on the state field."""

        state = raw_data.get("location__state") or raw_data["location"]["state"]
        return get_region_by_state(state)

    def process(self, raw_data: dict) -> dict:
        """Process the raw data and return formatted client data."""
        return self.format_client_data(raw_data)