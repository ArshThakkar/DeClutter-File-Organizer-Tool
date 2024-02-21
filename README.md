# DeClutter File Organizer Tool

This is a simple Python script designed to organize files within a directory into specific folders based on their file types. It helps to declutter your workspace by categorizing files such as images, documents, media, and others into separate folders for easy access and management.

## Features

- Automatically organizes files into categorized folders.
- Supports various file types including images, documents, media files, and others.
- Easy to customize and extend with additional file types or categories.

## Usage

1. Clone the repository or download the `main.py` script.
2. Place the `main.py` script in the directory you want to organize.
3. Run the script using Python 3.

   ```bash
   python main.py
   ```

4. The script will categorize files into folders based on their types.

## Supported File Types

- **Images**: `.png`, `.img`, `.jpg`, `.jpeg`
- **Documents**: `.txt`, `.docx`, `.doc`, `.pdf`, `.xlsx`, `.ppt`
- **Media**: `.mp4`, `.mp3`, `.avi`, `.flv`, `.mpeg`

## Customization

You can customize the script by modifying the following variables:

- `doc_exts`: List of document file extensions.
- `img_exts`: List of image file extensions.
- `media_exts`: List of media file extensions.

Add or remove file extensions from these lists to adjust which files are categorized into each folder.

## Note

- Ensure that you have proper permissions to modify files within the directory.
- Make sure to back up your files before running the script, especially if you're unsure about the outcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute, report issues, or suggest improvements via GitHub. Contributions are welcome!
