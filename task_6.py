def greedy_algorithm(products: dict, budget: int):
    product_list = get_product_list(products)
    sorted_products = get_sorted_products_by_ratio(product_list)

    result = []

    for product in sorted_products:
        if product["cost"] > budget:
            continue
        result.append(product)
        budget -= product["cost"]

    return result
    
def get_product_list(products: dict):
    return [{"name": name, **data} for name, data in products.items()]


def get_sorted_products_by_ratio(products: list):
    for product in products:
        product["ratio"] = product["calories"] / product["cost"]

    sorted_products = sorted(products, key=lambda d: d["ratio"], reverse=True)
    return sorted_products


def dynamic_programming_up_bottom(products: dict, budget: int):
    product_list = get_product_list(products)

    memo ={}
    result = get_max_calories(product_list, budget, memo)
    return result


def get_max_calories(products, budget, memo):
    if budget <= 0 or not products:
        return []
    
    remaining_key = tuple(sorted(p["name"] for p in products))
    key = (budget, remaining_key)

    if key in memo:
        return memo[key]

    groups = []
    for product in products:
        if product["cost"] > budget:
            continue

        rest_prod = [p for p in products if p["name"] != product["name"]]
        group = get_max_calories(rest_prod, budget - product["cost"], memo)
        group = group + [product]
       
        groups.append(group)

    best_group = max(groups, key=lambda group: sum(item.get("calories", 0) for item in group), default=[])
    memo[key] = best_group

    return best_group


def dynamic_programming_bottom_up(products: dict, budget: int):
    product_list = get_product_list(products)
    sorted_products = sorted(product_list, key=lambda d: d["cost"])
    p= len(products)
    # K = [[0 for p in range(budget + 1)] for i in range(p + 1)]
    K = [[(0, []) for p in range(budget + 1)] for i in range(p + 1)]

    for i in range(1, p + 1):
        for j in range(1, budget + 1):
            current_product = sorted_products[i-1]
            cost = current_product["cost"]
            if cost > j:
                K[i][j] = K[i-1][j]
            else:
                # print(f'else [{i}-{j}]' , j, '-',  sorted_products[i-1]["cost"])
                if K[i-1][j-cost][0] + current_product["calories"] > K[i-1][j][0]:
                    # K[i][j] = K[i-1][j-cost] + current_product["calories"]
                    new_cal = K[i-1][j-cost][0] + current_product["calories"]
                    new_list = K[i-1][j-cost][1] + [current_product]
                    K[i][j] = (new_cal, new_list)

                    
                else:
                    K[i][j] = K[i-1][j]

                # K[i][j] = max(K[i-1][j-cost] + sorted_products[i-1]["calories"], K[i-1][j])
                # result.append()

    # for i in range(budget+2):
    #     if i == 0:
    #         print(f"{'Product':<10}", end="")
    #     else:
    #         print(f"{i-1:<4}", end="")
    # print()        
    # for i in range(p+1):
    #     for j in range(budget + 2):
    #         if j == 0:
    #             if i == 0:
    #                 print(f"{"0":<10}", end="")
    #             else:
    #                 print(f"{sorted_products[i-1]["name"]:<10}", end="")
    #         else:
    #             print(f"{K[i][j-1][0]:<4}", end="")
    #     print()
    
    return K[p][budget][1]



items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def show_result(name, result):
    print(f"{name}: ")
    print(f"Next products were picked up: {', '.join(item['name'] for item in result)}")
    print(f"With total calories: {sum(item['calories'] for item in result)}")


budget = 100

result = greedy_algorithm(items, budget)
show_result("greedy_algorithm", result)
# print("greedy_algorithm: ")
# print(f"Next products were picked up: {', '.join(item['name'] for item in result)}")
# print(f"With total calories: {sum(item['calories'] for item in result)}")

print('-'*100)
result = dynamic_programming_up_bottom(items, budget)
show_result("dynamic_algorithm_up_bottom", result)
# print("dynamic_algorithm_up_bottom: ")
# print(f"Next products were picked up: {', '.join(item['name'] for item in result)}")
# print(f"With total calories: {sum(item['calories'] for item in result)}")

print('-'*100)
result = dynamic_programming_bottom_up(items, budget)
show_result("dynamic_algorithm_bottom_up", result)
# print("dynamic_algorithm_bottom_up: ")
# print(f"Next products were picked up: {', '.join(item['name'] for item in result[1])}")
# print(f"With total calories: {result[0]}")
