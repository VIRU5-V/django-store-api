import paypalrestsdk
from paypalrestsdk.exceptions import ResourceNotFound, ResourceInvalid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreatePaymentSerializer
from oscar.core.loading import get_model
from django.conf import settings

Order = get_model('order', 'Order')


class PaymentView(APIView):
    def post(self, request, pk=None):
        serializer = CreatePaymentSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data['order_id']
            basket_id = serializer.validated_data['basket_id']

            order = Order.objects.filter(basket_id=basket_id).first()

            payment = paypalrestsdk.Payment({
                'intent': 'sale',
                'payer': {
                    'payment_method': 'paypal'
                },
                'transactions': [{
                    'amount': {
                        'total': str(order.total_incl_tax),
                        'currency': order.currency,
                    }
                }],
                'redirect_urls': {
                    'return_url': settings.BASE_URL + f'/payment_process/verify_payment/?order_id={order_id}',
                    'cancel_url': settings.BASE_URL,
                }
            })

            if payment.create():
                approval_url = next(link.href for link in payment.links if link.method == 'REDIRECT')
                return Response({'approval_url': approval_url})
            else:
                return Response(payment.error, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentVerfification(APIView):
    def get(self, request, *args, **kwargs):
        payment_id = request.query_params.get('paymentId')
        payer_id = request.query_params.get('PayerID')
        
        order_id = request.query_params.get('order_id')

        try:
            payment = paypalrestsdk.Payment.find(payment_id)

            if payment.execute({"payer_id": payer_id}):
                    # update order status
                    order = Order.objects.get(number=order_id)
                    order.set_status('Complete')
                    order.save()
                    return Response({"payment_status": 'successful'})
            else:
                return Response({"msg": "payment already processed", "payment_status": "already processed"})

        except (ResourceNotFound, ResourceInvalid) as e:
            return Response({'error': str(e), 'payment_status': 'Failed' }, status=status.HTTP_400_BAD_REQUEST)