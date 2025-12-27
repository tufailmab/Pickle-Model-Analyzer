import pickle
import warnings
import os

# Optional: ignore version mismatch warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Get all .pkcls files in the current directory
pkcls_files = [f for f in os.listdir('.') if f.endswith('.pkcls')]

if not pkcls_files:
    print("No .pkcls files found in the current directory.")
    exit()

output_filename = "pkcls_summary.txt"
with open(output_filename, "w", encoding="utf-8") as outfile:

    for file in pkcls_files:
        outfile.write(f"{'='*80}\n")
        outfile.write(f"Processing file: {file}\n")
        outfile.write(f"{'='*80}\n\n")
        
        print(f"Starting to load the file: {file}")

        # Step 1: Load the Orange SklModelRegression object
        try:
            with open(file, "rb") as f:
                obj = pickle.load(f)
            print("File loaded successfully.\n")
        except Exception as e:
            print(f"Error while loading the file {file}: {e}")
            outfile.write(f"Error while loading the file: {e}\n\n")
            continue

        # Step 2: Check object type
        obj_type = type(obj)
        print("Type of loaded object:", obj_type)
        outfile.write(f"Type of loaded object: {obj_type}\n\n")

        # Step 3: Print Orange wrapper info
        outfile.write("Orange wrapper attributes:\n")
        outfile.write(f"Model name: {getattr(obj, 'name', 'N/A')}\n")
        outfile.write(f"Orange wrapper params: {getattr(obj, 'params', 'N/A')}\n")
        outfile.write(f"Original training data: {getattr(obj, 'original_data', 'N/A')}\n\n")

        # Step 4: Access underlying scikit-learn model
        skl_model = getattr(obj, "skl_model", None)
        outfile.write("Underlying scikit-learn model:\n")
        outfile.write(f"{skl_model}\n\n")

        # Step 5: Print hyperparameters
        if skl_model is not None:
            outfile.write("Model hyperparameters:\n")
            outfile.write(f"{skl_model.get_params()}\n\n")

            # Step 6: Print feature importances
            if hasattr(skl_model, "feature_importances_"):
                outfile.write("Feature importances:\n")
                outfile.write(f"{skl_model.feature_importances_}\n\n")

            # Step 7: Number of estimators (trees)
            if hasattr(skl_model, "estimators_"):
                outfile.write("Number of estimators (trees):\n")
                outfile.write(f"{len(skl_model.estimators_)}\n\n")
        
        outfile.write("\n\n")

print(f"All pkcls file summaries saved to {output_filename}")
