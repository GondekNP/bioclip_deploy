from huggingface_hub import hf_hub_download
import os
import requests

def download_species_names(target_path):
    hf_hub_download(
        repo_id = "imageomics/bioclip-demo",
        repo_type="space",
        filename = "txt_emb_species.npy",
        local_dir= target_path,
        local_dir_use_symlinks = False,
    )
    hf_hub_download(
        repo_id = "imageomics/bioclip-demo",
        repo_type="space",
        filename = "txt_emb_species.json",
        local_dir= target_path,
        local_dir_use_symlinks = False,
    )

if __name__ == '__main__':
    # In a notebook, you can set target_path directly without using __file__
    # Example: Set target_path to './data' to create a data folder in the current directory
    target_path = './data'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    download_species_names(target_path)