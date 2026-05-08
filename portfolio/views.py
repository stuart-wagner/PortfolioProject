from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Project, Resume, SkillType, Skill, Portrait
from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.all()[:3]
    active_portrait = Portrait.objects.filter(is_active=True).first()
    context = {'featured_projects': featured_projects, 'portrait': active_portrait}
    return render(request, 'portfolio/home.html', context)


def about(request):
    return render(request, 'portfolio/about.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def skills(request):
    skill_types = SkillType.objects.prefetch_related('skills').all()
    return render(request, 'portfolio/skills.html', {'skill_types': skill_types})


def resume(request):
    active_resume = Resume.objects.filter(is_active=True).first()
    return render(request, 'portfolio/resume.html', {'resume': active_resume})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f"New message from {name}",
                    message=message,
                    from_email=email,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Message sent successfully!')
            except Exception as e:
                messages.error(request, f'Error sending message: {str(e)}')

            return redirect('portfolio:contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})
