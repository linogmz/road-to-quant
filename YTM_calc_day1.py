# YTM_calc_day1.py

def calculate_ytm(price, face_value, coupon_rate, years_to_maturity, frequency=1):
    periods = years_to_maturity * frequency
    coupon = coupon_rate * face_value / frequency

    def bond_price(ytm):
        return sum([coupon / (1 + ytm / frequency) ** t for t in range(1, periods + 1)]) + \
               face_value / (1 + ytm / frequency) ** periods

    def bond_price_derivative(ytm):
        return sum([-t * coupon / frequency / (1 + ytm / frequency) ** (t + 1) for t in range(1, periods + 1)]) + \
               -periods * face_value / frequency / (1 + ytm / frequency) ** (periods + 1)

    ytm = 0.05  # initial guess
    for _ in range(100):
        price_diff = bond_price(ytm) - price
        if abs(price_diff) < 1e-6:
            break
        ytm -= price_diff / bond_price_derivative(ytm)

    return round(ytm * 100, 4)  # as percentage

# Sample usage
if __name__ == "__main__":
    ytm = calculate_ytm(price=950, face_value=1000, coupon_rate=0.05, years_to_maturity=3)
    print(f"Estimated YTM: {ytm:.2f}%")
