from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from ithacaweb.projects.models import ProjectElement, ProjectType
from ithacaweb.base.models import People, FooterText

'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''


class ProjectElementAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail ITHACA" menu item
    # rather than under the default Snippets section.
    model = ProjectElement


class ProjectTypeAdmin(ModelAdmin):
    model = ProjectType


class ProjectModelAdminGroup(ModelAdminGroup):
    menu_label = 'Categories'
    menu_icon = 'fa-suitcase'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ProjectElementAdmin, ProjectTypeAdmin)


class PeopleModelAdmin(ModelAdmin):
    model = People
    menu_label = 'People'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('first_name', 'last_name', 'job_title', 'thumb_image')


class FooterTextAdmin(ModelAdmin):
    model = FooterText


class ITHACAModelAdminGroup(ModelAdminGroup):
    menu_label = 'Misc'
    menu_icon = 'fa-asterisk'  # change as required
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = (PeopleModelAdmin, FooterTextAdmin)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(ProjectModelAdminGroup)
modeladmin_register(ITHACAModelAdminGroup)
