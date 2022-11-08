import numpy


def candidate_pairs():
    candidates_pairs = []
    for number in range(1, 100):
        for number_2 in range(1, 100):
            candidates_pairs.append([number, number_2])
    return candidates_pairs


primary_pairs = candidate_pairs()


def generate_sums(pairs):
    sum_dict = {}
    for item in pairs:
        if sum(item) in sum_dict:
            if item[::-1] not in sum_dict[sum(item)]:
                sum_dict[sum(item)].append(item)
        else:
            sum_dict[sum(item)] = [item]

    # print
    # for key, value in sum_dict.items():
    #     print(f"{key}: {value}")
    return sum_dict


def generate_products(pairs):
    prod_dict = {}
    for item in pairs:
        prod = item[0]*item[1]
        if prod in prod_dict:
            if item[::-1] not in prod_dict[prod]:
                prod_dict[prod].append(item)
        else:
            prod_dict[prod] = [item]
    sort = sorted(prod_dict.items())
    for key, value in sort:
        prod_dict[key] = value
        # print(f"{key}: {value}")
    return prod_dict


def delete_product_single_pairs(primary_pairs):
    new_pairs = []
    product_pairs = [value[0] for key, value in generate_products(primary_pairs).items() if len(value) == 1]
    for pair in primary_pairs:
        if pair not in product_pairs:
            new_pairs.append(pair)
    return new_pairs


def delete_sum_single_pairs(secondary_pairs):
    new_pairs = []
    for value in generate_sums(secondary_pairs).values():
        if len(value) != 1:
            for pair in value:
                new_pairs.append(pair)

    return new_pairs


def leave_product_single_pairs(third_pairs):
    new_pairs = []
    product_pairs = generate_products(third_pairs).values()
    for pair in product_pairs:
        if len(pair) == 1:
            new_pairs.append(pair[0])
    return new_pairs


def leave_sum_single_pairs(fourth_pairs):
    new_pairs = []
    product_pairs = generate_sums(fourth_pairs).values()
    for pair in product_pairs:
        if len(pair) == 1:
            new_pairs.append(pair[0])
    return new_pairs


secondary_pairs = delete_product_single_pairs(primary_pairs)
third_pairs = delete_sum_single_pairs(secondary_pairs)
fourth_pairs = leave_product_single_pairs(third_pairs)
final_pair = leave_sum_single_pairs(fourth_pairs)

print(len(secondary_pairs))
print(len(third_pairs))
print(len(fourth_pairs))
print(len(final_pair))

# prod = generate_products(final_pair)
# sums = generate_sums(final_pair)


# for key, value in prod.items():
#         print(f"{key}: {value}")
#
# print("=============")
# for key, value in sums.items():
#     print(f"{key}: {value}")

