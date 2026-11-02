import os
import subprocess

def prepare_dataset():
    # 1. Download dan Ekstrak Dataset Kaggle
    print("Mengunduh dataset dari Kaggle...")
    # Pastikan API Kaggle (kaggle.json) sudah terkonfigurasi di lokal/laptop kamu
    subprocess.run(["kaggle", "datasets", "download", "-d", "uttejkumarkandagatla/fall-detection-dataset"])
    
    print("Mengekstrak dataset...")
    subprocess.run(["unzip", "-q", "fall-detection-dataset.zip", "-d", "fall_dataset/"])

def create_yaml():
    # 2. Mencari folder train dan val/valid secara dinamis
    dataset_path = "fall_dataset"
    train_dir = ""
    val_dir = ""

    for root, dirs, files in os.walk(dataset_path):
        if 'train' in root and ('images' in root or len(files) > 0 and files[0].endswith(('.jpg', '.png'))):
            train_dir = os.path.abspath(root)
        elif ('val' in root or 'valid' in root) and ('images' in root or len(files) > 0 and files[0].endswith(('.jpg', '.png'))):
            val_dir = os.path.abspath(root)

    print(f"Ketemu! Jalur Train: {train_dir}")
    print(f"Ketemu! Jalur Val  : {val_dir}")

    # 3. Membuat file data.yaml dengan jalur absolut (full path)
    yaml_content = f"""
train: {train_dir}
val: {val_dir}

nc: 3
names: ['Fall Detected', 'Walking', 'Sitting']
"""
    with open('data.yaml', 'w') as f:
        f.write(yaml_content)
    print("File data.yaml berhasil dibuat secara otomatis!")

if __name__ == "__main__":
    prepare_dataset()
    create_yaml()