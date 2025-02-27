from django.utils.timezone import now
import datetime
from django import template

register = template.Library()

@register.filter
def time_until(value):
    if not value:
        return ''
    
    time_diff = now() - value

    if time_diff < datetime.timedelta(days=1):
        hours = int(time_diff.total_seconds() // 3600)
        minutes = int(time_diff.total_seconds() // 60)

        if hours > 0:
            return f'{hours} hours ago'
        elif minutes > 0:
            return f'{minutes} minutes ago'
        else:
            return 'Just now'
        
    else:
        return value.strftime('%b %d, %Y')