# ASR Training & Evaluation Repository

This repository contains scripts and notebooks required to train, fine-tune, and evaluate an Automatic Speech Recognition (ASR) model using prepared audio data and manifest files.
The repository is structured to keep code separate from large datasets and model artifacts, which are shared via external links.

<br>

## Repository Structure

```
ASR/
│
├── 1_Training_Script.ipynb
├── 2_Finetune_Script.ipynb
├── Evaluation.ipynb
│
├── dataset_download.py
├── extract_audio_files.py
├── create_manifest.py
├── manifest_path_change.py
│
└── README.md
```

<br>

## File Descriptions

### Notebooks
1. 1_Training_Script.ipynb

 - Used for training the ASR model from scratch

2. 2_Finetune_Script.ipynb

 - Used for fine-tuning a pretrained / previously trained model

 - Loads model weights from an existing checkpoint

 - Typically used to improve performance on specific datasets (e.g., dev_other)

3. Evaluation.ipynb

 - Used for model evaluation

 - Computes metrics such as WER (Word Error Rate)


### Python Scripts

1. dataset_download.py

 - Downloads the raw dataset (e.g., LibriSpeech)

 - Handles dataset extraction and directory setup

2. extract_audio_files.py

 - Extracts and prepares decoded audio files
 - Ensures audio format, sample rate, and structure are consistent

3. create_manifest.py

 - Generates manifest JSON files required for training and evaluation

Each entry includes:
 - audio file path
 - transcript
 - duration

4. manifest_path_change.py

 - Utility script to update audio paths inside manifest files
 - Useful when moving data across machines or storage locations

<br>

## External Resources (Provided Separately)

Due to size constraints, the following resources are not stored in this repository and are shared via external links:

- **Manifest Files**
  - train_clean.json
  - dev_clean.json
  - dev_other.json

- **Decoded Audio Files**
  - Preprocessed audio used for training and evaluation

- **Model Artifacts**
  - Trained model
  - Tokenizer
  - Checkpoints

## Link to these resources :
```
- Manifest files: <LINK>
- Decoded audio: <LINK>
- Model & tokenizer: <LINK>
- Checkpoints: <LINK>

```

