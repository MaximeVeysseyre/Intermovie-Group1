import os

class Credentials():
    RAW_LOCAL_PATH = os.getcwd() + os.sep + 'data' + os.sep + 'RAW' + os.sep
    CURATED_LOCAL_PATH = os.getcwd() + os.sep + 'data' + os.sep + 'CURATED' + os.sep
    TITLE_BASICS = r'title.basics.tsv'
    TITLE_AKAS = r'title.akas.tsv'
    TITLE_PRINCIPALS = r'title.principals.tsv'
    TITLE_RATINGS = r'title.ratings.tsv'
    NAME_BASICS = r'name.basics.tsv'
