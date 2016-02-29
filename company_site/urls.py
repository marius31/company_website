from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static 
#import debug_toolbar

#admin.autodiscover() 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'company_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', 'company_site.views.index', name='index'),
	# first part in the tuple url pattern is a regex match
	# second part projectname.views.method names for that view
	# third part links function name to template for ex index.html
	url(r'^about/$', 'company_site.views.about', name='about'),
	url(r'^projects/$', 'company_site.views.projects', name='projects'),
	url(r'^interior_design/$', 'company_site.views.interior_design', name='interior_design'),
	url(r'^exterior_design/$', 'company_site.views.exterior_design', name='exterior_design'),
	url(r'^constructions/', 'company_site.views.constructions', name='constructions'),
	url(r'^installations/$', 'company_site.views.installations', name='installations'),
	url(r'^customer_advice/$', 'company_site.views.customer_advice', name='customer_advice'),
	url(r'^contact/$', 'company_site.views.contact', name='contact'),
	url(r'^contact/done/$', TemplateView.as_view(
								template_name='contact_done.html',
								content_type='text/html'),
								name='contact'),
)

if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

		#urlpatterns += patterns('',
		#url(r'^__debug__/', include(debug_toolbar.urls)),
		#)
