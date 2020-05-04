from django.views import View
from django.shortcuts import render
from django.http import Http404


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'welcome.html')


def menu(request):
    return render(request, 'menu.html')

class GetTicketView(View):
    const = dict({'ticket_number': 0})
    change_oil_q = []
    inflate_tires_q = []
    diagnostic_q = []

    def get(self, request, service_type):
        minutes_to_wait = 0
        self.const['ticket_number'] += 1
        if service_type == 'change_oil':
            minutes_to_wait += 2 * len(self.change_oil_q)
            self.change_oil_q.append(self.const['ticket_number'])
        elif service_type == 'inflate_tires':
            minutes_to_wait += 2 * len(self.change_oil_q) + 5 * len(self.inflate_tires_q)
            self.inflate_tires_q.append(self.const['ticket_number'])
        elif service_type == 'diagnostic':
            minutes_to_wait += 2 * len(self.change_oil_q) + 5 * len(self.inflate_tires_q) + 30 * len(self.diagnostic_q)
            self.diagnostic_q.append(self.const['ticket_number'])
        else:
            self.const['ticket_number'] -= 1
            raise Http404
        return render(request, 'ticket.html', {
            'ticket_number': self.const['ticket_number'],
            'minutes_to_wait': minutes_to_wait})

    class Process(View):

        def get(self, request):

            return render(request, 'process.html', {
                'change_oil_number': len(GetTicketView.change_oil_q),
                'inflate_tires_number': len(GetTicketView.inflate_tires_q),
                'diagnostic_number': len(GetTicketView.diagnostic_q),
            })
