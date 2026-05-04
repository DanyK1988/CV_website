from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Render a one-page startup-style personal portfolio."""

    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Static data for fast landing-page delivery.
        # You can migrate this structure into models/admin later.
        context["profile"] = {
            "name": "Your Name",
            "role": "Data & Tech Professional",
            "headline": "Full-Stack Data Solutions",
            "intro": (
                "I design and ship scalable data platforms, analytics systems, "
                "web products, and AI-driven workflows with measurable business impact."
            ),
            "email": "you@example.com",
            "location": "Global / Remote",
            "socials": [
                {"label": "LinkedIn", "url": "#"},
                {"label": "GitHub", "url": "#"},
                {"label": "Resume", "url": "#"},
            ],
        }

        context["nav_items"] = [
            {"label": "About", "href": "#about"},
            {"label": "Data Engineering", "href": "#data-eng"},
            {"label": "Analytics", "href": "#analytics"},
            {"label": "Web", "href": "#web"},
            {"label": "AI", "href": "#ai"},
            {"label": "Git", "href": "#git"},
        ]

        context["sections"] = [
            {
                "id": "data-eng",
                "title": "Data Engineering",
                "subtitle": "Reliable pipelines, modern data stack, and production-grade architecture.",
                "tech_stack": [
                    "Python",
                    "Airflow",
                    "dbt",
                    "BigQuery",
                    "Kafka",
                    "Docker",
                ],
                "projects": [
                    {
                        "title": "Real-Time Event Pipeline",
                        "description": (
                            "Built a streaming pipeline for clickstream ingestion and near-real-time "
                            "analytics, with data quality checks and alerting."
                        ),
                    },
                    {
                        "title": "Warehouse Migration Program",
                        "description": (
                            "Led migration from legacy ETL to modular ELT using dbt and CI workflows, "
                            "improving reliability and delivery speed."
                        ),
                    },
                ],
            },
            {
                "id": "analytics",
                "title": "Analytics",
                "subtitle": "Metrics systems, BI experiences, and decision intelligence.",
                "tech_stack": [
                    "SQL",
                    "Looker",
                    "Tableau",
                    "Power BI",
                    "Pandas",
                    "A/B Testing",
                ],
                "projects": [
                    {
                        "title": "Executive KPI Command Center",
                        "description": (
                            "Created a unified KPI dashboard and metric definitions that aligned "
                            "cross-functional teams around one source of truth."
                        ),
                    },
                    {
                        "title": "Experimentation Insights Toolkit",
                        "description": (
                            "Delivered reusable experiment analysis templates to speed up "
                            "hypothesis validation and product decisions."
                        ),
                    },
                ],
            },
            {
                "id": "web",
                "title": "Web",
                "subtitle": "Beautiful, high-performance applications and APIs.",
                "tech_stack": [
                    "Django",
                    "Django REST Framework",
                    "React",
                    "Tailwind CSS",
                    "PostgreSQL",
                    "Nginx",
                ],
                "projects": [
                    {
                        "title": "Data Product Portal",
                        "description": (
                            "Developed a secure self-service portal where teams monitor data jobs, "
                            "track SLAs, and request new datasets."
                        ),
                    },
                    {
                        "title": "Customer Insights Web App",
                        "description": (
                            "Shipped a responsive app for segmentation and behavioral insights, "
                            "optimized for speed and usability."
                        ),
                    },
                ],
            },
            {
                "id": "ai",
                "title": "AI",
                "subtitle": "LLM integrations, intelligent assistants, and workflow automation.",
                "tech_stack": [
                    "OpenAI API",
                    "RAG",
                    "Vector DB",
                    "LangChain",
                    "Prompt Engineering",
                    "Evals",
                ],
                "projects": [
                    {
                        "title": "AI Knowledge Assistant",
                        "description": (
                            "Implemented a retrieval-augmented assistant over internal docs "
                            "to reduce support load and boost team productivity."
                        ),
                    },
                    {
                        "title": "Automated Analytics Narratives",
                        "description": (
                            "Built AI-generated dashboard summaries that convert metrics into "
                            "clear weekly business narratives."
                        ),
                    },
                ],
            },
            {
                "id": "git",
                "title": "Git",
                "subtitle": "Collaboration, clean history, and release confidence.",
                "tech_stack": [
                    "GitHub",
                    "GitFlow",
                    "Conventional Commits",
                    "GitHub Actions",
                    "Code Review",
                    "CI/CD",
                ],
                "projects": [
                    {
                        "title": "Release Automation Pipeline",
                        "description": (
                            "Set up semantic versioning and CI/CD checks to keep releases "
                            "predictable and safer."
                        ),
                    },
                    {
                        "title": "Monorepo Quality Guardrails",
                        "description": (
                            "Introduced lint/test gates, branch protections, and PR templates "
                            "to improve velocity without sacrificing quality."
                        ),
                    },
                ],
            },
        ]

        return context
