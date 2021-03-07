import os
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from ti.utils import get_temporary_secret_and_token

# listaf = ['9c41111e2de84547a463fd39217199738d1e3deb72d4fec4399e6e241983c6f0.ae3cef932725ca7a30cdcb93fc6e09150a55e2a130ec7af63975a16c153ae2ba']
listaf = ['data.zip']
for item in listaf:
    # local_file = "/home/tione/notebook/lxmert/pytorch_pretrained_bert/" + item
    local_file = "/home/tione/notebook/lxmert/" + item

    bucket = "lxmert-1303238127"

    data_key = "./lxmert/" + item

    secret_id, secret_key, token = get_temporary_secret_and_token()
    secret_id = "AKIDOaCZibL3TdYZQ5CiuFJ83llW0UkjgPnv"
    secret_key = "0kETmqedSP9LIzQuAAvgrSYOMLo17737"
    config = CosConfig(Region=os.environ.get('REGION'), SecretId=secret_id, SecretKey=secret_key, Scheme='https')
    client = CosS3Client(config)

    response = client.get_object(
        Bucket=bucket,
        Key=data_key
    )
    response['Body'].get_stream_to_file(local_file)