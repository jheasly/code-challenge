import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # Given a GET argument named 'address' at
        # /api/parse?address=[address goes here], uses usaddress 
        # parse method to return three components; input_string,
        # address_components, address_type

        try:
            input_string = request.query_params['address']
            address_components, address_type = self.parse(input_string)
            return Response({
                'input_string': input_string,
                'address_components': address_components,
                'address_type': address_type,
            })
        except ParseError:
            raise

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        try:
            address_components, address_type = usaddress.tag(address)
            return address_components, address_type
        except usaddress.RepeatedLabelError:
            raise
