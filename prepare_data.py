import csv

COLUMNS = [
    "Mothers Single Years of Age",
    "Mothers Age Recode 9",
    "Cigarettes Before Pregnancy",
    "Cigarettes 1st Trimester",
    "Cigarettes 2nd Trimester",
    "Cigarettes 3rd Trimester",
    "Body Mass Index",
    "Body Mass Index Recode",
    "No Risk Factors Reported",
    "No Infections Reported",
    "Five Minute APGAR Score",
    "Five Minute APGAR Recode"
]

INDICES = [
    [74, 76],
    [78, 79],
    [252, 254],
    [254, 256],
    [256, 258],
    [258, 260],
    [282, 286],
    [286, 287],
    [336, 337],
    [352, 353],
    [443, 445],
    [445, 446]
]

MISSING_VALUES = [
    None,
    None,
    '99',
    '99',
    '99',
    '99',
    '99.9',
    '9',
    '9',
    '9',
    '99',
    '5'
]

INPUT_FILE = 'Nat2020PublicUS.c20210506.r20210812.txt'
OUTPUT_FILE = 'natality_dataset.csv'

MAX_NO_READINGS = 100000


def is_data_correct(data):
    for single_data, not_reported_value in zip(data, MISSING_VALUES):
        if not_reported_value is not None and single_data == not_reported_value:
            return False
    return True


def main():
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        with open(INPUT_FILE, encoding='utf-8') as f:
            no_correct_readings = 0
            for no_readings, row in enumerate(f, 1):
                data = [row[index[0]:index[1]] for index in INDICES]
                if is_data_correct(data):
                    writer.writerow(data)
                    no_correct_readings += 1
                    if no_correct_readings == MAX_NO_READINGS:
                        print(f'Number of inputs read before gaining data: {no_readings}')
                        break

            print(f'Number of data left: {len(f.readlines())}')


if __name__ == '__main__':
    main()
