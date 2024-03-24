def main():
    print("Welcome to the Stock Fundamental Analysis Program")
    print("Please enter the following fundamental analysis metrics for the stock:")

    # Get user input for fundamental analysis metrics
    stock_name = input("Enter the stock name: ")
    current_price = float(input("Enter the current price per share ($): "))
    earnings_per_share = float(input("Enter the earnings per share ($): "))
    book_value_per_share = float(input("Enter the book value per share ($): "))
    debt = float(input("Enter the total debt ($): "))
    cash_flow = float(input("Enter the operating cash flow ($): "))
    dividend_yield = float(input("Enter the dividend yield (%): "))
    market_cap = float(input("Enter the market capitalization ($): "))
    roe = float(input("Enter the return on equity (%): "))

    # Perform analysis based on user inputs
    print("\nStock Fundamental Analysis for:", stock_name)
    print("--------------------------------------------------")
    print("Current Price per Share: $", current_price)
    print("Earnings per Share: $", earnings_per_share)
    print("Book Value per Share: $", book_value_per_share)
    print("Total Debt: $", debt)
    print("Operating Cash Flow: $", cash_flow)
    print("Dividend Yield: ", dividend_yield, "%")
    print("Market Capitalization: $", market_cap)
    print("Return on Equity (ROE): ", roe, "%")

    if current_price < book_value_per_share:
        print("The stock is trading below its book value per share.")
    else:
        print("The stock is trading above or at its book value per share.")

    if debt == 0:
        print("The company has no debt, which is positive.")
    else:
        print("The company has debt totaling $", debt)

    if cash_flow > 0:
        print("The company is generating positive operating cash flow.")
    else:
        print("The company is not generating positive operating cash flow.")

    if dividend_yield > 0:
        print("The stock pays a dividend yield of", dividend_yield, "%")
    else:
        print("The stock does not pay a dividend.")

    if roe > 0:
        print("The company has a positive return on equity (ROE).")
    else:
        print("The company has a negative return on equity (ROE).")

if __name__ == "__main__":
    main()




