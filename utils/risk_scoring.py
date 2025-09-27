def calculate(bio: dict, behavior: dict, network: dict) -> float:
    score = 1 - ((bio["auth_score"] * 0.5) +
                 (1 - behavior["deviation_score"]) * 0.3 +
                 (1 if network["device_trusted"] else 0) * 0.2)
    return round(score, 2)
