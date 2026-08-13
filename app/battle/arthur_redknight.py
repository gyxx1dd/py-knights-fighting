def battle_arthur_redknight(arthur: object, red_knight: object) -> None:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0
    elif red_knight["hp"] <= 0:
        red_knight["hp"] = 0
