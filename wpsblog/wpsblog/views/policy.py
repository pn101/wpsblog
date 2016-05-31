from django.shortcuts import render


def terms(request):
    return render(
            request,
            'policy/terms.html',
            {
                'site_name': 'Terms & Conditions',
            }
    )


def privacy(request):
    return render(
            request,
            'policy/privacy.html',
            {
                'site_name': 'Privacy',
            }
    )


def disclaimer(request):
    return render(
            request,
            'policy/disclaimer.html',
            {
                'site_name': 'Disclaimer',
            }
    )
