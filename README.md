![Python](https://img.shields.io/badge/Python-3.x-blue)

![License](https://img.shields.io/badge/License-MIT-green)

![Status](https://img.shields.io/badge/Project-Completed-brightgreen)


# Bulk Email Sender

## Installation

```bash
pip install -r requirements.txt
```

## Setup

1. Copy `.env.example` to `.env`

2. Edit `.env`

```env
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
```

3. Run

```bash
python main.py
```

# 📧 Bulk Email Sender

A Python-based Bulk Email Sender that reads contacts from a CSV file, personalizes email templates, and sends emails securely using Gmail SMTP.

## ✨ Features

- 📄 Read contacts from a CSV file
- 📨 Send personalized emails
- 🔐 Secure Gmail SMTP authentication
- 🔒 Store credentials using `.env`
- 📂 Modular Python architecture
- 📋 Easy-to-edit email templates
- ⚡ Bulk email sending

## 📂 Project Structure

```text
Email_Sender/
│
├── config.py              # Load environment variables
├── csv_reader.py          # Read contacts from CSV
├── email_sender.py        # Gmail SMTP functions
├── message_builder.py     # Personalize templates
├── template_loader.py     # Load template.txt
├── main.py                # Main application
├── Name_Email.csv         # Contact list
├── template.txt           # Email template
├── .env.example           # Environment variable example
├── .gitignore
└── README.md
```
## 🛠 Technologies Used

- Python 3
- Gmail SMTP
- python-dotenv
- CSV Module
- EmailMessage

- ## 📸 Screenshots

### Terminal Output

![Terminal Output](image/terminal.png)

### Email Received

![Email Received](image/gmail.png)

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.
