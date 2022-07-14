import PyPDF2
from datetime import datetime

class PdfParser:
    # initializing the attributes
    def __init__(self, filepath):
        self.text = None
        self.content_dict = None
        self.FILE_PATH = filepath
        self.date_time = str(datetime.now()).replace(" ", "--").replace(":", "-").split(".")[0]

        self.keys = ["District", "Police Station", "Year", "FIR No.", "Date", "Day.", "Date from",
                     "Date to", "Time Period", "Time from", "Time to", "Place of Occurrence",
                     "Direction and distance from P.S.", "Address", "Name", "Father's",
                     "Date/Year of Birth", "Nationality"]
        self.dict_keys = ["dist_name", "police_station", "year", "fir_no_org", "date",
                          "occurrence_of_offence_day", "occurrence_of_offence_date_from",
                          "occurrence_of_offence_date_to", "occurrence_of_offence_time_period",
                          "occurrence_of_offence_time_from", "occurrence_of_offence_time_to",
                          "place_of_occurrence_district_org", "place_of_occurrence_name_of_police_station",
                          "details_address_1", "complaint_informan_name",
                          "complaint_informan_father_husband_name", "complaint_informan_date_year_of_birth",
                          "complaint_informan_nationality"]
        self.vals = ["" for i in range(len(self.keys))]

    # To check the next whitespace in the string
    def whitespace(self, strt, text):
        str_ = ""
        for i in range(strt, len(text)):
            if text[i] != " ":
                # chng = "#/" if text[i] == "[" else text[i]
                str_ += text[i]
            else:
                return str_
        return str_

    # Parsing the pdf contents
    def parse_(self):
        with open(self.FILE_PATH, mode='rb') as f:
            # reading and getting the contents
            reader = PyPDF2.PdfFileReader(f)
            page = reader.getPage(0)
            self.text = page.extractText()

        return self.text

    # getting the content
    def get_content(self, print_logs=False):
        self.text = self.parse_()
        for i in range(len(self.keys)):
            # getting the results from the extracted content
            occurence = self.text.find(self.keys[i])
            result = self.whitespace(occurence + len(self.keys[i]) + 1, self.text)

            # To see the logs in terminal
            if print_logs:
                print(f"{self.dict_keys[i]}: {result}")

            self.vals[i] = result

        result_dict = {self.dict_keys[i]: str(self.vals[i]) for i in range(len(self.dict_keys))}
        # for keys in self.dict_keys:
        #     for values in self.vals:
        #         result_dict[keys] = values
        #         self.vals.remove(values)
        #         break

        return result_dict


if __name__ == "__main__":
    parser = PdfParser("FIR Sample update.pdf")
    # print(len(parser.keys), len(parser.dict_keys))
    # print(parser.vals)
    content = parser.get_content(print_logs=False)
    print(content)