# Ben Chappell

# Calculates the cost function of the system using a specific formula

def main():
    eIn = 120
    price = 11222

    print(cost(eIn, price))

def cost(eIn, price):
    # Calculates the cost function as a sum of the two normed values
    # eIn is normed on a scale of 0 to 100, with the maximum value being associated with an eIn of 1200 MWh
    # price is normed on a scale of 0 to 100, with the maximum value being associated with an price of 1710368 $
    # These are then summed to represent the cost of the system
    maxEIn = 1200
    maxPrice = 1710368
    eInScale = 100
    priceScale = 100

    normedEIn = eInScale * (eIn / maxEIn)
    normedPrice = priceScale * (price / maxPrice)

    return normedEIn + normedPrice

if __name__ == "__main__":
    main()