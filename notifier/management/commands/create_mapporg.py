from django.core.management.base import BaseCommand, CommandError
from notifier.models import MappOrg
from optparse import make_option

class Command(BaseCommand):

    help = "Create org with url_lms and url_logo in MappOrg db"

    option_list = BaseCommand.option_list + (
        make_option('--org',
                    action='store',
                    dest='org',
                    default=None,
                    help='organization course'),
        make_option('--logo',
                    action='store',
                    dest='logo',
                    default=None,
                    help='organization logo'),
        make_option('--site',
                    action='store',
                    dest='site',
                    default=None,
                    help='organization site'),
        make_option('--create-map',
                    action='store_true',
                    dest='create_mapporg',
                    default=None,
                    help='Create org with url_lms and url_logo in MappOrg db'),
        make_option('--modify-map',
                    action='store_true',
                    dest='modify_mapporg',
                    default=None,
                    help='Modify org with url_lms or url_logo in MappOrg db'),
    )

    def create_mapporg(self, org, logo, site):
        if MappOrg.objects.filter(organization=org).exists():
            mapp_org = MappOrg.objects.get(organization=org)
            mapp_org.url_site = site
            mapp_org.url_logo = logo
            mapp_org.save()
            print "Modificado Correctamente"
        else:
            mapp_org = MappOrg.objects.create(
                        organization=org,
                        url_site=site,
                        url_logo=logo
                    )
            print "Creado Correctamente"
    
    def modify_mapporg(self, org, options):
        if MappOrg.objects.filter(organization=org).exists():
            mapp_org = MappOrg.objects.get(organization=org)
            if options.get('logo'):
                mapp_org.url_logo = options.get('logo')
                print "Logo odificado Correctamente"
            if options.get('site'):
                mapp_org.url_site = options.get('site')
                print "Dominio modificado Correctamente"
            mapp_org.save()
            if not options.get('site') and not options.get('logo'):
                print "Falta parametros"
        else:
            print "No existe la organizacion"

    def handle(self, *args, **options):
        """
        """
        
        if options.get('create_mapporg') and options.get('org') and options.get('logo') and options.get('site'):
            org = options['org']
            logo = options['logo']
            site = options['site']
            self.create_mapporg(org, logo, site)
            return
        elif options.get('modify_mapporg') and options.get('org'):
            org = options['org']
            self.modify_mapporg(org, options)
            return
        else:
            print "Error en los parametros"
