def apply_discount(price, discount):
    if isinstance(price, int) == False and isinstance(price, float) == False:
        return "The price should be a number"
    if isinstance(discount, int) == False and isinstance(discount, float) == False:
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        discount = (discount / 100) * price
        final_price = price - discount
    return final_price

print(apply_discount(20, 10))