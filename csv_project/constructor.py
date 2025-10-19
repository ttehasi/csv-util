from csv_project.utils import make_table, processing, unite


def generate_report(filelist: list, format_report):
    result = '''You have to wrtire the correct report type. 
Usage main.py -h [--help]'''
    match format_report:
        case 'average-rating':
            general_data = unite(filelist)
            data_of_brand_and_atributs = processing(general_data)
            result = make_table(data_of_brand_and_atributs)
    return result