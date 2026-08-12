def lancelot_preparation(knight_config: dict) -> dict:
    lancelot = knight_config["lancelot"]

    # apply armour
    lancelot["protection"] = 0
    for armour in lancelot["armour"]:
        lancelot["protection"] += armour["protection"]

    # apply weapon
    lancelot["power"] += lancelot["weapon"]["power"]

    # apply potion if exist
    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            protect = lancelot["potion"]["effect"]["protection"]
            lancelot["protection"] += protect

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    return lancelot
