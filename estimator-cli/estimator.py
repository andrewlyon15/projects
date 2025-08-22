print('Estimator CLI placeholder')
#!/usr/bin/env python3
import argparse
import math

def calculate_estimate(sqft, coats, coverage, paint_cost, hourly_rate, painters, margin):
    # Total area to paint
    total_area = sqft * coats

    # Calculate gallons needed (with 10% waste)
    raw_gallons = total_area / coverage
    gallons_needed = math.ceil(raw_gallons * 1.10 * 100) / 100  # round up to 2 decimals

    # Material cost
    material_cost = round(gallons_needed * paint_cost, 2)

    # Labor hours and cost
    labor_hours = round(total_area / (150 * painters), 2)  # assuming 150 sqft/hour per painter
    labor_cost = round(labor_hours * hourly_rate * painters, 2)

    # Overhead (10% of materials + labor)
    overhead = round(0.10 * (material_cost + labor_cost), 2)

    # Suggested bid including margin
    subtotal = material_cost + labor_cost + overhead
    suggested_bid = round(subtotal * (1 + margin), 2)

    # Return a dictionary of results
    return {
        "Total Area (sqft x coats)": total_area,
        "Gallons Needed": gallons_needed,
        "Material Cost ($)": material_cost,
        "Labor Hours": labor_hours,
        "Labor Cost ($)": labor_cost,
        "Overhead ($)": overhead,
        "Suggested Bid ($)": suggested_bid
    }

def main():
    parser = argparse.ArgumentParser(description="Painting Job Estimator CLI")
    parser.add_argument("--sqft", type=float, required=True, help="Square footage to paint")
    parser.add_argument("--coats", type=int, default=2, help="Number of coats")
    parser.add_argument("--coverage", type=float, default=350.0, help="Sqft per gallon of paint")
    parser.add_argument("--paint-cost", type=float, required=True, help="Cost per gallon of paint")
    parser.add_argument("--hourly-rate", type=float, required=True, help="Labor hourly rate")
    parser.add_argument("--painters", type=int, default=1, help="Number of painters")
    parser.add_argument("--margin", type=float, default=0.25, help="Profit margin (0.25 = 25%)")

    args = parser.parse_args()

    results = calculate_estimate(
        sqft=args.sqft,
        coats=args.coats,
        coverage=args.coverage,
        paint_cost=args.paint_cost,
        hourly_rate=args.hourly_rate,
        painters=args.painters,
        margin=args.margin
    )

    print("\n=== Painting Estimate ===")
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
