from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from core.models import Contact, GetQuote, Service, Technology, CaseStudy, CSCategory, FAQ, SEOHomepage, ServicePageLead
from .forms import ServicePageLeadForm

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

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, status="published")
    faqs = service.faqs.all()
    section_1 = getattr(service, 'service_section_1', None)  # Avoids errors if it doesn't exist
    section_2 = getattr(service, 'service_section_2', None)  # If you make this OneToOneField too
    highlights = service.service_highlight.all()
    technicals = service.technical_highlight.all()
    # services = Service.objects.filter(status="published")

    form = ServicePageLeadForm()

    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        form = ServicePageLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.page_url = request.build_absolute_uri()  # Capture the page URL
            lead.save()
            return JsonResponse({"success": True, "message": "Thank you! Your request has been submitted."})

        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    context = {
        'service': service,
        'section_1': section_1,
        'section_2': section_2,
        'highlights': highlights,
        'technicals': technicals,
        'faqs': faqs,
       #  'services': services,
        'form': form,
    }
    return render(request, 'core/services/service_detail.html', context)

def service_detail_form_submit(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        form = ServicePageLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.page_url = request.POST.get("page")  # Get the correct URL from AJAX request
            lead.save()
            return JsonResponse({"success": True, "message": "Thank you! Your request has been submitted."})
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

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