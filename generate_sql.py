from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load saved model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5_sql_model")
tokenizer = T5Tokenizer.from_pretrained("t5_sql_model")

def generate_sql(question):
    prompt = f"translate English to SQL: {question}"
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=128)
    outputs = model.generate(inputs["input_ids"])
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
