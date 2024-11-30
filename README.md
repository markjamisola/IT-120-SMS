**IT120-SMS Application (send ease)**

**Overview**

- The IT120-SMS Application is a Django-based web application designed for sending SMS messages. The application integrates with Twilio, a cloud communications platform, to send messages from a Twilio phone number to the recipient's mobile phone number.

- This system allows users to input their phone number, select a salutation (greeting), enter the recipient's name, compose a custom message, and send it via SMS. The app ensures seamless communication between the sender and the recipient.

**Features**

- **SMS Sending:** Send custom messages via SMS to any valid phone number using Twilio. In our case, our app only has one valid number that we can send SMS to.

- **Salutation (Greeting):** Choose from predefined salutations (e.g., "Good Morning", "Hello") to personalize messages.

- **Recipient Name:** Add the recipient's name, and the system will send the message with the greeting followed by the recipient’s name.

- **Twilio Integration:** Utilizes Twilio’s API for seamless message sending.

- **User-Friendly Interface:** Simple web interface to send SMS messages with form validation.

- **Error Handling:** Handles errors and displays them to the user if any issues arise during message sending.

**Tech Stack**

- **Backend Framework:** Django 5.1.3
- **Programming Language:** Python 3.12.1
- **Twilio API:** For sending SMS messages
- **Frontend:** HTML, CSS (Bootstrap for UI styling)


**Installation Guide / Running the Application**
Follow the steps below to set up and run the IT120-SMS Application on your local machine.

git clone https://github.com/markjamisola/IT-120-SMS

After cloning you can try to run the program by typing 
python manage.py runserver on your vscode terminal.

**Configuration**

**Twilio Setup**
You need a Twilio account to send SMS messages. Follow these steps to set it up:

Go to Twilio’s website and sign up for an account if you don't already have one.
After creating an account, find your Account SID and Auth Token from the Twilio console.
You will also need a Twilio phone number to send messages. You can get one from the Twilio console.

After getting your Account SID, Auth Token, and Twilio phone number, you can change the existing Twilio Credentials located on dashboard/views.py 

- **# Twilio credentials**

- account_sid = 'your twilio sid'
- auth_token = 'your twilio token'
- from_='your twilio number',


**Send ease Pages**

- http://127.0.0.1:8000/ - Welcome Page
- http://127.0.0.1:8000/send-sms/ - Send SMS Page
- and after sending a SMS a Success Page will be shown
