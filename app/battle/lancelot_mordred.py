def battle_lancelot_mordred(lancelot: dict, mordred: dict) -> None:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0
    elif mordred["hp"] <= 0:
        mordred["hp"] = 0
