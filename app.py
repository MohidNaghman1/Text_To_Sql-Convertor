from flask import Flask, render_template, request
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = Flask(__name__)

# Load model & tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5_sql_model")
tokenizer = T5Tokenizer.from_pretrained("t5_sql_model")

@app.route("/", methods=["GET", "POST"])
def index():
    question = ""
    sql_query = ""

    if request.method == "POST":
        question = request.form["question"]
        input_text = "translate English to SQL: " + question

        input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=128)
        output_ids = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
        sql_query = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return render_template("index.html", sql_query=sql_query, question=question)


if __name__ == "__main__":
    app.run(debug=True)
