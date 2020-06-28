# file: detect_column_level_data_entry_errors.py
# this program produces a diagnostic report that shows data entry errors in each column

from my_population_groups import Population


def main():
    population_data = get_population_data()

    print_report(population_data, 'Column-Level Data Entry Errors')


def get_population_data():
    infile_name = input('Please enter input file name: ')
    infile = open(infile_name, 'r',  encoding='utf-8')
    population_data = []
    for line in infile:
        category, male_count, female_count, calculate_total = line.split()
        population_data.append(
            Population(category, int(male_count), int(female_count), int(calculate_total))
            )
    infile.close()
    return population_data


def calculate_column_total(population_data):
    return


def calculate_column_error(population_data):
    return


def print_report(this_population_data, report_title):
    print()
    print()
    print('{0:^50}'.format(report_title))
    print()
    print('{0:<20}{1:>10}{2:>15}{3:>15}'.format('Age Group', 'Males', 'Females', 'Total'))
    for population_data in this_population_data:
        print('{0:<20}{1:>10,.0f}{2:>15,.0f}{3:>15,.0f}'.format(
            population_data.category,
            population_data.male_count,
            population_data.female_count,
            population_data.calculate_total_count(),

        ))


main()
