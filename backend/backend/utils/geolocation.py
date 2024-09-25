def process_coordinates(latitude: float, longitude: float) -> str:
    """Classify the client based on their location coordinates."""

    if (-46.361899 <= latitude <= -34.276938 and -2.196998 <= longitude <= -15.411580) or \
    (-52.997614 <= latitude <= -44.428305 and -19.766959 <= longitude <= -23.966413):
        return "special"
    
    if (-54.777426 <= latitude <= -46.603598 and -26.155681 <= longitude <= -34.016466):
        return "normal"
    
    return "laborious"

def get_region_by_state(state: str) -> str:
    """Extract the region based on the state field."""
    
    state = state.lower()
    regions = {
        'norte': ['acre', 'amapá', 'amazonas', 'pará', 'rondônia', 'roraima', 'tocantins'],
        'nordeste': ['alagoas', 'bahia', 'ceará', 'maranhão', 'paraíba', 'pernambuco', 'piauí', 'rio grande do norte', 'sergipe'],
        'centro-oeste': ['distrito federal', 'goiás', 'mato grosso', 'mato grosso do sul'],
        'sudeste': ['espírito santo', 'minas gerais', 'rio de janeiro', 'são paulo'],
        'sul': ['paraná', 'rio grande do sul', 'santa catarina']
    }

    for region, states in regions.items():
        if state in states:
            return region
    return "State invalid"