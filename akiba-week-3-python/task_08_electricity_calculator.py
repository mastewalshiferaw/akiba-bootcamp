def validate_units(units):
   
    try:
        value = float(units)
        return value >= 0
    except ValueError:
        return False



def calculate_tier_charges(units):
    
    tier1_units = min(units, 50)
    remaining = units - tier1_units

   
    tier2_units = min(remaining, 100)
    remaining = remaining - tier2_units

    tier3_units = remaining

    tier1_cost = tier1_units * 0.50
    tier2_cost = tier2_units * 0.75
    tier3_cost = tier3_units * 1.20

    return tier1_units, tier1_cost, tier2_units, tier2_cost, tier3_units, tier3_cost


def calculate_total_bill(units, service_fee=10.0):
  
    t1_u, t1_c, t2_u, t2_c, t3_u, t3_c = calculate_tier_charges(units)
    energy_charge = t1_c + t2_c + t3_c
    total = energy_charge + service_fee
    return total



def generate_billing_summary(units, service_fee=10.0):
    """Prints a clear receipt for the customer."""
    t1_u, t1_c, t2_u, t2_c, t3_u, t3_c = calculate_tier_charges(units)
    energy_charge = t1_c + t2_c + t3_c
    total_bill = energy_charge + service_fee

    print("====================================")
    print("      ELECTRICITY BILL SUMMARY      ")
    print("====================================")
    print(f"Total Consumption: {units} units")
    print("------------------------------------")
    print(f"Tier 1 (0-50 units)   : {t1_u:.1f} units = {t1_c:.2f} Birr")
    print(f"Tier 2 (51-150 units) : {t2_u:.1f} units = {t2_c:.2f} Birr")
    print(f"Tier 3 (>150 units)   : {t3_u:.1f} units = {t3_c:.2f} Birr")
    print("------------------------------------")
    print(f"Energy Charge         : {energy_charge:.2f} Birr")
    print(f"Fixed Service Fee     : {service_fee:.2f} Birr")
    print("====================================")
    print(f"TOTAL AMOUNT DUE      : {total_bill:.2f} Birr")
    print("====================================")


