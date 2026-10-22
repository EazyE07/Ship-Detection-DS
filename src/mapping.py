"""Mapping of ship classes to the three high-level categories used by the project.

The V1 model predicts 25 fine-grained ship types, the V2 model predicts the
three categories directly. `categorize` handles both.
"""

SHIP_MAPPING = {
    'Military': [
        'Aircraft Carrier', 'Commander', 'Cruiser', 'Destroyer',
        'Frigate', 'Landing', 'Other Warship', 'Patrol', 'Submarine'
    ],
    'Logistics': [
        'Barge', 'Cargo', 'Container Ship', 'Oil Tanker',
        'RoRo', 'Other Merchant'
    ],
    'Civilian': [
        'Auxiliary Ships', 'Dock', 'Ferry', 'Fishing Vessel',
        'Hovercraft', 'Motorboat', 'Other Ship', 'Sailboat',
        'Tugboat', 'Yacht'
    ]
}

CAT_COLORS = {
    'Military': (0, 0, 255),       # Red
    'Logistics': (255, 0, 0),      # Blue
    'Civilian': (0, 255, 0),       # Green
    'Unknown': (128, 128, 128)     # Gray
}

_SUBTYPE_TO_CATEGORY = {
    subtype: category
    for category, subtypes in SHIP_MAPPING.items()
    for subtype in subtypes
}
_CATEGORY_BY_LOWER_NAME = {category.lower(): category for category in SHIP_MAPPING}


def categorize(label):
    """Return the category for a model label.

    Accepts either a category name (V2 model, e.g. 'military') or a
    fine-grained ship type (V1 model, e.g. 'Destroyer'). Returns 'Unknown'
    if the label matches neither.
    """
    label = str(label)
    return _CATEGORY_BY_LOWER_NAME.get(
        label.lower(), _SUBTYPE_TO_CATEGORY.get(label, 'Unknown')
    )
