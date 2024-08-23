from transformers import AutoTokenizer
import torch
import joblib
import warnings
warnings.filterwarnings('ignore')

model_path = 'classification_model/native_distilbert-base-cased.model'
model = joblib.load(model_path)
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-cased')

input_statements = ["Amazing experience, will visit again:)","Very bad service here."]

inputs = tokenizer(input_statements,truncation=True,
                   padding='max_length',max_length=512,return_tensors='pt')

input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']


# Running model in evaluation mode
model.eval()

with torch.no_grad():
    outputs = model(input_ids,attention_mask = attention_mask)

predictions = torch.argmax(outputs.logits,dim = -1)
print(predictions)