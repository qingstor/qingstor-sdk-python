# DeleteMultipleObjects Example

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

Then set the input parameters used by the `delete_multiple_objects` method. `quiet` Specifies whether to return a list of deleted objects.

```python
objects = [{"key": "file_will_be_delete.jpg"}, {"key": "file_will_be_delete.zip"}]
```

For parameter details, please refer to [Official API Documentation](https://docs.qingcloud.com/qingstor/api/bucket/delete_multiple).

Then call the `delete_multiple_objects` method to delete the object. object_key Sets the filepath of the object to be deleted (in the current bucket).

```python
output = bucket_srv.delete_multiple_objects(objects=objects, quiet=False)
if output.status_code != 200:
    print("Delete objects({}) in bucket({}) failed with given message: {}".format(
        objects,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print(output['deleted'])  # 'deleted' contains objects deleted successfully.
```

If the operation returns correctly, the response status code will be 200.
