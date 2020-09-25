from .credentials import Credentials as cr
import csv

import os

def split_datas(filename, columnwanted):
    
    '''
    Break raw data into many files
    '''

    RAW_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "RAW" + os.sep
    CURATED_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "CURATED" + os.sep

    csv.field_size_limit(10000000)
    
    with open(RAW_LOCAL_PATH + filename, encoding='utf-8') as file_stream:    
        file_stream_reader = csv.DictReader(file_stream, delimiter='\t')
        
        open_files_references = {}

        for row in file_stream_reader:
            title_type = row[columnwanted]

            # Open a new file and write the header
            if title_type not in open_files_references:
                output_file = open(cr.CURATED_LOCAL_PATH + '{}.csv'.format(title_type), 'w', encoding='utf-8', newline='')
                dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                # dw.writeheader()
                open_files_references[title_type] = output_file, dictionary_writer
            # Always write the row
            open_files_references[title_type][1].writerow(row)
        # Close all the files
        for output_file, _ in open_files_references.values():
            output_file.close()
