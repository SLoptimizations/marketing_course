from django.shortcuts import render
import uuid
from . models import UserInfo
from django.views.generic import TemplateView, CreateView, View
from . funcs.main import send_mail
from django.contrib.auth.models import User


# Create your views here.


def shein_view(request):
        return render(request, 'task_landing_pages/shain-landing-page.html')

def nespresso_view(request):
        return render(request, 'task_landing_pages/nespresso-landing-page.html')

def personal_trainer_view(request):
        return render(request, 'task_landing_pages/personal-trainer-landing-page.html')


def nespresso_thanku_link_view(request):
    if request.method == "POST":
        return render(request, 'task_landing_pages/nespresso-thanku-page.html')
    return render(request, 'task_landing_pages/nespresso-landing-page-thanku.html')

def shein_thanku_link_view(request):
    if request.method == "POST":
        return render(request, 'task_landing_pages/shain-thanku-page.html')
    return render(request, 'task_landing_pages/shain-landing-page-thanku.html')

def personal_trainer_thanku_link_view(request):
    if request.method == "POST":
        return render(request, 'task_landing_pages/personal-trainer-thanku-page.html')
    return render(request, 'task_landing_pages/personal-trainer-landing-page-thanku.html')





def register(request):

    if request.method == "POST":

            # info = user_info_form.save(commit=False)
            data = request.POST
            user = UserInfo(
                username=data['username'],
                email=data['email'],
            )
            user.url_id = str(uuid.uuid4()).split('-')[1]


            user.save()

            send_mail(to=user.email,
                      campaign_json='landing_page/funcs/email_settings.json',
                      url_id=user.url_id)


    else:
        return render(request, 'landing_page/about.html')


    return render(request, 'landing_page/thanku_page.html')


class VideoPageView(TemplateView):
    template_name = 'video_page/video_page.html'

    def get(self, request, *args, **kwargs):
        url_id = request.GET.get('id', '')
        try:
            # user_id = int(request.POST['id'])
            # user = UserInfo.objects.get(url_id=url_id)
            user = UserInfo.objects.all().filter(url_id=url_id)[0]  # .get(url_id=url_id)
            user.visits_counter = user.visits_counter + 1
            user.save()

        except User.DoesNotExist:
            return render(request, 'landing_page/about.html')

        return render(request, 'video_page/video_page.html')


class UnsubscribeView(View):
    template_name = 'email_page/unsubscribe.html'

    def get(self, request, *args, **kwargs):
        url_id = request.GET.get('id', '')
        try:
            # user_id = int(request.POST['id'])
            user = UserInfo.objects.get(url_id=url_id)
            user.unsubscribe = 1
            user.save()

        except User.DoesNotExist:
            return render(request, 'landing_page/about.html')

        return render(request, 'email_page/unsubscribe.html')

    def post(self, request, *args, **kwargs):
        url_id = request.GET.get('id', '')
        try:
            # url_id = int(request.POST['id'])
            user = UserInfo.objects.all().filter(url_id=url_id)[0]      #.get(url_id=url_id)
            user.unsubscribe = 0
            user.save()

        except User.DoesNotExist as e:
            print(e)
            return render(request, 'landing_page/about.html')
        except:
            return render(request, 'landing_page/about.html')

        return render(request, 'email_page/unsubscribe.html')
