
from datasets import load_dataset
import json

# Load the dataset
dataset = load_dataset("princeton-nlp/SWE-bench", split="dev")
print(dataset)


# # Iterate through each split in the dataset
# for split in dataset.keys():
#     # Convert the dataset to a list of dictionaries
#     data_as_dicts = dataset[split].to_dict()

#     # Simplify the structure to a list of samples
#     simplified_data = [dict(zip(data_as_dicts.keys(), values)) for values in zip(*data_as_dicts.values())]
    
#     # Define the filename based on the split
#     filename = f"data/data-{split}.json"
    
#     # Save the simplified data to a JSON file
#     with open(filename, 'w') as f:
#         json.dump(simplified_data, f, indent=4)

#     print(f"{filename} has been saved with {len(simplified_data)} samples.")
