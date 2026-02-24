import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import (BASE_DIR, DATETIME_FORMAT, DEFAULT_FORMAT,
                       ENCODING_UTF8, FILE_FORMAT, PRETTY_FORMAT, RESULTS)

FILE_OUTPUT_INFO = 'Файл с результатами был сохранён: {file_path}'


def default_output(results, *args):
    for row in results:
        print(*row)


def pretty_output(results, *args):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args):
    results_dir = BASE_DIR / RESULTS
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding=ENCODING_UTF8) as f:
        csv.writer(
            f, dialect=csv.unix_dialect,
        ).writerows(
            results,
        )
    logging.info(FILE_OUTPUT_INFO.format(file_path=file_path))


OUTPUTS = {
    PRETTY_FORMAT: pretty_output,
    FILE_FORMAT: file_output,
    DEFAULT_FORMAT: default_output,
}


def control_output(results, cli_args):
    OUTPUTS.get(cli_args.output)(results, cli_args)
