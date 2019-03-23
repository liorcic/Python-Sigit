def multi(x):
    return x * x


def map_exercise(func_name, list_of_elements):
    results = []
    for element in list_of_elements:
        results.append(func_name(element))
    return results


elements = [2,4,6]
results_functions = map_exercise(multi, elements)
print(results_functions)