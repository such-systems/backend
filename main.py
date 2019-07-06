from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

def create_namespace(name):
    v1 = client.CoreV1Api()
    body = client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
    v1.create_namespace(body=body)

def delete_namespace(name):
    v1 = client.CoreV1Api()
    v1.delete_namespace(name=name)

create_namespace("such-namespace")
delete_namespace("such-namespace")
