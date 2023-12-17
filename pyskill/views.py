from django.views.generic import TemplateView

from pyskill.forms import DispatchForm
from pyskill.models import Dispatch


from pyskill.src.python_vac_data import pure_skills, vac_amount

from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from config import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class IndexView(TemplateView):
    template_name = "pyskill/index_2.html"


class ShowSkills(TemplateView):
    template_name = "pyskill/show_skills.html"

    def get_context_data(self, **kwargs):
        """Формируем данные для отображения в шаблоне"""

        context_data = super().get_context_data(**kwargs)

        context_data["pure_skills"] = pure_skills  # хард скиллы

        context_data["vac_amount"] = vac_amount  # количество анализируемых вакансий

        return context_data


class DispatchCreateView(CreateView):

    """Создание рассылки пользователю"""

    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy("pyskill:index")

    def form_valid(self, form):
        # Сохраняем данные из формы

        response = super().form_valid(form)

        # Получаем значение поля mail_to_send из формы

        mail_to_send = form.cleaned_data["mail_to_send"]

        subject = "Аналитика PySkiLL"

        # Формируем html - версию письма с добавлением шаблонных переменных

        html_message = render_to_string(
            "pyskill/skills_to_send.html",
            {"pure_skills": pure_skills, "vac_amount": vac_amount},
        )
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER

        # Создаем объект EmailMultiAlternatives
        msg = EmailMultiAlternatives(subject, plain_message, from_email, [mail_to_send])

        # Добавляем HTML-версию письма
        msg.attach_alternative(html_message, "text/html")

        # Отправляем письмо
        msg.send()

        return response


class DispatchUpdateView(UpdateView):
    model = Dispatch
    form_class = DispatchForm
    success_url = reverse_lazy("pyskill:index")
