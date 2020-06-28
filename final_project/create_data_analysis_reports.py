# file: create_data_analysis_reports.py
# this program produces eight data analysis reports from the cleaned_data.txt file

from my_population_groups import Population


def main():

    populations = get_population_instances()

    populations.sort(key=by_category, reverse=True)
    print_count_based_report(populations, 'Counts by Age Group')

    populations.sort(key=by_male_count, reverse=True)
    print_count_based_report(populations, 'Counts by Descending Male Count')

    populations.sort(key=by_female_count, reverse=True)
    print_count_based_report(populations, 'Counts by Descending Female Count')

    populations.sort(key=by_total_count, reverse=True)
    print_count_based_report(populations, 'Counts by Descending Total Count')


def get_population_instances():
    population_group = Population('0-14', 97680, 93991, 191671)
    infile_name = input('Please enter input file name: ')
    infile = open(infile_name, 'r',  encoding='utf-8')
    population_data = []
    for line in infile:
        category, male_count, female_count, calculate_total = line.split()
        population_data.append(Population(category, int(male_count), int(female_count),
                                          int(population_group.calculate_total_count())))

    infile.close()

    return population_data


def print_count_based_report(these_sorted_populations, count_report_title):
    count_report_title = count_report_title.center(50)
    print()
    print(count_report_title)
    print()
    print('{0:<10}{1:>10}{2:>10}{3:>10}'.format(
        'Age Group', 'Males', 'Females', 'Total'))
    for population_data in these_sorted_populations:

        print('{0:<10}{1:>10}{2:>10}{3:>10}'.format(
            population_data.category, population_data.male_count, population_data.female_count,
            population_data.calculate_total))


def by_category(population_data):
    return population_data.category


def by_male_count(population_data):
    return population_data.male_count


def by_female_count(population_data):
    return population_data.female_count


def by_total_count(population_data):
    return population_data.calculate_total


main()
