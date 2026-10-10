"""Generate gardening advice for a season and plant type."""


def get_season_advice(season):
    """Return seasonal care advice, or a fallback for unknown seasons."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    if season == "winter":
        return "Protect your plants from frost with covers."

    return "No advice for this season."


def get_plant_advice(plant_type):
    """Return plant-specific advice, or a fallback for unknown types."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    if plant_type == "vegetable":
        return "Keep an eye out for pests!"

    return "No advice for this type of plant."


def generate_advice(season, plant_type):
    """Combine seasonal and plant-specific advice into two lines."""
    season_advice = get_season_advice(season)
    plant_advice = get_plant_advice(plant_type)

    return f"{season_advice}\n{plant_advice}"


def main():
    """Display advice using the starter program's default choices."""
    # User input will replace these defaults in issue #2.
    season = "summer"
    plant_type = "flower"

    print(generate_advice(season, plant_type))


# Importing this module makes its functions available without printing.
if __name__ == "__main__":
    main()
