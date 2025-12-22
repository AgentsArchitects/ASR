import os
import json
import soundfile as sf
from tqdm import tqdm
from datasets import load_dataset

# --- Configuration ---
# Please change all these Paths as per your
CACHE_DIR = r"D:/Softgetix/ASR_dataset/asr_data"
BASE_AUDIO = r"D:/Softgetix/ASR_dataset/asr_data/decoded_audio"
OUTPUT_DIR = r"D:/Softgetix/ASR_dataset/asr_data/manifests"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_manifest(dataset_name, subset, split, audio_dir, manifest_path, cache_dir, prefix):
    print(f"\n📄 Creating manifest for {dataset_name} [{split}]")
    
    # Load dataset from Hugging Face (for transcripts)
    dataset = load_dataset(dataset_name, subset, split=split, cache_dir=cache_dir)
    audio_files = sorted([f for f in os.listdir(audio_dir) if f.endswith(".flac")])

    if len(audio_files) != len(dataset):
        print(f"⚠️ Warning: Mismatch between audio files ({len(audio_files)}) and dataset entries ({len(dataset)})")

    entries = []

    for i, sample in enumerate(tqdm(dataset, desc=f"Building {prefix} manifest")):
        if i >= len(audio_files):
            break

        # Get transcript
        text = sample.get("text", "").upper().strip()
        text = text.translate(str.maketrans('', '', '.,?!\'"'))

        # Match sequential audio file
        audio_path = os.path.join(audio_dir, audio_files[i])

        try:
            with sf.SoundFile(audio_path) as snd:
                duration = len(snd) / snd.samplerate
        except Exception as e:
            print(f"⚠️ Skipping {audio_path}: {e}")
            continue

        if duration > 0.1 and len(text) > 0:
            entries.append({
                "audio_filepath": audio_path.replace("\\", "/"),
                "duration": duration,
                "text": text
            })

    # Write manifest
    with open(manifest_path, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry) + "\n")

    print(f"✅ Manifest created: {manifest_path}")
    print(f"   ➜ Total entries: {len(entries)}")


# --- Run for all splits ---
create_manifest(
    "nguyenvulebinh/libris_clean_100", None, "train.clean.100",
    os.path.join(BASE_AUDIO, "train"),
    os.path.join(OUTPUT_DIR, "train_manifest.json"),
    CACHE_DIR, prefix="train"
)

create_manifest(
    "librispeech_asr", "clean", "validation",
    os.path.join(BASE_AUDIO, "dev_clean"),
    os.path.join(OUTPUT_DIR, "dev_clean_manifest.json"),
    CACHE_DIR, prefix="dev_clean"
)

create_manifest(
    "librispeech_asr", "other", "validation",
    os.path.join(BASE_AUDIO, "dev_other"),
    os.path.join(OUTPUT_DIR, "dev_other_manifest.json"),
    CACHE_DIR, prefix="dev_other"
)




