def preparation_mordred(knight_config: dict) -> dict:
    mordred = knight_config["mordred"]

    # apply armour
    mordred["protection"] = 0
    for armour in mordred["armour"]:
        mordred["protection"] += armour["protection"]

    # apply weapon
    mordred["power"] += mordred["weapon"]["power"]

    # apply potion if exist
    if mordred["potion"] is not None:
        if "power" in mordred["potion"]["effect"]:
            mordred["power"] += mordred["potion"]["effect"]["power"]

        if "protection" in mordred["potion"]["effect"]:
            mordred["protection"] += mordred["potion"]["effect"]["protection"]

        if "hp" in mordred["potion"]["effect"]:
            mordred["hp"] += mordred["potion"]["effect"]["hp"]

    return mordred
