import os
import shutil
import logging

def delete_local_file(delete_file_path):
    try:
        files_to_delete = [os.path.join(delete_file_path, filename) for filename in os.listdir(delete_file_path)]
        for item in files_to_delete:
            if os.path.isfile(item):
                os.remove(item)
                print(f"Deleted file: {item}")
            elif os.path.isdir(item):
                shutil.rmtree(item)
                print(f"Deleted folder: {item}")
    except Exception as e:
        logging.exception(f"Error Deleting local files  : {e}")
        raise e