import json
import random
from fpdf import FPDF   # install fpdf using pip install fpdf


def load_wishes_from_json(filename):
    # Load wishes from a JSON file
    try:
        with open(filename, 'r') as file:
            wishes = json.load(file)
        return wishes
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(
            f"Error: Failed to load wishes from '{filename}'. Invalid JSON format.")
    return []


def save_sent_wish(wish, filename):
    # Save the sent wish to a text file
    try:
        with open(filename, 'a') as file:
            file.write(wish + "\n")
        print("Sent wish has been saved.")
    except IOError:
        print(f"Error: Failed to save sent wish to '{filename}'.")


def generate_personalized_wish(name, wish):
    # Generate a personalized wish by replacing "{name}" with the actual name
    return wish.replace("{name}", name)


def save_output(output, filename):
    # Save the entire output to a text file
    try:
        with open(filename, 'w') as file:
            file.write(output)
        print(f"Output has been saved to '{filename}'.")
    except IOError:
        print(f"Error: Failed to save output to '{filename}'.")


def convert_txt_to_pdf(txt_file, pdf_file):
    # Convert a text file to a PDF file
    pdf = FPDF()
    pdf.add_page()

    with open(txt_file) as file:
        text = file.read()

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text)
    print("Converted to PDF successfully")
    pdf.output(pdf_file)


def wishBirthday(name,
                 yourName,
                 age,
                 save_sent_wishes=True,
                 save_output_file=True,
                 convert_to_pdf=True):
    # Load wishes from a JSON file
    wishes = load_wishes_from_json('wishes.json')

    if wishes:
        print(f"\nDear {name},")
        print('')
        print("Hope you're having a good day!")
        selected_wish = random.choice(wishes)
        personalized_wish = generate_personalized_wish(name, selected_wish)
        print(personalized_wish)
        print(
            f"Wishing you a wonderful year and a great time turning {age} years young.")
        print('')
        print("Best regards,")
        print(yourName)
        print('')

        if save_sent_wishes:
            # Save the sent wish to a text file
            save_sent_wish(personalized_wish, "sent_wishes.txt")

        output = f"Dear {name},\n\n"
        output += "Hope you're having a good day!\n"
        output += personalized_wish + "\n"
        output += f"Wishing you a wonderful year and a great time turning {age} years young.\n\n"
        output += "Best regards,\n"
        output += yourName + "\n"

        if save_output_file:
            # Save the entire output to a text file
            save_output(output, "birthday_output.txt")

        if convert_to_pdf:
            # Convert the output text file to a PDF file
            convert_txt_to_pdf("birthday_output.txt", "birthday_output.pdf")
    else:
        print("Error: No wishes found.")


def setup():
    # Gather input from the user
    while True:
        nameInput = input("Hey there! What's your card's receiver's name? ")
        if not nameInput:
            print("Error: Name cannot be empty.")
        elif any(char.isdigit() for char in nameInput):
            print("Error: Name cannot contain numbers.")
        else:
            break

    while True:
        yourNameInput = input("What's your name? ")
        if not yourNameInput:
            print("Error: Your name cannot be empty.")
        elif any(char.isdigit() for char in yourNameInput):
            print("Error: Name cannot contain numbers.")
        else:
            break

    while True:
        ageInput = input("How old is this person turning? ")
        if not ageInput:
            print("Error: Age cannot be empty.")
        elif not ageInput.isdigit():
            print("Error: Invalid age. Please enter a valid number.")
        else:
            ageInput = int(ageInput)
            break

    while True:
        saveSentInput = input("Save sent wishes? (Y/N): ").lower()
        if saveSentInput == "y":
            save_sent_wishes = True
            break
        elif saveSentInput == "n":
            save_sent_wishes = False
            break
        else:
            print("Error: Invalid input. Please enter 'Y' or 'N'.")

    while True:
        saveOutputInput = input("Save output to file? (Y/N): ").lower()
        if saveOutputInput == "y":
            save_output_file = True
            break
        elif saveOutputInput == "n":
            save_output_file = False
            break
        else:
            print("Error: Invalid input. Please enter 'Y' or 'N'.")

    while True:
        convertToPdfInput = input(
            "Convert output file to PDF? (Y/N): ").lower()
        if convertToPdfInput == "y":
            convert_to_pdf = True
            break
        elif convertToPdfInput == "n":
            convert_to_pdf = False
            break
        else:
            print("Error: Invalid input. Please enter 'Y' or 'N'.")

    wishBirthday(nameInput,
                 yourNameInput,
                 ageInput,
                 save_sent_wishes=save_sent_wishes,
                 save_output_file=save_output_file,
                 convert_to_pdf=convert_to_pdf)


# Start the code
setup()
