import boto3

def send(txt):
	# Create an SNS client
	client = boto3.client(
    		"sns",
    		aws_access_key_id="AKIAXDK47CXK2TIZMMF3",
    		aws_secret_access_key="kleDihHqu1i+GVE0vaJ0OU0GciVMIFAd28bF9bPL",
    		region_name="us-east-1"
	)

	# Send your sms message.
	client.publish(
    		PhoneNumber="+1 5305649132",
    		Message=txt
	)