import csv
import pandas as pd

def MW_calculation(file_name):
        positive_sum = 0.0
        total_sum = 0.0
        with open(file_name) as file:
            tsv_file = csv.reader(file, delimiter="\t")
            for line in tsv_file:
                if line[1] != "model":
                    if line[5] == "expected":
                        positive_sum += float(line[6])
                        print(line[5])
                        total_sum += float(line[6])
                    else:
                        total_sum += float(line[6])
        return(positive_sum / total_sum)
    


def main():
    MW_val = MW_calculation("/home/erackleff/NLPScholar/MW_BERT_RESULTS_byROI.tsv")
    print(MW_val)
main()