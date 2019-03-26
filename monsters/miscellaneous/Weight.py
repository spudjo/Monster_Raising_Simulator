# functions related to Creature weight


def calculate_weight(base_weight, body_parts):

    for part in body_parts:
        base_weight += part.weight
    return base_weight
