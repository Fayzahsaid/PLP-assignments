def  calculate_discount(price, discount_percent) :
    if discount_percent >= 20:
       discount_price = price - (price*discount_percent/100)
       return discount_price
    else:
        print(price)

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent) 
print(f"price after the discount is:{final_price}")

