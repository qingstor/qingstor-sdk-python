# 基本图片处理

用于对用户存储于 QingStor 对象存储上的图片进行各种基本处理，例如格式转换，裁剪，翻转，水印等。

目前支持的图片格式有:

- png
- tiff
- webp
- jpeg
- pdf
- gif
- svg

> 目前不支持对加密过后的图片进行处理，单张图片最大为 10M 。

图片处理的参数详细信息请参考对应文档说明 [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/image_process/) 。

## 用法

使用您的 AccessKeyID 和 SecretAccessKey 初始化 Qingstor 对象。

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

然后根据要操作的 bucket 信息（zone, bucket name）来初始化 Bucket。

```python
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

假设您指定的 bucket 中存在一张图片（your-picture-uploaded.jpg），我们可以通过操作这张图片来演示基本图像处理 API 的一系列用法。

同时，为了演示方便，我们新建一个用于发送并接收图片处理结果的函数 `perform_img_action()`，它在内部调用我们的基本图像处理 api。

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

指定该图片在 bucket 中的路径。

```python
object_key = "your-picture-uploaded.jpg"
```

1. 获取图像的信息
    ```python
    print(perform_img_action(bucket_srv, object_key, "info"))
    ```

2. 裁剪图像（这里围绕图片中心裁剪出宽 300px, 高 400px 的图片）。
    ```python
    print(perform_img_action(bucket_srv, object_key, "crop:w_300,h_400,g_0", True))
    ```

3. 旋转图像 90 度。
    ```python
    print(perform_img_action(bucket_srv, object_key, "rotate:a_90", True))
    ```

4. 调整图像大小。
    ```python
    print(perform_img_action(bucket_srv, object_key, "resize:w_300,h_400,m_0", True))
    ```

5. 为图像添加文字水印（文字应首先进行 base64 编码并去除 padding，颜色也一样）。
    ```python
    import base64

    color = str.replace("c_" + str(base64.b64encode(bytes('#FF0000', encoding='utf8')), 'utf8'), "=", "")
    print(perform_img_action(bucket_srv, object_key,
                             "watermark:d_150,p_0.9,t_5rC05Y2w5paH5a2X," + color, True))
    ```

6. 为图像添加图片水印。
    ```python
    print(perform_img_action(bucket_srv, object_key,
                             "watermark_image:l_10,t_10,p_2,"
                             "u_aHR0cHM6Ly9wZWszYS5xaW5nc3Rvci5jb20vaW1nLWRvYy1lZy9xaW5jbG91ZC5wbmc", True))
    ```

7. 格式化图像为 png。
    ```python
    print(perform_img_action(bucket_srv, object_key, "format:t_png", True))
    ```

8. 操作管道，图像将按顺序处理。 管道中的最大操作数为10。例子最后使用 save action 将图片保存至 bucket: `your-bucket-01` 中的 `img_res.png`。
    ```python
    print(perform_img_action(bucket_srv, object_key,
                             "rotate:a_180|crop:w_300,h_400,g_0|resize:w_300,h_300|"
                             "format:t_png|save:b_your-bucket-01,k_img_res.png",
                             True))
    ```
