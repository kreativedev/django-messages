from django_messages.models import inbox_count_for, unread_messages_for

def inbox(request):
    if request.user.is_authenticated():
        return {'messages_inbox_count': inbox_count_for(request.user)}
    else:
        return {}

def unread_messages(request):
	if request.user.is_authenticated():
		return {'unread_messages': unread_messages_for(request.user)}
	else:
		return {}