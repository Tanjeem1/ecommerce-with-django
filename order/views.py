import json
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Order, OrderItem

def start_order(request):
    try:
        cart = Cart(request)
        data = json.loads(request.body)
        total_price = 0
        items = []

        for item in cart:
            product = item['product']
            total_price += product.price * int(item['quantity'])
            obj = {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price),  # Convert the payment into integer amount
                },
                'quantity': item['quantity']
            }
            items.append(obj)
        
        stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
        if not stripe.api_key:
            return JsonResponse({'error': 'Stripe API key not configured'}, status=400)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url='http://127.0.0.1:8000/cart/success/',
            cancel_url='http://127.0.0.1:8000/cart/cancel'
        )
        payment_intent = session.payment_intent

        order = Order.objects.create(
            user=request.user, 
            first_name=data['first_name'], 
            last_name=data['last_name'], 
            email=data['email'], 
            phone=data['phone'], 
            address=data['address'], 
            zipcode=data['zipcode'], 
            place=data['place'],
            paid=False,  # Set to False until payment confirmed
            paid_amount=total_price
        )    
        order.payment_intent = payment_intent
        order.save()

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity
            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        cart.clear()
        return JsonResponse({'session': {'id': session.id}})  # Match frontend expectation

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=400)