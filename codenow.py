from datetime import time
from paynow import Paynow


paynow = Paynow(
    '18812', 
    '1b7591ad-53e9-4dfb-8f0e-f4afbe5f42f1',
    'http://google.com', 
    'http://google.com'
    )

payment = paynow.create_payment('food', 'kodebluded@gmail.com')

payment.add('food fo kids', 800)

response = paynow.send_mobile(payment, '0772222222', 'ecocash')


if(response.success):
    poll_url = response.poll_url

    print("Poll Url: ", poll_url)

    status = paynow.check_transaction_status(poll_url)

    print("Payment Status: ", status.status)
else:
    print("There was an error")