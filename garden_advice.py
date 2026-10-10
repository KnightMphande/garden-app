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


def get_valid_choice(prompt, valid_choices):
    """Ask repeatedly until the user enters one of the supported choices.

    Ignore surrounding whitespace and letter case so inputs such as
    ' SUMMER ' are accepted as 'summer'.
    """
    while True:
        choice = input(prompt).strip().lower()

        if choice in valid_choices:
            return choice

        # Explain the available choices before prompting again.
        print(f"Invalid choice. Please choose: {', '.join(valid_choices)}.")


def main():
    """Collect valid user choices and display matching gardening advice."""
    season = get_valid_choice(
        "Choose a season (summer/winter): ",
        ("summer", "winter"),
    )
    plant_type = get_valid_choice(
        "Choose a plant type (flower/vegetable): ",
        ("flower", "vegetable"),
    )

    print("\nGardening advice:")
    print(generate_advice(season, plant_type))


# Importing the module exposes its functions without starting the prompts.
if __name__ == "__main__":
    main()
