from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import render


class OrganizationSocialAccountAdapter(DefaultSocialAccountAdapter):
    def new_user(self, request, sociallogin):
        """
        ? Used to configure the domain of social authentication email address.
        TODO: Utilize models to add the domain name for authentication.
        """
        print("\n ---------------------- New User -------------------------")
        organization_lists =[
            "qodemedia.net"
        ]
        if not request.GET.get('hd') in organization_lists:
            print("error occured")
            response = render(request,"errors/login_error.html")
            print(type(response))
            raise ImmediateHttpResponse(response)
        else:
            return super().new_user(request, sociallogin)