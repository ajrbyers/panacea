from journal import models as journal_models


def get_journal():
    journals = journal_models.Journal.objects.all()

    if journals:
        return journals[0]
    else:
        return None

class SiteSettingsMiddleware(object):
    @staticmethod
    def process_request(request):
        """ This middleware class sets a series of variables for templates and views to access inside the request object

        :param request: the current request
        :return: None or an http 404 error in the event of catastrophic failure
        """
        request.port = request.META['SERVER_PORT']
        request.base_url = 'http{0}://{1}'.format('s' if request.is_secure() else '', request.get_host())
        request.journal = get_journal()

