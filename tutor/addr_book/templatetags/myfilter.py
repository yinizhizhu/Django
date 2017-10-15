from django import template
register = template.Library()
def get(value, arg):
	return value[arg]
register.filter('get',get)