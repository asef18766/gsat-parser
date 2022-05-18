import csv
def tsv_reader(fname:str):
    with open(fname, "r", encoding="utf-8") as file:
        tsv_file = csv.reader(file, delimiter="\t")
        return [line for line in tsv_file]