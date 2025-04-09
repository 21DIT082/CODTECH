import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from fpdf import FPDF
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

FACES_DIR = "faces"
if not os.path.exists(FACES_DIR):
    os.makedirs(FACES_DIR)

ATTENDANCE_FILE = "attendance.csv"

EMAIL_SENDER = "21DIT082@charusat.edu.in"
EMAIL_PASSWORD = "21dit082"
EMAIL_RECEIVER = "shahharnish004@gmail.com"

# Load registered faces
def load_registered_faces():
    known_encodings = []
    known_names = []
    for filename in os.listdir(FACES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = face_recognition.load_image_file(os.path.join(FACES_DIR, filename))
            encoding = face_recognition.face_encodings(img)
            if encoding:
                known_encodings.append(encoding[0])
                known_names.append(os.path.splitext(filename)[0])
    return known_encodings, known_names

# Register a new face
def register_face(name):
    if not name:
        messagebox.showerror("Error", "Please enter a name before registering.")
        return

    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Registration", "Press 'S' to capture and register your face.")
    registered = False

    while True:
        ret, frame = cap.read()
        cv2.imshow("Register Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_path = os.path.join(FACES_DIR, f"{name}.jpg")
            cv2.imwrite(face_path, frame)
            messagebox.showinfo("Success", f"Face registered successfully as {name}")
            registered = True
            break
    cap.release()
    cv2.destroyAllWindows()
    if registered:
        update_dashboard()

# Mark attendance
def mark_attendance(name):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(ATTENDANCE_FILE):
        df = pd.DataFrame(columns=["Name", "Time"])
        df.to_csv(ATTENDANCE_FILE, index=False)
    df = pd.read_csv(ATTENDANCE_FILE)
    if not ((df["Name"] == name) & (df["Time"].str.startswith(now.strftime("%Y-%m-%d")))).any():
        new_record = pd.DataFrame([[name, date_time]], columns=["Name", "Time"])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_csv(ATTENDANCE_FILE, index=False)
        messagebox.showinfo("Attendance", f"Attendance marked for {name} at {date_time}")
        root.after(100, update_dashboard)
        send_email(name, date_time)
    else:
        messagebox.showinfo("Already Marked", f"{name}'s attendance is already marked today.")

# Recognize face and mark attendance
def recognize_face():
    known_encodings, known_names = load_registered_faces()
    if not known_encodings:
        messagebox.showerror("Error", "No registered faces found. Please register first.")
        return

    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Face Recognition", "Press 'Q' to exit recognition mode.")
    recognized = False

    while True:
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]
                mark_attendance(name)
                recognized = True

            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or recognized:
            break
    cap.release()
    cv2.destroyAllWindows()

# Update dashboard
def update_dashboard():
    for row in dashboard_tree.get_children():
        dashboard_tree.delete(row)
    if os.path.exists(ATTENDANCE_FILE):
        df = pd.read_csv(ATTENDANCE_FILE)
        today = datetime.now().strftime("%Y-%m-%d")
        df_today = df[df['Time'].str.startswith(today)]
        for _, row in df_today.iterrows():
            dashboard_tree.insert('', 'end', values=(row['Name'], row['Time']))

# Export today's attendance to PDF
def export_pdf():
    if not os.path.exists(ATTENDANCE_FILE):
        messagebox.showerror("Error", "No attendance records found.")
        return

    df = pd.read_csv(ATTENDANCE_FILE)
    today = datetime.now().strftime("%Y-%m-%d")
    df_today = df[df['Time'].str.startswith(today)]

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Attendance Report - {today}", ln=True, align='C')
    pdf.ln(10)
    for index, row in df_today.iterrows():
        pdf.cell(200, 10, txt=f"{row['Name']} - {row['Time']}", ln=True)

    filename = f"attendance_{today}.pdf"
    pdf.output(filename)
    messagebox.showinfo("Exported", f"Attendance PDF saved as {filename}")

# Send email notification
def send_email(name, time):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = f"Attendance Notification - {name}"
    body = f"{name} marked attendance at {time}."
    msg.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Email send error: {e}")

# GUI setup
def open_gui():
    global dashboard_tree, root
    root = tb.Window(themename="superhero")
    root.title("Face Recognition Attendance System")
    root.geometry("650x550")

    title = tb.Label(root, text="Attendance Management System", font=("Helvetica", 18, "bold"))
    title.pack(pady=10)

    frame = tb.Frame(root)
    frame.pack(pady=10)

    tb.Label(frame, text="Enter Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
    name_entry = tb.Entry(frame, font=("Helvetica", 12))
    name_entry.grid(row=0, column=1, padx=10)

    tb.Button(frame, text="Register Face", bootstyle=SUCCESS, command=lambda: register_face(name_entry.get())).grid(row=1, column=0, pady=10)
    tb.Button(frame, text="Mark Attendance", bootstyle=PRIMARY, command=recognize_face).grid(row=1, column=1, pady=10)

    dashboard_label = tb.Label(root, text="Today's Attendance", font=("Helvetica", 14, "bold"))
    dashboard_label.pack(pady=10)

    dashboard_tree = ttk.Treeview(root, columns=("Name", "Time"), show='headings', height=10)
    dashboard_tree.heading("Name", text="Name")
    dashboard_tree.heading("Time", text="Time")
    dashboard_tree.pack(pady=5, fill='x', padx=20)

    tb.Button(root, text="Export to PDF", bootstyle=INFO, command=export_pdf).pack(pady=10)

    update_dashboard()
    root.mainloop()

if __name__ == "__main__":
    open_gui()
