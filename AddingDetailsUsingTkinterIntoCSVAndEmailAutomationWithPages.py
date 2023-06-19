import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, init
import tkinter as tk
from tkinter import messagebox

init()

red = Fore.RED
magenta = Fore.MAGENTA
cyan = Fore.CYAN

print(magenta + "-" * 75)
print(Fore.LIGHTBLACK_EX + "     ...Enhancing Communication with Email Automation using Python...")
print(magenta + "-" * 75)

# For Details Filling and append inside csv file
def openDetailsForm():
    
    detailsWindow = tk.Toplevel(root)
    detailsWindow.title("Details Form")
    detailsWindow.geometry("400x500")
    detailsWindow.configure(bg="grey")          

    nameLabel = tk.Label(detailsWindow, text="Name:", font=("Arial", 12), bg="lightgray")
    nameLabel.pack(pady=10)

    nameEntry = tk.Entry(detailsWindow, font=("Arial", 12))
    nameEntry.pack(pady=5)

    departmentLabel = tk.Label(detailsWindow, text="Department:", font=("Arial", 12), bg="lightgray")
    departmentLabel.pack(pady=10)

    departmentEntry = tk.Entry(detailsWindow, font=("Arial", 12))
    departmentEntry.pack(pady=5)

    yopLabel = tk.Label(detailsWindow, text="Year of Passing:", font=("Arial", 12), bg="lightgray")
    yopLabel.pack(pady=10)

    yopEntry = tk.Entry(detailsWindow, font=("Arial", 12))
    yopEntry.pack(pady=5)

    emailLabel = tk.Label(detailsWindow, text="Email ID:", font=("Arial", 12), bg="lightgray")
    emailLabel.pack(pady=10)

    emailEntry = tk.Entry(detailsWindow, font=("Arial", 12))
    emailEntry.pack(pady=5)

    phoneLabel = tk.Label(detailsWindow, text="Phone Number:", font=("Arial", 12), bg="lightgray")
    phoneLabel.pack(pady=10)

    phoneEntry = tk.Entry(detailsWindow, font=("Arial", 12))
    phoneEntry.pack(pady=5)

    placeLabel = tk.Label(detailsWindow, text="Place:", font=("Arial", 12), bg="lightgray")
    placeLabel.pack(pady=10)

    placeEntry = tk.Entry(detailsWindow, font=("Arial", 12))
    placeEntry.pack(pady=5)

    def saveDetails():
        name = nameEntry.get()
        department = departmentEntry.get()
        yop = yopEntry.get()
        email = emailEntry.get()
        phone = phoneEntry.get()
        place = placeEntry.get()

        if (
            name.strip() == ""
            or department.strip() == ""
            or yop.strip() == ""
            or email.strip() == ""
            or phone.strip() == ""
            or place.strip() == ""
        ):
            messagebox.showerror("Error"+"Please fill in all the fields.")
            return

        details = [name, department, yop, email, phone, place]

        with open("user_details.csv", "r") as f:
            fileReader = csv.reader(f)
            for row in fileReader:
                if (
                    row[0] == name
                    and row[1] == department
                    and row[2] == yop
                    and row[3] == email
                    and row[4] == phone
                    and row[5] == place
                ):
                    messagebox.showerror("Error"+"Details already exist.")
                    return

        with open("user_details.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(details)

        messagebox.showinfo("Success", "Details saved successfully.")
        detailsWindow.destroy()

    saveButton = tk.Button(
        detailsWindow,
        text="Save Details",
        command=saveDetails,
        font=("Arial", 12),
        bg="gray",
        fg="white",
    )
    saveButton.pack(pady=20)


def send_emails():
    try:
        detailsList = []
        departmentList = []
        # CSV file reading
        with open("user_details.csv", "r") as f:
            fileRead = csv.reader(f)
            next(fileRead)
            j = 0
            for i in fileRead:
                detailsList.append(i)
                departmentList.append(detailsList[j][1])

                j += 1

        recipientEmails = []
        departmentChoice = departmentVar.get().upper()

        if departmentChoice == "0":
            outputText.insert(tk.END,"..........The End..........\n")
            return

        if departmentChoice in ["IT", "CSE", "ECE", "EEE", "MECH"]:
            for i in range(len(departmentList)):
                if departmentList[i] == departmentChoice:
                    recipientEmails.append(detailsList[i])

        else:
            outputText.insert(tk.END, "Chosen department is not eligible for this course...\n")
            return

        senderEmail = "tams192498@gmail.com"
        password = "kkgupriznwukbmkl"

        # mail sharing
        for details in recipientEmails:
            message = MIMEMultipart()
            message["From"] = senderEmail
            message["To"] = details[3]
            message["Subject"] = "CodeQuest-Exciting Summer Courses for Lifelong Fun!..."
            userEmail = details[3]

            # HTML and CSS content inside mail design
            body ='''
            <html>

            <head>
                <style>
                    .bodyy {{
                        margin: auto;
                        width: 100%;
                        text-align: center;
                        background-color: rgb(191, 185, 221);
                        color: rgb(23, 24, 23)
                    }}
                    
                    table {{
                        margin: auto;
                        width: 100%;
                        text-align: center;
                    }}
                    
                    th {{
                        color: rgb(46, 44, 44);
                    }}
                    
                    #boxStyle {{
                        width: 250px;
                        height: 30px;
                        text-align: center;
                        background-color: darkgray;
                    }}
                </style>

            </head>

            <body class="bodyy">
                <br><br>
                <h1>CodeQuest</h1>
                <img src="https://tams.neocities.org/image.png">
                <br><br>
                <hr>
                <h3>Hey {name},</h3>
                <p>Our Professional Certificate Program is designed to help you become an expert in the fast paced blockchain industry.</p>
                <h3>Cources Offered</h3>
                <p>...Python Development...<br>
                ...Full-Stack Java Development...<br>
                ...Data Science and Machine Learning...<br>
                ...Front-End Development...<br>
                ...Back-End Development...
                </p>
                <hr>
                <p>...For Course details...</p>
                <button style="background-color: gray;color:black"><a href="https://tams.neocities.org/CourceDetails" style="color:black;text-decoration: none;">Click here</a></button>
                <p>...Thank you for your time...</p>
                <hr>
                <footer>
                    <p>&copy;2023 - "CodeQuest" Created by Tams...</p>
                    <p>If you don't want to recieve these emails, no problem you can inform to Tams...</p>
                </footer>
                <br><br><br>
            </body>

            </html>

            '''.format(
                name=details[0]
            )

            message.attach(MIMEText(body, "html"))
            text = message.as_string()

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(senderEmail, password)
                server.sendmail(senderEmail, userEmail, text)

            print(cyan+"Mail Sent to\t"+userEmail)
            outputText.insert(tk.END,"Mail sent to " + userEmail + "\n")

    except Exception as e:

        outputText.insert(tk.END,"Error..." + str(e) + "\n")


def exitApplication():
    result = messagebox.askquestion("Exit","Are you sure you want to exit?")
    if result == "yes":
        root.destroy()


root = tk.Tk()
root.title("Email Automation")
root.geometry("600x600")
root.configure(bg="grey")

departmentVar = tk.StringVar(root)
departmentVar.set("0")

headingLabel = tk.Label(
    root, text="Email Automation", font=("Arial", 20, "bold"), bg="lightgray"
)
headingLabel.pack(pady=20)

detailsButton = tk.Button(
    root,
    text="Enter Details",
    command=openDetailsForm,
    font=("Arial", 14),
    bg="gray",
    fg="white",
)
detailsButton.pack(pady=10)

departmentLabel = tk.Label(
    root, text="Select Department:", font=("Arial", 14), bg="lightgray"
)
departmentLabel.pack(pady=10)

departmentDropdown = tk.OptionMenu(
    root, departmentVar, "0", "IT", "CSE", "ECE", "EEE", "MECH", "CIVIL", "ROBOTICS"
)

departmentDropdown.configure(width=15)
departmentDropdown.pack(pady=5)

sendButton = tk.Button(
    root,
    text="Send Emails",
    command=send_emails,
    font=("Arial", 14),
    bg="gray",
    fg="white",
)
sendButton.pack(pady=10)

outputText = tk.Text(root, height=10, width=50)
outputText.pack(pady=20)

exitButton = tk.Button(
    root,
    text="Exit",
    command=exitApplication,
    font=("Arial", 14),
    bg="gray",
    fg="white",
)
exitButton.pack(pady=10)

root.mainloop()

print(magenta + "-" * 75)
print(Fore.LIGHTBLACK_EX + "                            ...THE END...")
print(magenta + "-" * 75)