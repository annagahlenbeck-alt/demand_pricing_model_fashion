# main function


def get_calc(name):
    while True:
        try:
            value = float(input(f"{name} (1-100): "))
            if 0 <= value <= 100:
                return value

            else:
                print("Value must be between 0 and 100")

        except ValueError:
            print("Please enter a number")


# trend calculator (weighted)
def calc_trend_score(search_interest, social_engagement, influencer_activity, sell_through_rate):
    trend_calc = (
        search_interest * 0.35 +
        social_engagement * 0.25 +
        influencer_activity * 0.20 +
        sell_through_rate * 0.20
    )

    if trend_calc >= 70:
        demand_level = "High"

    elif trend_calc >= 40:
        demand_level = "Medium"

    else:
        demand_level = "Low"

    return trend_calc, demand_level


# price optimization
def opti_price(cost, competitor_prices, brand_positioning):

    avg_competitor = sum(competitor_prices) / len(competitor_prices)

    if brand_positioning == "luxury":
        multiplier = 2.2

    elif brand_positioning == "premium":
        multiplier = 1.6

    else:
        multiplier = 1.2


# suggested retail price
    recommended_price = cost * multiplier

    if recommended_price < avg_competitor * 0.8:
        recommended_price = avg_competitor * 0.8

    wholesale_price = recommended_price * 0.5

    if recommended_price > avg_competitor * 1.2:
        price_effect = "Price may reduce demand due to premium positioning."

    elif recommended_price < avg_competitor:
        price_effect = "Price provides competitive advantage. "

    else:
        price_effect = "Price alinges with market expectations. "

    return recommended_price, wholesale_price, price_effect


def main():
    print("FASHION DEMAND ANALYSIS TOOL")

# Trend Input
    search_interest = get_calc("Search inetrest")
    social_engagement = get_calc("Social engagement")
    influencer_activity = get_calc("Influencer activity")
    sell_through_rate = get_calc("Sell-through rate")

    trend_calc, demand_level = calc_trend_score(
        search_interest, social_engagement, influencer_activity, sell_through_rate)

 # Pricing Inputs
    cost = float(input("\nProduction cost (€): "))

    competitors_raw = input("Competitor prices (comma-separated): ")
    competitor_prices = [float(x.strip()) for x in competitors_raw.split(",")]

    brand_positioning = input(
        "Brand positioning (luxury/premium/mid): ").lower()

# Price Optimization
    recommended_price, wholesale_price, price_effect = opti_price(
        cost, competitor_prices, brand_positioning
    )

# Final Output

    print("Results")
    print(f"Trend Score: {trend_calc:.1f}/100")
    print(f"Demand Level: {demand_level}")
    print(f"Recommended Retail Price: €{recommended_price:.2f}")
    print(f"Wholesale Price: €{wholesale_price:.2f}")
    print(f"Market Price Interpretation: {price_effect}")


if __name__ == "__main__":
    main()
