class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        pass
    
    def add_item(self, name, price, quantity=1):
        for i in range(quantity):
            self.items.append({'item': name, 'price': price})
        self.total += price * quantity
        return self.total
    
    def mean_item_price(self):
        return round(self.total / len(self.items), 2)

    def median_item_price(self): 
        item_list = []
        for i in range(len(self.items)):
            item_list.append(self.items[i]['price'])
        sorted_list = sorted(item_list)
        mid = len(sorted_list) // 2
        if len(sorted_list) % 2 == 1: 
            median = sorted_list[(mid + 1)]
        else:
            median = round((sorted_list[mid] + sorted_list[mid + 1]) / 2, 2)
        return median

    def apply_discount(self):
        if self.employee_discount is None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self.total * (1 - (self.employee_discount / 100))

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
            self.total -= removed_item['price']
            return removed_item
        else:
            return "Nothing in your cart to remove."