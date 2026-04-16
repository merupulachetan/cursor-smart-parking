"""
Hierarchical options for vehicle registration (type → subtype, brand → model).
"""

from __future__ import annotations

import json
from typing import Any

# type -> subtypes list, brands -> { brand: [models] }
CATALOG: dict[str, dict[str, Any]] = {
    "Car": {
        "subtypes": ["Hatchback", "Sedan", "SUV", "MUV", "Coupe"],
        "brands": {
            "Maruti Suzuki": ["Swift", "Baleno", "Dzire", "Brezza", "Ertiga", "Wagon R"],
            "Hyundai": ["i20", "Venue", "Creta", "Verna", "Ioniq 5"],
            "Tata": ["Nexon", "Punch", "Harrier", "Safari", "Tiago"],
            "Mahindra": ["Scorpio", "XUV700", "Thar", "Bolero"],
            "Honda": ["City", "Amaze", "Elevate"],
            "Toyota": ["Innova", "Fortuner", "Glanza", "Hyryder"],
            "Skoda": ["Slavia", "Kushaq", "Superb"],
            "Volkswagen": ["Virtus", "Taigun"],
        },
    },
    "Motorcycle": {
        "subtypes": ["Scooter", "Commuter", "Sports", "Electric", "Cruiser"],
        "brands": {
            "Honda": ["Activa", "Shine", "Unicorn", "CB350"],
            "TVS": ["Jupiter", "Apache", "Raider", "iQube"],
            "Bajaj": ["Pulsar", "CT 100", "Dominar", "Chetak"],
            "Hero": ["Splendor", "Passion", "Xtreme", "Vida"],
            "Royal Enfield": ["Classic", "Meteor", "Himalayan"],
            "Ola": ["S1 Pro", "S1 Air"],
        },
    },
    "Commercial": {
        "subtypes": ["Van", "Pickup", "Light truck", "Tempo"],
        "brands": {
            "Tata": ["Ace", "Intra", "Yodha"],
            "Mahindra": ["Bolero Pickup", "Jeeto", "Supro"],
            "Ashok Leyland": ["Dost", "Partner"],
        },
    },
}


def catalog_json_string() -> str:
    return json.dumps(CATALOG)


def validate_selection(
    vehicle_type: str,
    vehicle_subtype: str,
    brand: str,
    model: str,
) -> None:
    t = vehicle_type.strip()
    if t not in CATALOG:
        raise ValueError("Invalid vehicle type")
    block = CATALOG[t]
    st = vehicle_subtype.strip()
    if st not in block["subtypes"]:
        raise ValueError("Invalid sub-type for this vehicle type")
    brands: dict[str, list[str]] = block["brands"]
    b = brand.strip()
    if b not in brands:
        raise ValueError("Invalid brand for this vehicle type")
    m = model.strip()
    if m not in brands[b]:
        raise ValueError("Invalid model for this brand")
