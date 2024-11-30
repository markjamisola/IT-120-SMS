from django.shortcuts import render
from twilio.rest import Client

def welcome_page(request):
    return render(request, 'dashboard/welcome.html') 

def send_sms(request):
    if request.method == "POST":
        salutation = request.POST.get("salutation")  # Get salutation (greeting) from form
        recipient_name = request.POST.get("recipient_name")  # Get recipient name from form
        phone_number = request.POST.get("phone_number")  # Get phone number
        message_body = request.POST.get("message_body")  # Get message body

        # Construct the full message with salutation and name
        full_message = f"{salutation}, {recipient_name}. {message_body}"

        # Twilio credentials
        account_sid = 'AC8ce7ccad83244fdf629c36e47fe8d29e'
        auth_token = '731534ef44f9428fd893233279a3f35b'
        client = Client(account_sid, auth_token)

        try:
            # Send SMS using Twilio
            message = client.messages.create(
                body=full_message,
                from_='+17753733918',
                to=phone_number
            )
            # Redirect to success page with context
            return render(request, 'dashboard/success.html', {
                'phone_number': phone_number,
                'message_sid': message.sid,
                'recipient_name': recipient_name,
                'salutation': salutation,
                'message_body': message_body,
            })
        except Exception as e:
            # Handle errors and display them on the SMS form page
            return render(request, 'dashboard/sms.html', {
                'error': str(e),
                'salutation': salutation,
                'recipient_name': recipient_name,
                'phone_number': phone_number,
                'message_body': message_body,
            })

    return render(request, 'dashboard/sms.html')
