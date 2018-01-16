from celery import shared_task
from muonic.lib.app import App
from muonic.lib.consumers import BufferedConsumer
from muonic_django.consumer import Consumer as DjangoConsumer
from muonic.lib.analyzers import *
from django.conf import settings


@shared_task(bind=True)
def start_run(self, options = {}):

    if 'data_provider' not in options:
        options['data_provider'] = settings.MUONIC_DEFAULT_DAQ_PROVIDER

    if 'sim' not in options:
        options['sim'] = True

    consumers = [
        BufferedConsumer(settings.MUONIC_CONSUMER_BUFFER_SIZE,
                         DjangoConsumer(simulation=options.get('sim'), username=options.get('username')))
    ]

    analyzers = []

    if options.get('do_rate', False):
        analyzers += [RateAnalyzer(consumers=consumers, **options.get('rate_settings', {}))]

    if options.get('do_pulse', False):
        analyzers += [PulseAnalyzer(consumers=consumers, **options.get('pulse_settings', {}))]

    if options.get('do_velocity', False) and not options.get('decay', False):
        analyzers += [VelocityAnalyzer(consumers=consumers, **options.get('velocity_settings', {}))]

    if options.get('do_decay', False) and not options.get('velocity', False):
        analyzers += [DecayAnalyzer(consumers=consumers, **options.get('decay_settings', {}))]

    app = App(options, analyzers=analyzers)
    app.run(run_id=self.request.id)