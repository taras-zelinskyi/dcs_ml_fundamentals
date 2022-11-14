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
    sort = sorted(sum_dict.items())
    sums_dict = {}
    for key, value in sort:
        sums_dict[key] = value
    return sums_dict


def generate_products(pairs):
    prod_dict = {}
    for item in pairs:
        prod = item[0] * item[1]
        if prod in prod_dict:
            if item[::-1] not in prod_dict[prod]:
                prod_dict[prod].append(item)
        else:
            prod_dict[prod] = [item]
    sort = sorted(prod_dict.items())
    prodd_dict = {}
    for key, value in sort:
        prodd_dict[key] = value
    return prodd_dict


def delete_product_single_pairs(primary_pairs):
    i = 1
    new_pairs = []
    for key, value in generate_products(primary_pairs).items():
        if len(value) > 1:
            i += 1
            new_pairs += value
    return new_pairs


def check_to_receive_product_need_at_least_two_pairs(secondary_pairs):
    new_pairs = []
    sum_dict = generate_sums(secondary_pairs)
    new_dict = {}
    for key, value in sum_dict.items():
        temp_value = []
        for pair in value:
            prod = pair[0] * pair[1]
            divider_count = 0
            for divider in range(2, 99):
                if prod % divider == 0 and ((prod / divider) < 99):
                    divider_count += 1
            if divider_count < 4:
                break
            else:
                temp_value.append(pair)
        if value == temp_value:
            for pair in value:
                new_pairs.append(pair)
            new_dict[key] = value
    return new_pairs


second_pairs = check_to_receive_product_need_at_least_two_pairs(candidate_pairs())
print(second_pairs)



def only_one_pair_have_correct_dividers(pairs):
    prod_dict = generate_products(pairs)
    sum_dict = generate_sums(pairs)

    for key, value in prod_dict.items():
        value_count = 0
        result_pair = []
        for pair in value:
            sum_ = pair[0] + pair[1]

            new_pairs = []
            for pair in sum_dict[sum_]:
                temp_value = []
                for pair_ in value:
                    prod = pair_[0] * pair_[1]
                    divider_count = 0
                    for divider in range(2, 99):
                        if prod % divider == 0 and ((prod / divider) < 99):
                            divider_count += 1
                    if divider_count < 4:
                        break
                    else:
                        temp_value.append(pair)
                if value == temp_value:
                    for pair in value:
                        new_pairs.append(pair)
                    result_pair.append(pair)
                    value_count += 1
        if result_pair == 1:
            return result_pair


third_pair = only_one_pair_have_correct_dividers(second_pairs)
# print(third_pair)
# print(generate_sums(candidate_pairs()))