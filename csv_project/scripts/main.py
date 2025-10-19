import argparse

from csv_project.constructor import generate_report


def main():
    parser = argparse.ArgumentParser(
        # prog='evaluation',
        description='''Provides a report on the selected settings'''
        )
    parser.add_argument('--files', nargs='+', 
                        help='Add file in result collection')
    parser.add_argument('--report', required=True,
                        help='Show what will as a result.\
                            You can use "average-rating" type', 
                            default='average-rating')
    report = generate_report(parser.parse_args().files, 
                             parser.parse_args().report)
    print(report)


if __name__ == '__main__':
    main()
