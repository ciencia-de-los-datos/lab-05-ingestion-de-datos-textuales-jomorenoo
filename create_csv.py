import os
import pandas as pd


def create_dataset_csv(root_dir, output_file):
    data = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(subdir, file)
                sentiment = os.path.basename(subdir)
                with open(filepath, "r", encoding="utf-8") as f:
                    phrase = f.read().strip()
                    data.append({"phrase": phrase, "sentiment": sentiment})

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)


train_dir = r"/Users/usuario/Documents/GitHub/lab-05-ingestion-de-datos-textuales-jomorenoo/data/train"
train_output_file = "train_dataset.csv"
create_dataset_csv(train_dir, train_output_file)

test_dir = r"/Users/usuario/Documents/GitHub/lab-05-ingestion-de-datos-textuales-jomorenoo/data/test"
test_output_file = "test_dataset.csv"
create_dataset_csv(test_dir, test_output_file)
