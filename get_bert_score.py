from bert_score import score

def get_bert_score(hypotheses, references):
    model_type = "microsoft/deberta-v2-xlarge-mnli" ## currently the best model
    # model_type = "roberta-large"
    P, R, F1 = score(cands=hypotheses, refs=references, lang='en', verbose=False, model_type=model_type)
    
    return P, R, F1

hyp = "I like apples"
ref = "Donald trump is the worst president ever"

p, r, f1 = get_bert_score([hyp], [ref])

print(f"Precision: {p}, Recall: {r}, F1: {f1}")
