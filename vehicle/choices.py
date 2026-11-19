
MODEL_CHOICES = (
    ("old_face", "Old Face"),
    ("new_face", "New Face"),
    ("facelift", "Facelift"),
)

CONDITION_STATUS = (
    ("excellent", "Excellent"),
    ("good", "Good"),
    ("fair", "Fair"),
    ("poor", "Poor"),
    ("damaged", "Damaged"),
)

DAMAGE_STATUS = (
    (10, "Minor Cosmetic Damage"),
    (20, "Cosmetic Damage"),
    (30, "Moderate Exterior Damage"),
    (40, "Significant Body Damage"),
    (50, "Structural Damage"),
    (60, "Mechanical Damage"),
    (70, "Severe Mechanical Damage"),
    (80, "Major Structural & Mechanical Damage"),
    (90, "Severe Vehicle Damage"),
    (100, "Total Loss / Wrecked"),
)

REPAIR_STATUS = (
    ("not_needed", "No Repair Needed"),
    ("not_started", "Not Repaired"),
    ("pending", "Awaiting Repair"),
    ("in_progress", "Under Repair"),
    ("partially_repaired", "Partially Repaired"),
    ("fully_repaired", "Fully Repaired"),
    ("repair_failed", "Repair Unsuccessful"),
    ("irreparable", "Beyond Repair"),
)

VEHICLE_TYPE = (
    ("passenger_car", "Passenger Car"),
    ("motorcycle", "Motorcycle"),
    ("scooter", "Scooter"),
    ("pickup_truck", "Pickup Truck"),
    ("van", "Van"),
    ("minibus", "Minibus"),
    ("bus", "Bus"),
    ("truck", "Truck"),
    ("tractor_truck", "Tractor Truck"),
    ("trailer", "Trailer"),
    ("semi_trailer", "Semi-Trailer"),
    ("agricultural_vehicle", "Agricultural Vehicle"),
    ("construction_vehicle", "Construction Vehicle"),
    ("special_purpose_vehicle", "Special-Purpose Vehicle"),
    ("electric_bicycle", "Electric Bicycle"),
    ("bicycle", "Bicycle"),
)


PART_CATEGORY = (
    ("engine_parts", "Engine Parts"),
    ("transmission_parts", "Transmission & Gearbox Parts"),
    ("braking_system", "Braking System"),
    ("suspension_system", "Suspension System"),
    ("steering_system", "Steering System"),
    ("electrical_system", "Electrical System"),
    ("cooling_system", "Cooling System"),
    ("fuel_system", "Fuel System"),
    ("exhaust_system", "Exhaust System"),
    ("air_intake_system", "Air Intake System"),
    ("body_parts", "Body Parts & Panels"),
    ("exterior_accessories", "Exterior Accessories"),
    ("interior_parts", "Interior Parts"),
    ("interior_accessories", "Interior Accessories"),
    ("lighting_system", "Lighting System"),
    ("wheels_and_tires", "Wheels & Tires"),
    ("battery_and_charging", "Battery & Charging System"),
    ("clutch_system", "Clutch System"),
    ("drivetrain", "Drivetrain & Axles"),
    ("filters_and_fluids", "Filters & Fluids"),
    ("air_conditioning", "Air Conditioning & Heating"),
    ("safety_systems", "Safety Systems"),
    ("electronics_and_sensors", "Electronics & Sensors"),
    ("glass_and_mirrors", "Glass & Mirrors"),
    ("belts_and_hoses", "Belts & Hoses"),
    ("fasteners_and_hardware", "Fasteners & Hardware"),
    ("performance_parts", "Performance & Tuning Parts"),
    ("motorcycle_parts", "Motorcycle Parts"),
    ("truck_and_heavy_vehicle_parts", "Truck & Heavy Vehicle Parts"),
    ("tools_and_equipment", "Automotive Tools & Equipment"),
    ("other_parts", "Other Parts"),
)
