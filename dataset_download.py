import os
import datasets
import sys

# ✅ Disable TorchCodec (forces use of SoundFile/Librosa)
datasets.config.USE_TORCHCODEC = False

sys.modules["torchcodec"] = None


OUT = "./asr_data"
os.makedirs(OUT, exist_ok=True)
from datasets import load_dataset, Audio
print("📥 Downloading LibriSpeech datasets (this may take a while)...")

# ------------------------------
# 1. Train (clean 100)
# ------------------------------
print("\nDownloading train.clean.100 ...")
train = load_dataset(
    "nguyenvulebinh/libris_clean_100",
    split="train.clean.100",
    cache_dir=OUT,
    streaming=False
)
train = train.cast_column("audio", Audio(decode=True))
_ = train[0]  # trigger extraction

# ------------------------------
# 2. Validation (dev-clean)
# ------------------------------
print("\nDownloading dev-clean ...")
dev_clean = load_dataset(
    "librispeech_asr",
    "clean",
    split="validation",
    cache_dir=OUT,
    streaming=False
)
dev_clean = dev_clean.cast_column("audio", Audio(decode=True))
_ = dev_clean[0]

# ------------------------------
# 3. Validation (dev-other)
# ------------------------------
print("\nDownloading dev-other ...")
dev_other = load_dataset(
    "librispeech_asr",
    "other",
    split="validation",
    cache_dir=OUT,
    streaming=False
)
dev_other = dev_other.cast_column("audio", Audio(decode=True))
_ = dev_other[0]

# ------------------------------
print("\n✅ Done. Data cached at:", OUT)
