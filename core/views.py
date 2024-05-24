from django.shortcuts import render
from django.http import JsonResponse
from core.models import Contact, GetQuote, Service, Technology, CaseStudy, CSCategory, FAQ, FAQSMangalore, SEOHomepage

# Create your views here.

def index(request):
    service = Service.objects.all()
    tech = Technology.objects.all()
    portfolio = CaseStudy.objects.all().order_by("date")
    seo = CaseStudy.objects.filter(category=2)
    webdev = CaseStudy.objects.filter(category=1)
    cscategory = CSCategory.objects.all()
    faq = FAQ.objects.all()
    meta = SEOHomepage.objects.get(id=1)

    context = {
        "service": service,
        "tech": tech,
        "portfolio": portfolio,
        "seo":seo,
        "webdev": webdev,
        "cscategory": cscategory,
        "faq": faq,
        "meta": meta,
    }

    return render(request, 'core/index.html', context)

def portfolio(request, slug):
    study = CaseStudy.objects.get(slug=slug)

    context = {
        "study": study
    }

    return render(request, 'core/portfolio-details.html', context)

def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = Contact.objects.create(
        full_name=full_name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )

    data = {
        "bool": True,
        "message": "Message Sent Successfully"
    }

    return JsonResponse({"data":data})

def ajax_get_quote(request):
    email = request.GET['email']

    get_quote = GetQuote.objects.create(
        email=email,
    )

    data = {
        "bool": True,
        "message": "Will get back to you soon!"
    }

    return JsonResponse({"data":data})

def s_magalore(request):
    tech = Technology.objects.all()
    seo = CaseStudy.objects.filter(category=2)
    webdev = CaseStudy.objects.filter(category=1)
    faq = FAQSMangalore.objects.all()


    context = {
        "tech": tech,
        "seo": seo,
        "webdev": webdev,
        "faq": faq,
    }

    return render(request, 'core/lp_s_mangalore.html', context)