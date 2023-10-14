import urllib.request
import os

os.system("clear")

ver = "\033[32m"

cor = "\033[45m"
car = "\033[34m"
cl = "\033[m"

print(f"""
PROTOCOLO DO SITE:

[01] HTTPS
[02] HTTP
""")

pro = int(input('? '))
if pro == 1:
    pro = 'https://'
elif pro == 2:
    pro = 'http://'
else:
    pass

print(f"\nEX.: {pro}site.dominio\n")

def siite():
    user = input(f"{ver}{pro}")
        
    print()
    subd = ["","register.","profile.","checkout.","help.","support.","contact.","about.","blog.","news.","products.","services.","faq.","privacy.","terms.","search.","gallery.","events.","forum.","downloads.","portfolio.","testimonials.","feedback.","videos.","contact-us.","pricing.","partners.","sitemap.","resources.","events-calendar.","shop.","newsroom.","forum-topic.","newsletter.","reviews.","testimonial.","contact-info.","pricing-plans.","affiliate-program.","team.","events-registration.","media.","downloads.","subscribe.","case-studies.","features.","test-drive.","feedback-form.","user-guide.","partnership.","press-releases.","knowledge-base.","contact-information.","join-us.","become-a-partner.","video-gallery.","catalog.","bookings.","sponsorship.","research.","events-gallery.","testimonials-page.","request-demo.","customer-service.","meet-the-team.","company-info.","terms-of-use.","customer-feedback.","affiliate-registration.","partner-program.","events-schedule.","subscribe-newsletter.","press-room.","blog-post.","customer-support-center.","our-team","product-catalog.","client-testimonials.","contact-details.","pricing-packages.","join-our-team.","partner-with-us.","video-library.","online-store.","news-articles.","forum-discussion.","privacy-policy.","ustomer-service-support.","how-it-works.","admin.","top.","pinel.","login.","users.","shopp.","itens."]
    cami = ["/register","/adm","/profile","/checkout","/help","/support","/contact","/about","/blog","/news","/products","/services","/faq","/privacy","/terms","/search","/gallery","/events","/forum","/downloads","/portfolio","/testimonials","/feedback","/videos","/contact-us","/pricing","/partners","/sitemap","/resources","/events-calendar","/shop","/newsroom ","/forum-topic","/newsletter","/reviews","/testimonial","/contact-info","/pricing-plans","/affiliate-program","/team","/events-registration","/media","/downloads","/subscribe","/case-studies","/features","/test-drive","/feedback-form","/user-guide","/partnership","/press-releases","/knowledge-base","/contact-information","/join-us","/become-a-partner","/video-gallery","/catalog","/bookings","/sponsorship","/research","/events-gallery","/testimonials-page","/request-demo","/customer-service","/meet-the-team","/company-info","/terms-of-use","/customer-feedback","/affiliate-registration","/partner-program","/events-schedule","/subscribe-newsletter","/press-room","/blog-post","/customer-support-center","/our-team","/product-catalog","/client-testimonials","/contact-details","/pricing-packages","/join-our-team","/partner-with-us","/video-library","/online-store","/news-articles","/forum-discussion","/privacy-policy","/customer-service-support","/how-it-works","/admin","/top","/pinel","/login","/users","/shopp","/itens"]
    for d in subd:
        try:
            site = f"{pro}{d}{user}/"
            exsite = urllib.request.urlopen(site)
            print(f"""{cor}[+]===> {site}{cl}
                        
""")
            for c in cami:
                try:
                    ssite = f'{site}{c}'
                    exssite = urllib.request.urlopen(ssite)
                    print(f"{car}{ssite}{cl}")
                except:
                    pass
        except:
            pass
siite()
