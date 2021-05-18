import sys
import csv
from datetime import datetime

class CSVParser:
    def __init__(self):
        self.jobs_file = "t_jobs.csv"
        self.applicants_file = "t_applicants.csv"

        self.jobs_file_handler = None
        self.applicants_file_handler = None

    def parse(self, file_name):
        self.jobs_file_handler = open(self.jobs_file, "w")
        self.applicants_file_handler = open(self.applicants_file, "w")

        with open(file_name, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter=',', quotechar='"')
            self.process_file(lines)

        self.jobs_file_handler.close()
        self.applicants_file_handler.close()

    def process_file(self, lines):
        map_headers = self.get_map_headers(lines)
    
        for idx, line in enumerate(lines):
            self.write_job(idx, line, map_headers)
            self.write_aplicants(idx, line, map_headers)

    def get_map_headers(self, lines):
        try:
            headers = lines.__next__()
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

    def write_job(self, idx, line, map_headers):
        self.jobs_file_handler.write("{},{},{},{},{}\n".format(
            idx+1,
            line[map_headers['job title']],
            line[map_headers['job description']],
            line[map_headers['location']],
            self.convert_date(line[map_headers['date']])
        ))

    def convert_date(self, date):
        parsed_date = datetime.strptime(date, '%d/%m/%Y')
        return parsed_date.strftime('%Y-%m-%d')

    def write_aplicants(self, idx, line, map_headers):
        applicants = [x.strip() for x in line[map_headers['applicants']].split(',')]

        for applicant in applicants:
            self.applicants_file_handler.write("{},{}\n".format(
                idx+1,
                applicant
            ))

# TODO : Do argument validation and add a help menu
file_name = sys.argv[1]

parser = CSVParser()
parser.parse(file_name)
