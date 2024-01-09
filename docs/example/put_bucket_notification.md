# PUT Bucket Notification

## Request Elements

|      Name      |  Type  | Description                                                                                                                                                                                                                                                                                                                                                     | Required |
| :------------: | :----: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: |
| notifications  | Array  | The configuration rules you set in bucket notification, <br>the elements in the configuration item are explained below.                                                                                                                                                                                                                                         |   Yes    |
|       id       | String | Optional unique identifier for each of the configurations in the NotificationConfiguration.                                                                                                                                                                                                                                                                     |   Yes    |
|  event_types   | Array  | The type of event. Whenever a type of event is triggered, a notification will be sent. <br>Now available types: <br> - “create_object”: When an object has been created <br> - “delete_object”: When an object has been deleted <br> - “abort_multipart”: When abort a multipart upload <br> - “complete_multipart”: When a multipart upload has been completed |   Yes    |
| object_filters | Array  | Object name matching rule(glob patterns)                                                                                                                                                                                                                                                                                                                        |    no    |
|   cloudfunc    | String | Event handles cloud services, receives events triggered in the notification and processes them. <br>Now available: <br> - tupu-porn: Tupu porn check service <br> - notifier: Notification service. Push the QingStor events to notify_url<br> - image: Image basic processing service                                                                          |   Yes    |
| cloudfunc_args | Object | Custom parameters provided to cloudfunc                                                                                                                                                                                                                                                                                                                         |    No    |
|   notify_url   | String | URL, which notifies the event processing result, <br>requests the processing result to be notify_url in method POST when the event is processed. <br>If the request with method POST is timeout, it will be retried. <br>The timeout time is 5S and the retry interval is 1s.                                                                                   |    No    |

### Parameters in image basic processing service

When cloudfunc has been set as image, we need cloudfunc_args as below parameters. <br>
Object storage will process the image according to the specified picture processing rules and save the result back to object storage.

|    Name     |  Type  | Description                                                                                                                                                                     | Required |
| :---------: | :----: |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :------: |
|   action    | String | The specific operation parameters of the picture, see [image basic processing service](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/image_process/) for more info.                                                                         |   Yes    |
| key_prefix  | String | Prefix of the name of the object processed, “gen” is the default.                                                                                                               |    No    |
| key_seprate | String | A separator between key_prefix and object, “_“ is the default.                                                                                                                  |    No    |
| save_bucket | String | The target bucket name that is saved as. <br>The default is the current bucket where the object is located.                                                                     |    No    |

See [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/notification/put_notification/) for more information about request elements.

## Code Snippet

Initialize the Qingstor object with your AccessKeyID and SecretAccessKey.

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

Initialize a Bucket object according to the bucket name you set for subsequent creation:

```python
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

then you can PUT Bucket Notification

```python
notifications = [
    {
        "cloudfunc": "tupu-porn",
        "event_types": [
            "create_object"
        ],
        "cloudfunc_args": None,
        "id": "notification-1",
        "object_filters": [
            "*", "test"
        ],
        "notify_url": "http://user_notify_url"
    }
]
resp = bucket_srv.put_notification(notifications=notifications)
if resp.status_code != 200:
    print("Set notifications of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, "utf-8")))
else:
    print("Put bucket notifications successfully.")
```
