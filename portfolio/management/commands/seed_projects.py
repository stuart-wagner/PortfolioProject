from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Seeds the database with 6 portfolio projects'

    def handle(self, *args, **options):
        projects_data = [
            {
                'title': 'Conversational AI Chatbot',
                'summary': 'An intelligent chatbot powered by LangChain and OpenAI APIs.',
                'business_problem': 'Organizations need efficient, scalable customer support solutions that can handle common inquiries 24/7 without human intervention.',
                'tools_used': 'Python, LangChain, OpenAI API, FastAPI, PostgreSQL',
                'key_features': '- Natural language understanding\n- Context-aware responses\n- Multi-turn conversations\n- Fallback to human agents\n- Analytics dashboard',
                'your_role': 'Led the architecture design and implementation of the chatbot core. Designed the prompt engineering strategy and integrated with OpenAI APIs. Built the FastAPI backend and handled deployment.',
                'biggest_challenge': 'Maintaining context across long conversations while managing token limits and ensuring accurate information retrieval from knowledge bases.',
                'what_learned': 'Learned the nuances of prompt engineering, token management, and the importance of clear conversation design. Gained experience with production LLM systems and handling edge cases.',
                'link': 'https://github.com/yourusername/chatbot-project'
            },
            {
                'title': 'n8n Agent Workflow Automation',
                'summary': 'Built complex automation workflows using n8n for data processing and API integration.',
                'business_problem': 'Manual data processes are error-prone, time-consuming, and don\'t scale. Businesses need reliable automation that integrates multiple systems.',
                'tools_used': 'n8n, Webhooks, REST APIs, JSON, Node.js, PostgreSQL',
                'key_features': '- Multi-step automation workflows\n- Real-time data synchronization\n- Error handling and retry logic\n- Webhook triggers\n- Extensive API integrations',
                'your_role': 'Designed the workflow architecture and implemented complex node configurations. Integrated with external APIs and managed webhook-based triggers. Optimized for reliability and performance.',
                'biggest_challenge': 'Handling edge cases in data transformation and ensuring workflows remain stable at scale with varying data inputs.',
                'what_learned': 'Deepened understanding of workflow automation patterns, API integration best practices, and the importance of robust error handling in production systems.',
                'link': 'https://github.com/yourusername/n8n-workflows'
            },
            {
                'title': 'LangChain RAG Agent System',
                'summary': 'Retrieval-Augmented Generation system using LangChain for intelligent document processing.',
                'business_problem': 'Organizations struggle to leverage their document repositories for accurate, context-aware responses without reimplementing custom search systems.',
                'tools_used': 'Python, LangChain, OpenAI, FAISS, ChromaDB, FastAPI, Pinecone',
                'key_features': '- Vector-based document retrieval\n- Multi-step reasoning\n- Tool integration framework\n- Context window optimization\n- Citation tracking',
                'your_role': 'Architected the RAG pipeline including vector embeddings, retrieval logic, and LLM integration. Implemented custom tools and optimized context management.',
                'biggest_challenge': 'Optimizing retrieval accuracy and managing the balance between context length and response quality within token constraints.',
                'what_learned': 'Mastered RAG patterns, vector databases, embeddings optimization, and the technical considerations when building production LLM applications.',
                'link': 'https://github.com/yourusername/langchain-rag'
            },
            {
                'title': 'Google AI Studio Multimodal Project',
                'summary': 'Multimodal AI application combining images, text, and video processing with Google AI Studio.',
                'business_problem': 'Processing diverse media types requires specialized models. A unified approach to multimodal data analysis is needed.',
                'tools_used': 'Google AI Studio, Vision API, Python, FastAPI, Cloud Storage, React',
                'key_features': '- Image analysis and description\n- Video understanding\n- Cross-modal reasoning\n- Real-time processing\n- Web-based UI',
                'your_role': 'Integrated Google AI Studio APIs and designed the multimodal processing pipeline. Built the FastAPI backend and React frontend for media upload and analysis.',
                'biggest_challenge': 'Managing API rate limits and ensuring consistent performance across different media types and sizes.',
                'what_learned': 'Gained expertise in multimodal AI capabilities, working with Google Cloud services, and building user interfaces for AI applications.',
                'link': 'https://github.com/yourusername/multimodal-ai'
            },
            {
                'title': 'Machine Learning Predictive Model',
                'summary': 'scikit-learn-based predictive modeling project demonstrating data science fundamentals.',
                'business_problem': 'Businesses need data-driven predictions for inventory, customer behavior, or market trends without building models from scratch.',
                'tools_used': 'Python, scikit-learn, pandas, numpy, Matplotlib, PostgreSQL',
                'key_features': '- Feature engineering pipeline\n- Model training and validation\n- Hyperparameter optimization\n- Performance metrics dashboard\n- Model serialization',
                'your_role': 'Conducted exploratory data analysis, engineered features, and trained multiple models. Compared algorithms and selected the best performer. Created performance visualizations.',
                'biggest_challenge': 'Handling class imbalance and feature scaling to prevent overfitting while maintaining model interpretability.',
                'what_learned': 'Strengthened foundation in machine learning workflows, statistical validation, and the importance of thorough data exploration.',
                'link': 'https://github.com/yourusername/ml-predictor'
            },
            {
                'title': 'Campus SkillSwap Django App',
                'summary': 'Full-stack CRUD application for skill-sharing community built with Django and React.',
                'business_problem': 'Students and professionals want to exchange skills and knowledge with peers but lack a platform designed for this purpose.',
                'tools_used': 'Django, Django REST Framework, React, PostgreSQL, Docker, AWS',
                'key_features': '- User profiles and skill listings\n- Request/match system\n- Review and rating system\n- Real-time notifications\n- Search and filtering',
                'your_role': 'Led full-stack development from database design through deployment. Built REST APIs, implemented authentication, and created responsive React components.',
                'biggest_challenge': 'Designing an intuitive matching algorithm that considers skill compatibility, availability, and user preferences.',
                'what_learned': 'Gained comprehensive full-stack experience, improved understanding of user-centered design, and learned deployment practices.',
                'link': 'https://github.com/yourusername/skillswap'
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created project: {project.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Project already exists: {project.title}')
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with projects'))
