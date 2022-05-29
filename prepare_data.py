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

INPUT_FILE = 'Nat2020PublicUS.c20210506.r20210812.txt'
OUTPUT_FILE = 'natality_dataset.csv'

MAX_NO_READINGS = 100000


if __name__ == '__main__':
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        with open(INPUT_FILE, encoding='utf-8') as f:
            for i, row in enumerate(f, 1):
                data = [row[index[0]:index[1]] for index in INDICES]
                writer.writerow(data)
                if i == MAX_NO_READINGS:
                    break
