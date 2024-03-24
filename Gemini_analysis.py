def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_rating(current_price, eps, book_value, total_debt, operating_cash_flow, dividend_yield, market_cap, roe):
    # Assign weights to different metrics (adjust as needed)
    price_to_earnings_ratio = current_price / eps
    price_to_book_ratio = current_price / book_value
    debt_to_equity_ratio = total_debt / market_cap  # Assuming market cap represents equity
    cash_flow_to_price_ratio = operating_cash_flow / market_cap

    # Basic scoring system (can be more complex)
    rating = 0
    if price_to_earnings_ratio < 15:
        rating += 2  # Lower P/E is generally better
    if price_to_book_ratio < 2:
        rating += 2  # Lower P/B is generally better
    if debt_to_equity_ratio < 0.5:
        rating += 1  # Lower debt-to-equity is generally better
    if cash_flow_to_price_ratio > 0.05:
        rating += 1  # Positive cash flow is good
    if dividend_yield > 2:
        rating += 1  # Higher dividend yield is attractive (consider sustainability)
    if roe > 0.15:
        rating += 1  # Higher ROE suggests good profitability

    # Normalize rating to 1-10 scale
    rating = min(rating, 10)  # Limit rating to 10
    return rating

def main():
    # Get user input for financial metrics
    stock_name = input("Enter the stock name: ")
    current_price = get_user_input("Enter the current price per share ($): ")
    earnings_per_share = get_user_input("Enter the earnings per share ($): ")
    book_value_per_share = get_user_input("Enter the book value per share ($): ")
    total_debt = get_user_input("Enter the total debt ($): ")
    operating_cash_flow = get_user_input("Enter the operating cash flow ($): ")
    dividend_yield = get_user_input("Enter the dividend yield (%): ")
    market_capitalization = get_user_input("Enter the market capitalization ($): ")
    return_on_equity = get_user_input("Enter the return on equity (%): ")

    # Print fundamental analysis summary
    print(f"\nStock Fundamental Analysis for: {stock_name}")
    print("--------------------------------------------------")
    print(f"Current Price per Share: $ {current_price:.2f}")
    print(f"Earnings per Share: $ {earnings_per_share:.2f}")
    print(f"Book Value per Share: $ {book_value_per_share:.2f}")
    print(f"Total Debt: $ {total_debt:,.2f}")
    print(f"Operating Cash Flow: $ {operating_cash_flow:,.2f}")
    print(f"Dividend Yield: {dividend_yield:.2f} %")
    print(f"Market Capitalization: $ {market_capitalization:,.2f}")
    print(f"Return on Equity (ROE): {return_on_equity:.2f} %")

    # Calculate rating
    rating = calculate_rating(current_price, eps=earnings_per_share, book_value=book_value_per_share,
                              total_debt=total_debt, operating_cash_flow=operating_cash_flow,
                              dividend_yield=dividend_yield, market_cap=market_capitalization, roe=return_on_equity)
    print(f"\nOverall Rating (1-10): {rating}")

if __name__ == "__main__":
    main()
