# Code to Update manifest paths if needed only 
import os, json

old_prefix = "D:/Softgetix/ASR_dataset/asr_data/decoded_audio"
new_prefix = "/content/drive/MyDrive/ASR_richard/audio/decoded_audio"

manifest_dir = r"D:/Softgetix/ASR_dataset/asr_data/manifests"
manifests = [
    os.path.join(manifest_dir, "train_manifest.json"),
    os.path.join(manifest_dir, "dev_clean_manifest.json"),
    os.path.join(manifest_dir, "dev_other_manifest.json"),
]

for manifest in manifests:
    new_lines = []
    with open(manifest, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            entry["audio_filepath"] = entry["audio_filepath"].replace(old_prefix, new_prefix).replace("\\", "/")
            new_lines.append(json.dumps(entry))
    with open(manifest, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

print("✅ All manifest paths updated successfully.")