# Sentiment Analysis with Streamlit and Hugging Face Transformers

This project is a **Sentiment Analysis** web application built using **Streamlit** and **Hugging Face Transformers**. It leverages the pre-trained **RoBERTa model** from Hugging Face for classifying text into three sentiment categories: **Positive**, **Neutral**, and **Negative**.

---

## 🚀 Features

- **Real-time Sentiment Analysis**: Enter any text, and the app predicts the sentiment and its confidence score.
- **Powered by Hugging Face**: Uses the `cardiffnlp/twitter-roberta-base-sentiment` pre-trained model for high accuracy.
- **Interactive UI**: Simple and user-friendly interface created with Streamlit.

---

## 📦 Requirements

Before running the application, ensure you have the following installed:

- Python 3.8 or later
- Required Python libraries:
  - `torch`
  - `transformers`
  - `streamlit`

---

## 🛠 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
2. **Install dependencies**:
   ```bash
   pip install torch transformers streamlit
3. **Run the Streamlit application**:
    ```bash
    streamlit run app.py  
4. **Access the app: Open your web browser and navigate to**:
    ```bash
   http://localhost:8501
5. **Acess the streamlit deployed project through [here](https://statementsentimentanalysis.streamlit.app/)**



### 🖥️ Code Overview
##### Main Libraries Used:

- Streamlit: For building the web interface.
- torch: For running the PyTorch-based RoBERTa model.
- transformers: For loading the pre-trained model and tokenizer from Hugging Face.
##### Key Functions:
- predict_sentiment(text): Takes user input and predicts its sentiment. Returns the sentiment label and confidence score.
- Streamlit Interface: Collects user input via a text area. Displays the predicted sentiment and confidence score dynamically.

🤝 Contributing
Contributions are welcome! If you find any issues or want to enhance the app, feel free to open an issue or submit a pull request.

🛡️ License
This project is licensed under the MIT License. See the LICENSE file for details.

