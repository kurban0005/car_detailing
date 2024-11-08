from django.shortcuts import render, redirect
from .models import Order
from bot import send_telegram_message
from .recaptcha import create_assessment
import os

credential_path = os.environ.get("CREDENTIAL_PATH")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def index(request):
    return render(request, 'm23_app/index.html')


def services(request):
    return render(request, 'm23_app/services.html')


def info(request):
    return render(request, 'm23_app/info.html')


def contacts(request):
    return render(request, 'm23_app/contacts.html')


def new_order(request):
    if request.method == 'POST':
        recaptcha_token = request.POST.get('g-recaptcha-response')
        try:
            response = create_assessment(
                project_id=os.environ.get("PROJECT_ID"),
                recaptcha_key=os.environ.get("RECAPTCHA_PUBLIC_KEY"),
                token=recaptcha_token,
                recaptcha_action="login"
            )
        except:
            print('reCAPTCHA не пройдена.'
                  '\nОШИБКА при выполнении create_assessment.'
                  '\nВозможно не нажали "я не робот".')
            return render(request, 'm23_app/new_order.html')

        if response and response.risk_analysis.score < 0.9:
            print('reCAPTCHA пройдена')
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            car_model = request.POST['car_model']
            question = request.POST['question']
            order = Order.objects.create(name=name.title(),
                                         phone_number=phone_number,
                                         car_model=car_model,
                                         question=question)
            order.date_add = order.date_add.strftime("%d/%m/%Y . %H:%M")
            print('Заказ создан')
            send_telegram_message(order)
            return redirect('m23_app:index')
        else:
            print('reCAPTCHA не пройдена')
            return render(request, 'm23_app/index.html')
    else:
        return render(request, 'm23_app/new_order.html')
