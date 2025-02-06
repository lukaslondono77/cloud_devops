import boto3

def lambda_handler(event, context):
    ses = boto3.client('ses')
    ses.send_email(
        Source='sender@example.com',
        Destination={'ToAddresses': ['recipient@example.com']},
        Message={
            'Subject': {'Data': 'Task Notification'},
            'Body': {'Text': {'Data': 'A new task has been created!'}}
        }
    )
    return {'statusCode': 200, 'body': 'Email sent!'}
