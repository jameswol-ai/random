# src/core/city_planner.py

def generate_city_plan(intent):
    systems = []

    # core city skeleton always exists
    systems.append("housing_grid")
    systems.append("road_network")

    if intent["focus"]["transport_heavy"]:
        systems.append("mass_transit_system")

    if intent["focus"]["eco_priority"]:
        systems.append("renewable_energy_grid")
        systems.append("water_harvesting_system")

    if intent["focus"]["high_density"]:
        systems.append("vertical_zoning_system")

    return systems
