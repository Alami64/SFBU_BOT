from dataprocess import load_default_resources

### Note, please follow the steps to run this and to generate the new embedding vector store ###
### Since the default loader script has something incompatible with the newest open ai version so we need to change the open ai version first, and change it back, only to run this script ###

# Step1: In terminal, run "pip install pip install openai==0.28"
# Step2: In terminal, run "python standalone_load_resources.py"
# The program will run and generate the new vectordb, before you run the app, do step3 first
# Step3: In terminal, run "pip install pip install openai==1.3.7" (or just pip install openai to get the latest version)
# Test the app, if the result is not satisfied, do it from Step1 again


def main():
    load_default_resources(load_from_local_stored_files=False)


if __name__ == "__main__":
    main()
