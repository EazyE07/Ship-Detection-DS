SHIP_MAPPING = {
    'Military': [
        'Aircraft Carrier', 'Commander', 'Cruiser', 'Destroyer', 
        'Frigate', 'Landing', 'Other Warship', 'Patrol', 'Submarine'
    ],
    'Logistics': [
        'Barge', 'Cargo', 'Container Ship', 'Oil Tanker', 
        'RoRo', 'Other Merchant'
    ],
    'Civilian/Other': [
        'Auxiliary Ships', 'Dock', 'Ferry', 'Fishing Vessel', 
        'Hovercraft', 'Motorboat', 'Other Ship', 'Sailboat', 
        'Tugboat', 'Yacht'
    ]
}

CAT_COLORS = {
    'Military': (0, 0, 255),      # Rot
    'Logistics': (255, 0, 0),     # Blau
    'Civilian/Other': (0, 255, 0), # Grün
    'Unknown': (128, 128, 128)    # Grau
}