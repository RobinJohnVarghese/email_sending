from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Email
from django.conf import settings
from .task import send_all_emails

def index(request):
    return render(request, 'index.html')


def submit_email(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_obj= Email.objects.filter(recipient=recipient).first()
        if email_obj:
            # print("!!!!!!!!!!",email_obj.recipient)
            return JsonResponse({"message": "Email is Existing", "email_id": email_obj.recipient}) 
        email_obj = Email.objects.create(recipient=recipient, subject=subject, message=message)
        return JsonResponse({"message": "Email saved successfully", "email_id": email_obj.id})

    return JsonResponse({"error": "Invalid request"}, status=400)
  

def tigger_email_task(request):
        send_all_emails.delay()  
        return JsonResponse({"message": "Email sending task triggered."})