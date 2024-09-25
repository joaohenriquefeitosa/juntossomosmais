def process_coordinates(latitude: float, longitude: float) -> str:
    if (-46.361899 <= latitude <= -34.276938 and -2.196998 <= longitude <= -15.411580) or \
    (-52.997614 <= latitude <= -44.428305 and -19.766959 <= longitude <= -23.966413):
        return "special"
    
    if (-54.777426 <= latitude <= -46.603598 and -26.155681 <= longitude <= -34.016466):
        return "normal"
    
    return "laborious"
