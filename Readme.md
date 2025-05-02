# Text-to-SQL Generator

## How to Run the App

1. **Clone this repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install dependencies**:
    First, set up your Python virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```
    Then, install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the pre-trained model**:
    Download the `t5_sql_model` from [Hugging Face Model Hub](https://huggingface.co/) or your chosen storage provider (e.g., Google Drive, S3).
    
    **Ensure the model is placed in the `t5_sql_model` directory** (inside the project directory).

4. **Run the Flask app**:
    Start the application:
    ```bash
    python app.py
    ```
    The app will be running at `http://127.0.0.1:5000/` (by default).

5. **Access the app**:
    Open your browser and visit:  
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Usage

- **Enter your question** (in English) in the input box. For example:
  - "Show all customers from Pakistan"
  - "Show all orders placed after 2020"

- **Click Submit** to get the corresponding SQL query, which you can use in your database.

---

## Notes

- The **model file is too large** for GitHub and cannot be uploaded. Please refer to the download instructions.
- If you encounter any issues with the app, check the **Troubleshooting** section below.

---

## Troubleshooting

- **Model file is not found**: Ensure the model is correctly downloaded and placed in the `t5_sql_model` directory.
- **Flask app doesn't start**: Make sure you have Flask installed, and you’re using the correct Python version.
- **Missing dependencies**: If some libraries are missing or incompatible, try:
    ```bash
    pip install --upgrade -r requirements.txt
    ```

---

## Model Details

The app uses the **T5** model, a transformer model fine-tuned to generate SQL queries based on natural language questions. It was trained on datasets like **WikiSQL** and **Spider** for the task of **Text-to-SQL Generation**.

