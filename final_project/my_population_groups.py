# file: my_population_groups.py
# A python module containing a basic version of the population_groups class and related code

PASSED = 'Passed'
FAILED = 'Failed'


class Population:

    def __init__(self, category, male_count, female_count, calculate_total):
        self.category = category
        self.male_count = male_count
        self.female_count = female_count
        self.calculate_total = calculate_total

    def calculate_total_count(self):
        return int(self.male_count + self.female_count)

    def calculate_error_count(self):
        return

    @property
    def category(self):
        return self.__category

    @property
    def category_percentage(self):
        return self.__category

    @category.setter
    def category(self, category):
        if category == '':
            raise AttributeError('category may not be set to a empty string.')
        self.__category = category

    @property
    def male_count(self):
        return self.__male_count

    @male_count.setter
    def male_count(self, male_count):
        if male_count < 0:
            raise AttributeError('male_count may not be set to a value less than zero')
        self.__male_count = male_count

    @property
    def female_count(self):
        return self.__female_count

    @female_count.setter
    def female_count(self, female_count):
        if female_count < 0:
            raise AttributeError('female_count may not be set to a value less than zero')
        self.__female_count = female_count

    def __str__(self):
        message = []
        message.append('Population:')
        message.append('[category =')
        message.append(self.category + ']')
        message.append('[male_count =')
        message.append(str(self.male_count) + ']')
        message.append('[female_count =')
        message.append(str(self.female_count) + ']')
        message.append('[total_count =')
        message.append(str(self.calculate_total_count()) + ']')
        return ''.join(message)

    def __repr__(self):
        return self.__str__()


def main():
    print('Unit testing output follows...')

    print('\n Test 1: Test Constructor')
    expected_category = 'Male'
    expected_male_count = 97680
    expected_female_count = 93991
    expected_calculate_total = 191671
    s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    actual_category = expected_category
    actual_male_count = s1.male_count
    actual_female_count = s1.female_count
    if actual_category != expected_category or actual_male_count != expected_male_count or actual_female_count\
            != expected_female_count:
        print(FAILED)
    else:
        print(PASSED)

    print('\n Test 2: Attempt to set category attribute to empty string')
    expected_category = ''
    expected_male_count = 97680
    expected_female_count = 93991
    expected_calculate_total = 191671

    test_result = FAILED
    try:
        s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    except AttributeError as ae:
        if str(ae) == 'category may not be set to a empty string.':
            test_result = PASSED
    finally:
        print(test_result)

    print('\n Test 3: Attempt to set male_count attribute to negative value')
    expected_category = 'Male'
    expected_male_count = -1
    expected_female_count = 93991
    expected_calculate_total = 191671

    test_result = FAILED
    try:
        s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    except AttributeError as ae:
        if str(ae) == 'male_count may not be set to a value less than zero':
            test_result = PASSED
    finally:
        print(test_result)

    print('\n Test 4: Attempt to set female_count attribute to negative value')
    expected_category = 'Female'
    expected_male_count = 97680
    expected_female_count = -1
    expected_calculate_total = 191671

    test_result = FAILED
    try:
        s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    except AttributeError as ae:
        if str(ae) == 'female_count may not be set to a value less than zero':
            test_result = PASSED
    finally:
        print(test_result)

    print('\n Test 5: Test calculate_total_count() method')
    expected_category = 'Male'
    expected_male_count = 97680
    expected_female_count = 93991
    expected_calculate_total = 191671

    calculate_total_count = Population('Male', 97680, 93991, 191671)
    calculate_total_count.calculate_total_count()
    try:
        s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    except AttributeError as ae:
        if expected_male_count + expected_female_count == calculate_total_count:
            test_result = PASSED
    finally:
        print(test_result)

    print('\n Test 6: Test __str__ Method')
    expected_category = 'Male'
    expected_male_count = 97680
    expected_female_count = 93991
    expected_calculate_total = 191671

    s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    expected_str_value = 'Population:[category =Male][male_count =97680][female_count =93991][total_count =191671]'
    actual_str_value = (str(s1))
    if actual_str_value != expected_str_value:
        print(FAILED)
    else:
        print(PASSED)

    print('\n Test 7: Test __repr__ Method')
    expected_category = 'Male'
    expected_male_count = 97680
    expected_female_count = 93991
    expected_calculate_total = 191671

    s1 = Population(expected_category, expected_male_count, expected_female_count, expected_calculate_total)
    expected_repr_value = 'Population:[category =Male][male_count =97680][female_count =93991][total_count =191671]'
    actual_repr_value = (repr(s1))
    if actual_repr_value != expected_repr_value:
        print(FAILED)
    else:
        print(PASSED)


if __name__ == '__main__':
    main()