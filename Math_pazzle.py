def candidate_pairs():
    candidates_pairs = []
    for number in range(2, 100):
        for number_2 in range(2, 100):
            candidates_pairs.append([number, number_2])
    return candidates_pairs


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


primary_pairs = candidate_pairs()
# print(len(primary_pairs))


def delete_product_single_pairs(primary_pairs):
    new_pairs = []
    product_pairs = [value[0] for key, value in generate_products(primary_pairs).items() if len(value) == 1]
    for pair in primary_pairs:
        if pair not in product_pairs:
            new_pairs.append(pair)
    return new_pairs


secondary_pairs = delete_product_single_pairs(primary_pairs)
# print(secondary_pairs)
# print(len(secondary_pairs))


def check_to_receive_product_need_at_least_two_pairs(secondary_pairs):
    sums = generate_sums(secondary_pairs)
    new_pairs = []
    for key, value in sums.items():
        for pair in value:
            prod = pair[0] * pair[1]
            divider_count = 0
            for divider in range(2, prod):
                if prod % divider == 0:
                    divider_count += 1
            if divider_count >= 4:
                new_pairs.append(pair)

    return new_pairs


third_pairs = check_to_receive_product_need_at_least_two_pairs(secondary_pairs)
print(third_pairs)
print(len(third_pairs))

generated_prod = generate_products(third_pairs)
# for key, value in generated_prod.items():
#     print(f"{key}: {value}")


def third_step(pairs, first_pairs):
    prod_dict = generate_products(pairs)
    new_pairs = []
    sums_dict = generate_sums(first_pairs)
    for key, value in prod_dict.items():
        pair_count = 0
        if pair_count == 0:
            for pair in value:
                sums = pair[0] + pair[1]
                additions = sums_dict[sums]
                for pr in additions:
                    pr = pr[0] * pr[1]
                    divider_count = 0
                    for divider in range(2, pr):
                        if pr % divider == 0:
                            divider_count += 1
                    if divider_count >= 4:
                        new_pairs.append(tuple(pair))
                        pair_count += 1
                        break
                    break
                break
    return set(new_pairs)


fourth_pairs = third_step(third_pairs, primary_pairs)
print(fourth_pairs)
print(len(fourth_pairs))


# third_pairs = check_to_receive_product_need_at_least_two_pairs(secondary_pairs)
# print(len(third_pairs))
#
# def check_to_receive_sum_need_one_pair(third_pairs):
#     prod = generate_products(third_pairs)
#     second = generate_sums(third_pairs)
#     new_pairs = []
#     for key, value in prod.items():
#         for pair in value:
#             sum_ = pair[0] + pair[1]
#             if sum_ in second:
#                 new_pairs.append(pair)
#     return new_pairs
#
#
# def leave_sum_single_pairs(fourth_pairs):
#     new_pairs = []
#     product_pairs = generate_sums(fourth_pairs).values()
#     for pair in product_pairs:
#         if len(pair) == 1:
#             new_pairs.append(pair[0])
#     return new_pairs





