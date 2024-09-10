from .models import Category,Tag, Article

def get_main_context(request):
    categories = Category.objects.all()
    Tags = Tag.objects.all()
    trend_news = Article.objects.all().order_by("-views")[:7]
    context = {

        "categories":categories,
        "Tags":Tags,
        "trend_news":trend_news,
        

    }
    return context


