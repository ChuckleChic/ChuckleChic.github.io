from django.shortcuts import render, redirect
from .models import DiaryEntry, SuggestedContent
from django.contrib.auth.decorators import login_required
from .ml_model import analyze_sentiment, generate_suggestions  # custom ML functions


def home(request):
    return render(request, 'home.html')  # You can create a home.html template or return any content here

# View to add a diary entry
@login_required
def add_entry(request):
    if request.method == "POST":
        content = request.POST.get('content')
        
        # Save the diary entry
        entry = DiaryEntry.objects.create(user=request.user, content=content)
        
        # Analyze sentiment and update the entry
        sentiment = analyze_sentiment(content)
        entry.sentiment = sentiment
        entry.save()

        # Generate content suggestions based on sentiment
        suggestions = generate_suggestions(sentiment)
        
        # Save the suggestions
        for suggestion in suggestions:
            SuggestedContent.objects.create(diary_entry=entry, suggestion=suggestion)

        return redirect('entry_detail', entry_id=entry.id)

    return render(request, 'add_entry.html')

# View to display the diary entry and suggestions
@login_required
def entry_detail(request, entry_id):
    entry = DiaryEntry.objects.get(id=entry_id)
    return render(request, 'entry_detail.html', {'entry': entry})

