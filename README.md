# SummarizeWithPegasus

A Flask-based web application for text summarization using Google's PEGASUS model via Hugging Face Transformers.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation 🛠️

### Prerequisites
- Python 3.6+
- 4GB+ free RAM
- 2GB+ disk space for models

### Manual Installation
```bash
git clone https://github.com/rhetav/SummarizeWithPegasus.git
cd SummarizeWithPegasus
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


## Usage 🚀

### Start the application:

``` bash
python app.py
```

Access the web interface at: http://localhost:5000


### Web Interface:

* Paste text into the input box
* Click "Summarize"
* View generated summary

### API Endpoint:

``` bash
curl -X POST -H "Content-Type: application/json" \
-d '{"text":"Your input text here..."}' \
http://localhost:5000/summarize
```

## Configuration ⚙️

### Modify parameters in app.py:

``` python
# Generation parameters
model.generate(
    input_ids,
    max_length=150,          # Maximum summary length
    min_length=40,           # Minimum summary length
    num_beams=4,             # Beam search width
    early_stopping=True
)
```

## Project Structure 📂

```
SummarizeWithPegasus/
├── .github/
│   └── workflows/
│       └── .gitkeep
├── .gitignore
├── app.py
├── artifacts/
│   ├── data_ingestion/
│   │   ├── data.zip
│   │   └── samsum_dataset/
│   │       ├── samsum-test.csv
│   │       ├── samsum-train.csv
│   │       └── samsum-validation.csv
│   ├── data_transformation/
│   │   └── samsum_dataset/
│   ├── model_trainer/
│   │   ├── pegasus-samsum-model/
│   │   └── tokenizer/
├── config/
│   └── config.yaml
├── Dockerfile
├── LICENSE
├── logs/
│   └── continuos_logs.log
├── main.py
├── params.yaml
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   └── SummarizeWithPegasus/
│       ├── __init__.py
│       ├── __pycache__/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── logging/
│       ├── pipeline/
│       └── utils/
├── template.py
```

## License 📄

This project is licensed under the MIT License - see LICENSE file for details.