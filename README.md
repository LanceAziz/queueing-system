# Queueing System Project

This project is a comprehensive queue management system designed to streamline the process of serving clients. It is currently **deployed in an educational institution in Cairo, Egypt**. The system consists of three distinct portals, each serving a unique purpose in the queueing process:

## Portals

### 1. Admin Portal
- **Functionality**: Only the admin can register accounts for the teller users.
- **Security**: Authentication is enforced to ensure that only authorized personnel can manage teller accounts.

### 2. Services Portal
- **Functionality**: Clients are created in the database while waiting to be served.
- **Integration**: Includes a thermal printer to print the client's number in the form of a receipt.

<p align="center">
  <img src="https://github.com/LanceAziz/queueing-system/blob/main/Images/Image%201.png" alt="Image 1"/>
</p>

### 3. Teller Portal
- **Functionality**: Teller users authenticate themselves, and upon successful login, they access a dashboard to serve the next client.
- **Display Integration**: The current client number is displayed on a 2.3-inch 7-segment 3-digit display.

<p align="center">
  <img src="https://github.com/LanceAziz/queueing-system/blob/main/Images/Image%202.png" alt="Image 2"/>
</p>

## Technology Stack

### Frontend
- **Framework**: [Next.js](https://nextjs.org/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)

### Backend
- **Framework**: [Django](https://www.djangoproject.com/)
- **Authentication**: JWT (JSON Web Tokens) for secure authentication.

### Database
- **Database**: MySQL

## Key Features
- **Race Condition Handling**: The app is designed to handle race conditions, ensuring data integrity and consistency.
- **Hardware Integration**: 
  - 2.3-inch 7-segment 3-digit display for showing the current client number.
  - Thermal printer for printing receipts from the Services Portal.
- **AI TTS Models**: Implemented AI Text-to-Speech models to convert specific strings into Arabic voice, enhancing the user experience.
