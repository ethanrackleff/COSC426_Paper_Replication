import csv
import pandas as pd

        
def merge_pred(file_names_tuple, file_name_result):
    token = []
    sentid =[]
    word = []
    wordpos = []
    model = []
    tokenizer = []
    punctuation = []
    prob = []
    surp = []
    for file_name in file_names_tuple:
        with open(file_name) as file:
            tsv_file = csv.reader(file, delimiter="\t")
            for line in tsv_file:
                if line[0] != "token":    
                    token.append(line[0])
                    sentid.append(line[1])
                    word.append(line[2])
                    wordpos.append(line[3])
                    model.append(line[4])
                    tokenizer.append(line[5])
                    punctuation.append(line[6])
                    prob.append(line[7])
                    surp.append(line[8])
    df = pd.DataFrame()
    df['token'] = token
    df['sentid'] = sentid
    df['word'] = word
    df['wordpos'] = wordpos
    df['model'] = model
    df['tokenizer'] = tokenizer
    df['punctuation'] = punctuation
    df['prob'] = prob
    df['surp'] = surp
    df.to_csv(file_name_result, sep="\t")

def main():
        file_names_BERT = ("/home/erackleff/NLPScholar/Split_EW_Pred_BERT/1_EW_pred_BERT.tsv", "/home/erackleff/NLPScholar/Split_EW_Pred_BERT/2_EW_pred_BERT.tsv", "/home/erackleff/NLPScholar/Split_EW_Pred_BERT/3_EW_pred_BERT.tsv", "/home/erackleff/NLPScholar/Split_EW_Pred_BERT/4_EW_pred_BERT.tsv")
        
        merge_pred(file_names_BERT, "EW_PREDICTIONS_BERT_MERGED.tsv")
main()

