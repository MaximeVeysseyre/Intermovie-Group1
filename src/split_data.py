import csv
import os

def split_data_title_basics():
        '''
        Break raw data into many files
        '''

        RAW_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "RAW" + os.sep
        TITLE_BASICS_FILE_NAME = "title.basics.tsv"
        CURATED_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "CURATED" + os.sep

        with open(RAW_LOCAL_PATH + TITLE_BASICS_FILE_NAME, encoding='utf-8') as file_stream:    
            file_stream_reader = csv.DictReader(file_stream, delimiter='\t')
            
            open_files_references = {}

            for row in file_stream_reader:
                title_type = row['titleType']

                # Open a new file and write the header
                if title_type not in open_files_references:
                    output_file = open(CURATED_LOCAL_PATH + '{}.csv'.format(title_type), 'w', encoding='utf-8', newline='')
                    dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                    dictionary_writer.writeheader()
                    open_files_references[title_type] = output_file, dictionary_writer
                # Always write the row
                open_files_references[title_type][1].writerow(row)
            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()


def split_data_title_principals():
        '''
        Break raw data into many files
        '''

        RAW_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "RAW" + os.sep
        TITLE_PRINCIPALS_FILE_NAME = "title.principals.tsv"
        CURATED_LOCAL_PATH = os.getcwd() + os.sep + "data" + os.sep + "CURATED" + os.sep

        with open(RAW_LOCAL_PATH + TITLE_PRINCIPALS_FILE_NAME, encoding='utf-8') as file_stream:    
            file_stream_reader = csv.DictReader(file_stream, delimiter='\t')
            
            open_files_references = {}

            for row in file_stream_reader:
                category = row['category']

                # Open a new file and write the header
                if category not in open_files_references:
                    output_file = open(CURATED_LOCAL_PATH + '{}.csv'.format(category), 'w', encoding='utf-8', newline='')
                    dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                    dictionary_writer.writeheader()
                    open_files_references[category] = output_file, dictionary_writer
                # Always write the row
                open_files_references[category][1].writerow(row)
            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()