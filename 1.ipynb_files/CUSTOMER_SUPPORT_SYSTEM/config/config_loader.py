import yaml

def load_config(config_path: str = r"C:\MY_Folder\MY_Courses\1.GEN_AI_LIVE_Classes\ipynb_files\CUSTOMER_SUPPORT_SYSTEM\config\config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config
