from os import listdir
import re
from tsv_reader import tsv_reader
from pprint import pprint
import openpyxl

'''
0 for apply
1 for star
'''
MODE = 0
MODE_LIST = {
    0:"apply",
    1:"star"
}

def parse_src(fname:str):
    print(f"cur year:{fname}")
    return [ 
        [fname[-3:]] + l[-2:] + [l[1][idx]+(f"({it})" if it[0]=="x" else "") for idx, it in enumerate(l[2].strip().split(' '))]
        for l in tsv_reader(f"{fname}/{MODE_LIST[MODE]}")
    ]

def export_xlsx(basedir:str):
    workbook = openpyxl.Workbook()
    sheet = workbook.worksheets[0]
    sheet.append(["學年度", "學校", "科系", "國文申請最低門檻", "英文申請最低門檻", "數學申請最低門檻", "社會申請最低門檻", "自然申請最低門檻"])
    for d in listdir(basedir):
        if re.match("^[0-9]{3}$", d):
            for l in parse_src(f"{basedir}/{d}"):
                sheet.append(l)
    workbook.save(f"{MODE_LIST[MODE]}.xlsx")

def main():
    export_xlsx("gsat/data")

if __name__ == "__main__":
    main()