from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Download the model and tokenizer
model_en = AutoModelForSequenceClassification.from_pretrained("vsak/BERT_filter_en")
tokenizer_en =AutoTokenizer.from_pretrained("vsak/BERT_filter_en")
model_gr = AutoModelForSequenceClassification.from_pretrained("vsak/BERT_filter_gr")
tokenizer_gr =AutoTokenizer.from_pretrained("vsak/BERT_filter_gr")
model_en.save_pretrained('API/models/BERT_filter_en') 
tokenizer_en.save_pretrained('API/models/Tokenizer_en') 
model_gr.save_pretrained('API/models/BERT_filter_gr') 
tokenizer_gr.save_pretrained('API/models/Tokenizer_gr') 
