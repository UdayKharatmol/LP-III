def knapsack(weights, values, capacity):
    n, max_value = len(values), 0

    def bound(item, weight, value):
        if weight >= capacity: return 0
        bound_val = value
        for i in range(item + 1, n):
            if weight + weights[i] <= capacity:
                bound_val += values[i]
                weight += weights[i]
            else:
                bound_val += values[i] * (capacity - weight) / weights[i]
                break
        return bound_val

    def branch_and_bound(item, weight, value):
        nonlocal max_value
        if weight <= capacity and value > max_value: max_value = value
        if item >= n - 1: return
        if bound(item, weight, value) > max_value:
            branch_and_bound(item + 1, weight + weights[item], value + values[item])
            branch_and_bound(item + 1, weight, value)

    branch_and_bound(0, 0, 0)
    return max_value

num_items = int(input("Enter the number of items: "))
weights, values = [], []
for i in range(num_items):
    weights.append(float(input(f"Enter weight of item {i+1}: ")))
    values.append(float(input(f"Enter value of item {i+1}: ")))

capacity = float(input("Enter knapsack capacity: "))
print(f"Maximum value in the knapsack: {knapsack(weights, values, capacity):.2f}")