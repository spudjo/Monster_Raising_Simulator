# functions related to Creature weight


def combine_value(base_value, body_parts):

    for part in body_parts:
        base_value += part.value
    return base_value
