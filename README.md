# InstaRatio 👀

Find out who isn’t following you back on Instagram! This script is functional as of August 2024.

Update: take a look at who you aren't following back either!

## Set Up

1. **Download Your Instagram Data:**
   - Go to Instagram.
   - Navigate to **Settings** > **Your Activity** > **Download Your Information**.
   - Download your following and followers information as JSON files.

2. **Prepare Your Files:**
   - Place the downloaded files (`following.json` and `followers.json`) in the same directory as `compare.py`.

3. **Set Up Python:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

4. **Modify File Paths (if necessary):**
   - Open `compare.py` and ensure the paths to `following.json` and `followers.json` are correctly set according to their location.

## Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing `compare.py`:

   ```bash
   cd /path/to/your/directory
   
3. Run the script:

   ```bash
   python compare.py

4. The script will output a list of accounts who are not following you back.

## License
This project is licensed under the MIT License.
