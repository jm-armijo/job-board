import sys
import csv

class CSVParser:

    def parse(file_name):
        with open(file_name, newline='') as csvfile:
            content = csv.reader(csvfile, delimiter=',', quotechar='"')
            CSVParser.process_file(content)

    def process_file(content):
        map_headers = CSVParser.__get_map_headers(content)
    
        for row in content:
            job = CSVParser.get_job(row, map_headers)
            aplicants = CSVParser.get_aplicants(row, map_headers)
            print(job)

    def __get_map_headers(content):
        try:
            headers = content.__next__()
        except StopIteration:
            # If the file is empty, return an empty hash
            return {}

        return {
            'job title': headers.index('job title'),
            'job description': headers.index('job description'),
            'date': headers.index('date'),
            'location': headers.index('location'),
            'applicants': headers.index('applicants')
        }

    def get_job(row, map_headers):
        return [
            row[map_headers['job title']],
            row[map_headers['job description']],
            row[map_headers['location']],
            row[map_headers['date']]
        ]

    def get_aplicants(row, map_headers):
        # Split applicants by comma and trim (strip) spaces from each applicant
        return [x.strip() for x in row[map_headers['applicants']].split(',')]

# TODO : Do argument validation and add a help menu
file_name = sys.argv[1]
CSVParser.parse(file_name)
