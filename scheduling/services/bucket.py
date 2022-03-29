import boto3
from scheduling import settings


class Bucket:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            try:
                s3_resource = boto3.client(
                    service_name=settings.AWS_SERVICE_NAME,
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    endpoint_url=settings.AWS_S3_ENDPOINT_URL,
                )
                cls._client = s3_resource
            except Exception as exception:
                pass

        return cls._client

    def get_list_objects(self, bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
        client = self.get_client()
        buck = client.list_objects_v2(Bucket=bucket_name)
        keys = []
        for obj in buck['Contents']:
            keys.append(obj)
        return keys

    def delete_object(self, object_name, bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
        try:
            client = self.get_client()
            response = client.delete_object(Bucket=bucket_name, Key=object_name)
        except Exception as exception:
            pass
        else:
            return response

    def download_obj(self, object_name, bucket_name=settings.AWS_STORAGE_BUCKET_NAME):
        with open(object_name, 'wb') as f:
            client = self.get_client()
            client.download_fileobj(bucket_name, object_name, f)


bucket = Bucket()

