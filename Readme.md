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
Manifest files, Decoded audio, Model & tokenizer, Checkpoints: https://drive.google.com/drive/folders/1NE7afN12yfLoW94lh8H7QZ-XLk0k5vt8?usp=sharing

Decoded Audio files : https://drive.google.com/drive/folders/1NE7afN12yfLoW94lh8H7QZ-XLk0k5vt8?usp=sharing

NOTE - You can download audio files from yourself using the code
```
<br>

## Model Performance (current)

**Model Type**
- **Model Type:**
- **CTC-based ASR model (Connectionist Temporal Classification)**

---

### Training Summary

The model was trained in two stages:

**Stage 1 – Initial Training**
- Trained from scratch for **57 epochs**
- **Early stopping** was applied to prevent overfitting
- Initial performance achieved:
  - **dev_other**: ~**8.0% WER**

**Stage 2 – Fine-Tuning**
- Fine-tuned from the best-performing checkpoint
- **Reduced learning rate** for stable adaptation
- Applied **stronger SpecAugment** to improve robustness
- Fine-tuning was run for **19 epochs**
- Final performance achieved:
  - **dev_other**: **6.13% WER**
  - **dev_clean**: **3.46% WER**

---

**Evaluation Results:**
- **dev_other**: **6.13% WER**
- **dev_clean**: **3.46% WER**


## Fine Tuning

  - Fine-tuned the pretrained CTC model instead of training from scratch
  - Applied **stronger SpecAugment** to improve robustness to noise and variability (SpecAugment intentionally hides small parts of the speech signal during training so the model learns to transcribe accurately even when audio is noisy or incomplete.)
  - Used conservative learning rate settings to avoid overfitting

## NEXT STEPS

The current model has achieved strong performance using a CTC-based architecture. Further improvements can be made through the following next steps:

### 1. Add Language Model–Based Decoding
- Integrate an external Language Model (e.g., n-gram / neural LM) with CTC decoding
- Use beam search with language model scoring
- Expected to significantly reduce errors related to grammar, word selection, and homophones  
- This is the **highest-impact next step**, especially for `dev_other`

### 2. Transition to Transducer (RNN-T) Model
- Move from CTC to a Transducer-based architecture
- Enables joint acoustic and language modeling
- Better suited for long-form and streaming speech
- Considered a **next training phase**, requiring additional compute and tuning
