# 🎉 Birthday WishCraft

The Birthday WishCraft is a Python script that generates personalized birthday wishes. It allows you to input the recipient's name, your name, and their age. The script then randomly selects a birthday wish from a collection of wishes and generates a personalized wish by replacing placeholders with the actual names and age.

## ✨ Features

- Generates personalized birthday wishes
- Randomly selects wishes from a collection
- Saves sent wishes to a text file
- Saves the entire output to a text file
- Converts the output text file to a PDF file

## 📋 Prerequisites

To run the Birthday WishCraft, ensure that you have the following installed:

- Python (Version 3.6 or higher)
- pip (Python package manager)

Additionally, install the `fpdf` package by running the following command:

```
pip install fpdf
```

## 🚀 Usage

1. Clone the repository to your local machine or download the source code as a ZIP file.
    
    ```bash
    git clone git@github.com:geekyharsh05/Birthday-WishCraft.git
    ```

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Run the script by executing the following command:
   ```
   python main.py
   ```

4. Follow the prompts and provide the necessary inputs:
   - Enter the recipient's name.
   - Enter your name.
   - Enter the recipient's age.

5. Choose the desired options:
   - Save sent wishes? Enter 'Y' to save the sent wishes to a text file or 'N' to skip.
   - Save output to file? Enter 'Y' to save the entire output to a text file or 'N' to skip.
   - Convert output file to PDF? Enter 'Y' to convert the output text file to a PDF file or 'N' to skip.

6. The script will generate a personalized birthday wish and display it on the console.

7. If you selected to save sent wishes, a text file named "sent_wishes.txt" will be created in the same directory, containing the sent wish.

8. If you selected to save the output to a file, a text file named "birthday_output.txt" will be created in the same directory, containing the entire output.

9. If you selected to convert the output to a PDF file, a PDF file named "birthday_output.pdf" will be created in the same directory, containing the output text in a formatted PDF document.

## 🤝 Contributing

Contributions to the Birthday WishCraft are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## 📄 License

The Birthday WishCraft is open source software licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the license terms.