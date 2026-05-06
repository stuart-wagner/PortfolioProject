from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages
from .models import Project
from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.all()[:3]
    context = {'featured_projects': featured_projects}
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
    skills_data = {
        'languages': ['Python', 'JavaScript', 'SQL', 'HTML/CSS'],
        'ai_tools': ['LangChain', 'OpenAI API', 'Google AI Studio', 'n8n', 'Anthropic Claude'],
        'frameworks': ['Django', 'React', 'FastAPI', 'scikit-learn', 'pandas'],
        'other': ['RAG', 'Prompt Engineering', 'API Integration', 'Database Design', 'Web Scraping']
    }
    return render(request, 'portfolio/skills.html', {'skills': skills_data})


def resume(request):
    return render(request, 'portfolio/resume.html')


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
                    recipient_list=['your-email@example.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Message sent successfully!')
            except Exception as e:
                messages.error(request, f'Error sending message: {str(e)}')

            return render(request, 'portfolio/contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})
