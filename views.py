from django.shortcuts import render, get_object_or_404
from gpio.models import Switch

def index(request):
	return render(request, 'gpio/index.html', {
		'switches': Switch.objects.all()
	})
	
def control_switch(request, switch_id, state):
	switch = get_object_or_404(Switch, pk=switch_id)
	switch.write(state)
	return render(request, 'gpio/switch.html', {
		'switch': switch,
		'state': state
	})
