from transformers import BertTokenizer, AutoTokenizer, BertForSequenceClassification, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# load saved models and tokenizers
device = torch.device('cpu')
model_en = BertForSequenceClassification.from_pretrained("models/BERT_filter_en").to(device)
tokenizer_en = BertTokenizer.from_pretrained('models/BERT_tokenizer') # tokenizer
# model_en.save_pretrained('BERT_filter_en') # save the model configuration and weights
model_gr = AutoModelForSequenceClassification.from_pretrained("models/BERT_filter_gr").to(device)
tokenizer_gr = AutoTokenizer.from_pretrained("models/Greek_BERT_tokenizer")
# model_gr.save_pretrained('BERT_filter_gr') # save the model configuration and weights

def model_logic(language,message):
    if language == 'en':
        # we use Bert model for english
        model = model_en
        tokenizer = tokenizer_en
    else:
        # we use greek BERT for greek
        model = model_gr
        tokenizer = tokenizer_gr
    # encoding the input text message
    encoded_text = tokenizer.encode_plus(message, add_special_tokens=True, max_length = 128, padding='max_length' , truncation=True, return_tensors = 'pt')
    input_ids = encoded_text['input_ids']
    attention_mask = encoded_text['attention_mask']
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    output = outputs.logits
    prob = F.softmax(output,dim=1) # prob is a 2x1 tensor
    prob_spam = prob[:,1].item() # probability of message being spam
    prob_spam = round(prob_spam * 100 , 1)  # round in the 3rd decimal and make it as percentage
    return prob_spam
