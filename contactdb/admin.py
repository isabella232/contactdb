from contactdb.models import Organisation, Person
from contactdb.models import Source, Countrycode
from contactdb.models import NetObject,ASN,Inetnum,Domainname
from contactdb.models import TelephoneNumber,URL,OtherCommunicationChannel
from contactdb.models import Tag
from django.contrib import admin

from contactdb.inetnumadmin import InetnumAdminPage

from django.core.exceptions import ValidationError

def createInlineAdmin(model_class, number_of_lines=0, key_name=None):
    class InlineAdmin(admin.TabularInline):
        model = model_class
        extra = number_of_lines
        fk_name = key_name
        
    return InlineAdmin

class OrganisationAdminPage(admin.ModelAdmin):
    list_display = ('name', 'country', 'email', 'pgp_fingerprint', 'business_hh_start', 'business_hh_end')
    search_fields = ['name' , 'email', 'country']
    list_filter = ['country']
    inlines = [
                createInlineAdmin(TelephoneNumber),
                createInlineAdmin(URL),
                createInlineAdmin(OtherCommunicationChannel),
#                createInlineAdmin(ProtectionProfile),
                createInlineAdmin(Tag),
              ]


class PersonAdminPage(admin.ModelAdmin):
    list_display = ('name', 'user', 'email', 'pgp_fingerprint', 'organisation', 'country', 'title', 'picture', 'remarks')
    exclude = ('last_logged_in', )
    search_fields = ['name', 'user']
    inlines = [
                createInlineAdmin(TelephoneNumber),
                createInlineAdmin(URL),
                createInlineAdmin(OtherCommunicationChannel),
#                createInlineAdmin(ProtectionProfile),
                createInlineAdmin(Tag),
              ]


admin.site.register(Organisation, OrganisationAdminPage)
admin.site.register(Person)

admin.site.register(Source)
admin.site.register(Countrycode)

admin.site.register(Inetnum, InetnumAdminPage)
