from django.contrib.comments.signals import comment_was_posted

def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    comment.is_public = False
    comment.save()

comment_was_posted.connect(on_comment_was_posted)