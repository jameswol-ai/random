def simulate_city(systems, intent):
    return {
        "urban_core": {
            "density": "high" if intent["focus"]["high_density"] else "medium",
            "transport_flow": "optimized" if "mass_transit_system" in systems else "car-based",
        },
        "infrastructure": systems,
        "sustainability_score": 85 if intent["focus"]["eco_priority"] else 60
    }
