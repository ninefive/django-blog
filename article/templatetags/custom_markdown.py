import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library() # Must be added to the definition of your own filters

@register.filter(is_safe = True) # register template filter
@stringfilter # string args
def custom_markdown(value):
	return mark_safe(markdown.markdown(value,
		extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
		safe_mode = True,
		enable_attributes = False))
