# 🧠 AlzheimerNER

**AlzheimerNER** is a specialized **Natural Language Processing (NLP)** and **Machine Learning** project focused on analyzing clinical trial eligibility criteria for **Alzheimer’s disease**.

---

### 🔄 How It Works

Messy & unstructured medical text from clinical trials in JSON format <br>
🔽 <br>
NLP and machine learning pick out the important information <br>
🔽 <br>
Key medical terms are mapped to the respective categories <br>
🔽 <br>
All information is turned into easy-to-read and structured data <br>
🔽 <br>
Doctors and researchers can quickly spot which patients qualify

---
## 🎯 Why It Matters?

This project empowers clinical researchers to:

- 📑 **Extract structured data** from free-text eligibility criteria  
- 🧠 **Identify patterns** across clinical trials  
- 👥 **Improves patient screening** in real-world clinic settings 
- 📊 **Enable deeper analysis** in Alzheimer’s research
- ⏱️ **Save time and resources** while **boosting efficiency** for researchers and clinicians

---

## 🚀 Key Features

- **Custom Named Entity Recognition (NER)** model built on **BERT (Bidirectional Encoder Representations from Transformers)**
- **Fine-tuned for clinical and biomedical contexts**
- Utilizes **Transformers** and **BERT** packages
- Enhanced with a **domain-specific dictionary** to capture specialized medical terms

---

## 🧬 What Is Extracted

The model identifies and classifies the following key entities:

| Category                      | Description                                                   |
|------------------------------|---------------------------------------------------------------|
| 👤 **Patient Demographics**     | Age, gender, and other relevant participant information        |
| 🩺 **Diagnosis**                | Alzheimer’s disease and related diagnostic terms               |
| 🧠 **Cognitive Assessment**     | Results or criteria related to cognitive function evaluation   |
| 💊 **Treatment & Medication**   | Prescribed drugs, interventions, and therapeutic approaches    |
| 📋 **Medical History**          | Comorbidities and prior clinical conditions                    |
| ⚕️ **Clinical Safety & Stability** | Parameters ensuring medical fitness or excluding instability |
| 🧪 **Biomarkers & Diagnostic Criteria** | Lab results, imaging, and diagnostic markers used in eligibility |


---



---

## 🛠️ Built With
- 🐍 **Python** including:
  - [`transformers`](https://huggingface.co/docs/transformers/index) (by Hugging Face)
  - `bert-base-uncased` (fine-tuned on clinical data)  
  - `json`
  - `re` 
  - `pathlib.Path` 
  - `pandas`  
  - `scikit-learn`:  
    - `train_test_split`  
    - `classification_report`  
    - `precision_score`, `recall_score`, `f1_score`
 - 📖 Custom **domain-specific medical dictionaries**  

---
<details>
<summary>✨ <strong>Personal Note</strong></summary>

This was my **first Machine Learning and NLP project**, developed from scratch with no prior coding experience.  
I learned and picked up everything I needed through online courses, tutorials, and the support of AI tools.

What began as a personal challenge has grown into something I’m proud of.  
This project stands as proof of my adaptability, determination, and ability to start from zero and keep moving forward.

</details>

---
