from datasets import load_dataset, Audio
import os, soundfile as sf, shutil

# --- Paths ---
CACHE_DIR = r"D:\Softgetix\ASR_dataset\asr_data"
OUTPUT_DIR = os.path.join(CACHE_DIR, "decoded_audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Helper: Extract dataset ---
def extract_dataset(name, subset=None, split="train.clean.100", tag="train", batch_size=200):
    print(f"\n🔄 Extracting {name} ({subset or ''}) [{split}]")
    ds = load_dataset(name, subset, split=split, cache_dir=CACHE_DIR, streaming=False)
    ds = ds.cast_column("audio", Audio())

    dataset_dir = os.path.join(OUTPUT_DIR, tag)
    os.makedirs(dataset_dir, exist_ok=True)

    for i in range(len(ds)):
        try:
            sample = ds[i]
            audio = sample["audio"]
            text = sample["text"]
            fname = f"{tag}_{i:05d}.flac"
            dest = os.path.join(dataset_dir, fname)

            # Save the FLAC permanently
            sf.write(dest, audio["array"], audio["sampling_rate"])
            if (i + 1) % batch_size == 0:
                print(f"✅ Saved {i + 1} samples")

        except Exception as e:
            print(f"⚠️ Skipping {i}: {e}")

    print(f"🎯 Completed extraction for {tag}: {len(ds)} files saved at {dataset_dir}\n")


# --- Run extraction for all sets ---
extract_dataset("nguyenvulebinh/libris_clean_100", split="train.clean.100", tag="train")
extract_dataset("librispeech_asr", subset="clean", split="validation", tag="dev_clean")
extract_dataset("librispeech_asr", subset="other", split="validation", tag="dev_other")
