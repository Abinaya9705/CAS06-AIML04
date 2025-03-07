import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
import pandas as pd

df = pd.read_csv("jigsaw_toxicity.csv")
df = df[['comment_text', 'toxicity', 'severe_toxicity', 'obscene', 'identity_attack', 'insult', 'threat']]

def label_comment(row):
    return 1 if row.toxicity > 0.5 or row.severe_toxicity > 0.5 or row.obscene > 0.5 \
              or row.identity_attack > 0.5 or row.insult > 0.5 or row.threat > 0.5 else 0

df['label'] = df.apply(label_comment, axis=1)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

class ToxicDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels
    
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        encoding = tokenizer(self.texts[idx], truncation=True, padding='max_length', max_length=128, return_tensors='pt')
        return {**encoding, 'labels': torch.tensor(self.labels[idx], dtype=torch.long)}

dataset = ToxicDataset(df['comment_text'].tolist(), df['label'].tolist())
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = AdamW(model.parameters(), lr=2e-5)

epochs = 3
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in dataloader:
        optimizer.zero_grad()
        input_ids, attention_mask, labels = batch['input_ids'].squeeze(1).to(device), batch['attention_mask'].to(device), batch['labels'].to(device)
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss/len(dataloader)}")

model.save_pretrained("unitary/unbiased-toxic-roberta")
tokenizer.save_pretrained("unitary/unbiased-toxic-roberta")
