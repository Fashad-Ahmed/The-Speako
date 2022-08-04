The Speako
==============================
<img src="./img.jpeg" />

## 🚀 About Project 
------------
Speech recognition, also known as automatic speech recognition (ASR), computer speech recognition, or speech-to-text, is a capability which enables a program to process human speech into a written format.

#### Features:
- This project will let the users to transcribe there `.flac` or `.wav` **audio** file.
- Translate the transcribtion into Urdu Language.
- Extract the Key point of text.

## 📂 Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------


## 📃 Transcription

### Fine-Tuning Steps:
#### Dataset:
- TIMIT:  is a corpus of phonemically and lexically transcribed speech of American English speakers of different genders and dialects.
#### Preprocessing Step:
- Removed irrelivant features from English dataset.In our dataset: `phonetic_detail` ,  `word_detail`, `dialect_region`, `sentence_type`, `speaker_id`)
- Removed expressions like  \ , \ ? \ . \ ! \ - \ ; \ : \ "
- Sampled the Audio file at 16 KHz
#### Evaluation:
- Use WER (Word Error Rate)
#### Training:
- TRANSFORMER: We use <a href="https://huggingface.co/docs/transformers/index#:~:text=to%20get%20started-,%F0%9F%A4%97%20Transformers,training%20a%20model%20from%20scratch.">Transformers</a> from huggnig face. 

- Model Use: [facebook/wav2vec2-large-960h-lv60-self](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self)
------------



## 🔤 Translation

#### Supported Language: 
URDU
- Translate the transcription into Urdu Language.
-  Model Uses: [Helsinki-NLP/opus-mt-en-ur](https://huggingface.co/Helsinki-NLP/opus-mt-en-ur)
------------

## 📌 Keywords Extraction
- Text analysis feature that automatically extracts the most used important words from a transciption. It helps summarize the content of texts and recognize the main topics discussed.
- Model Uses: [KeyBERT](https://maartengr.github.io/KeyBERT/)

------------

## 🔮 User Interface
------------

## 📋 License
------------
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the `LICENSE` file for details.


