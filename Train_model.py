from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from prepare_data import load_and_prepare

# Load and reduce dataset to 5,000 samples for faster training
full_dataset = load_and_prepare("wikisqlSpider.csv")
small_dataset = full_dataset.shuffle(seed=42).select(range(5000))
dataset = small_dataset.train_test_split(test_size=0.1)

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Tokenization function
def preprocess(example):
    input_enc = tokenizer(example['input'], padding="max_length", truncation=True, max_length=128)
    target_enc = tokenizer(example['output'], padding="max_length", truncation=True, max_length=128)
    input_enc['labels'] = target_enc['input_ids']
    return input_enc

# Apply tokenization
tokenized = dataset.map(preprocess, batched=True)

# Define training arguments
args = TrainingArguments(
    output_dir="./t5_sql_model",
    evaluation_strategy="epoch",
    learning_rate=3e-4,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=1,
    weight_decay=0.01,
    save_strategy="epoch",
    save_total_limit=2,  # Keep only latest 2 checkpoints
)

# Set up Trainer
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized['train'],
    eval_dataset=tokenized['test']
)

# Train the model
trainer.train()

# Save final model and tokenizer
model.save_pretrained("t5_sql_model")
tokenizer.save_pretrained("t5_sql_model")
