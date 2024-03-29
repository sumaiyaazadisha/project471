from django.shortcuts import redirect, get_object_or_404, render
from .models import Video

def redirect_to_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return redirect(video.url)

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos})

