# QingStor Image Processing Usage Guide

For processing the image stored in QingStor by a variety of basic operations, such as format, crop, watermark and so on.

Currently supported image formats are:

- png
- tiff
- webp
- jpeg
- pdf
- gif
- svg

> Currently, the encrypted picture is not supported. The maximum size of a single picture is 10M.

For image process parameters' details, Please see [QingStor Image API](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/image_process/).

## Usage

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

Assuming that there is an image in your bucket (named your-picture-uploaded.jpg), we can manipulate this image to demonstrate a series of usages of the basic image processing API.

At the same time, for the convenience of demonstration, we create a new function `perform_img_action()` for sending requests and receiving image processing results, which internally calls our basic image processing API.

```python
import tempfile

def perform_img_action(bucket_srv: Bucket, object_key: str, action: str, binary: bool = False, **kwargs) -> str:
    """
    perform_img_action performs the action specified and return the saved binary file name if action modify the image.
    Otherwise the text info will be returned.
    If response not as expected, error message stored in response will be returned.

    :param bucket_srv: the specified bucket where object_key located in.
    :param object_key: image location in bucket.
    :param action: actions will be performed.
    :param binary: is this action will output a binary file based on original image file. If true, file will be saved.
    :return: result based on binary flag or error message when error happened.
    """
    resp = bucket_srv.image_process(object_key=object_key, action=action, **kwargs)
    if resp.status_code != 200:
        return resp['message']
    elif binary:
        # example: stored in /tmp folder.
        with tempfile.NamedTemporaryFile(delete=False) as f:
            # for chunk in resp.content:
            #     f.write(chunk)
            f.write(resp.content)
            return f.name
    else:
        # Until now, only `info` reach this branch.
        # print(resp['width'])
        # print(resp['height'])
        # print(resp['type'])
        return str(resp.content, encoding="utf8")
```

Specifies the path of the image in the bucket.

```python
object_key = "your-picture-uploaded.jpg"
```

1. Get image information
    ```python
    print(perform_img_action(bucket_srv, object_key, "info"))
    ```

2. Crop the image (here a 300px wide, 400px image is cropped around the center of the image).
    ```python
    print(perform_img_action(bucket_srv, object_key, "crop:w_300,h_400,g_0", True))
    ```

3. Rotate the image 90 degrees.
    ```python
    print(perform_img_action(bucket_srv, object_key, "rotate:a_90", True))
    ```

4. Resize the image.
    ```python
    print(perform_img_action(bucket_srv, object_key, "resize:w_300,h_400,m_0", True))
    ```

5. Add a text watermark to the image (the text should first be base64 encoded and remove padding, the same with color).
    ```python
    import base64

    color = str.replace("c_" + str(base64.b64encode(bytes('#FF0000', encoding='utf8')), 'utf8'), "=", "")
    print(perform_img_action(bucket_srv, object_key,
                             "watermark:d_150,p_0.9,t_5rC05Y2w5paH5a2X," + color, True))
    ```

6. Add a picture watermark to the image.
    ```python
    print(perform_img_action(bucket_srv, object_key,
                             "watermark_image:l_10,t_10,p_2,"
                             "u_aHR0cHM6Ly9wZWszYS5xaW5nc3Rvci5jb20vaW1nLWRvYy1lZy9xaW5jbG91ZC5wbmc", True))
    ```

7. Format the image as png.
    ```python
    print(perform_img_action(bucket_srv, object_key, "format:t_png", True))
    ```

8. include operations in pipeline and they will be processed in order. The maximum number of operations in the pipeline is 10. The example ends with a save action to save the image to `img_res.png` in the bucket: `your-bucket-01`.
    ```python
    print(perform_img_action(bucket_srv, object_key,
                             "rotate:a_180|crop:w_300,h_400,g_0|resize:w_300,h_300|"
                             "format:t_png|save:b_your-bucket-01,k_img_res.png",
                             True))
    ```
