from django.core.management.base import BaseCommand
from portfolio.models import SkillType, Skill


class Command(BaseCommand):
    help = 'Seeds the database with initial skill types and skills'

    def handle(self, *args, **options):
        # Create skill types
        skill_types_data = [
            {
                'name': 'Languages',
                'icon': 'fas fa-code',
                'color': 'info',
                'order': 1,
                'skills': ['Python', 'JavaScript', 'SQL', 'HTML/CSS']
            },
            {
                'name': 'AI & LLM Tools',
                'icon': 'fas fa-brain',
                'color': 'warning',
                'order': 2,
                'skills': ['LangChain', 'OpenAI API', 'Google AI Studio', 'n8n', 'Anthropic Claude']
            },
            {
                'name': 'Frameworks & Libraries',
                'icon': 'fas fa-cube',
                'color': 'success',
                'order': 3,
                'skills': ['Django', 'React', 'FastAPI', 'scikit-learn', 'pandas']
            },
            {
                'name': 'Other Skills',
                'icon': 'fas fa-star',
                'color': 'danger',
                'order': 4,
                'skills': ['RAG', 'Prompt Engineering', 'API Integration', 'Database Design', 'Web Scraping']
            },
        ]

        for st_data in skill_types_data:
            skills_list = st_data.pop('skills')
            skill_type, created = SkillType.objects.get_or_create(
                name=st_data['name'],
                defaults=st_data
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created SkillType: {skill_type.name}'))
                
                # Create skills for this skill type
                for order, skill_name in enumerate(skills_list, 1):
                    skill, skill_created = Skill.objects.get_or_create(
                        name=skill_name,
                        skill_type=skill_type,
                        defaults={'order': order}
                    )
                    if skill_created:
                        self.stdout.write(f'  Created Skill: {skill.name}')
            else:
                self.stdout.write(f'SkillType already exists: {skill_type.name}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded skills data'))
