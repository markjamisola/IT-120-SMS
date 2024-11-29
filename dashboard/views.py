from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client

def send_sms(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        message_body = request.POST.get("message_body")

        
        account_sid = 'AC8ce7ccad83244fdf629c36e47fe8d29e'
        auth_token = '8052039e6296a00d2da0ad90088a24b2'
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=message_body,
                from_='+17753733918',
                to=phone_number
            )
            return HttpResponse(f"SMS sent successfully! Message SID: {message.sid}")
        except Exception as e:
            return HttpResponse(f"Failed to send SMS. Error: {e}")

    return render(request, 'dashboard/sms.html')
