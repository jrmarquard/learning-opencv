import requests
import os

def download_file(_src, _filename):
    """
    Downloads a file from a given source URL to the specified local filename.

    Parameters:
    _src (str): The source URL from which to download the file.
    _filename (str): The local filename to save the downloaded file.

    Returns:
    None. Prints a success message if the file is downloaded successfully,
    a failure message if the download fails, or a message indicating that the file
    already exists and was not downloaded.
    """
    if not os.path.isfile(_filename):
        response = requests.get(_src, stream=True)
        if response.status_code == 200:
            with open(_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"File '{_filename}' downloaded successfully.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    else:
        print(f"Did not download file. Already exists.")
    
