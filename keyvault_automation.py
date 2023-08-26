import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from Keyvault_Variable import kvname,kvuri,secret

keyVaultName = kvname
KVUri = kvuri

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)


# print(f"Creating a secret in KV_NAME called '{secretName}' with the value '{secretValue}' ...")

for Key,Value in secret.items():
  client.set_secret(Key, Value)

print(Key,Value)

print(" done.")

# print(f"Retrieving your secret from KV_NAME.")

# retrieved_secret = client.get_secret(secretName)

# print(f"Your secret is '{retrieved_secret.value}'.")
# print(f"Deleting your secret from KV_NAME ...")

# poller = client.begin_delete_secret(secretName)
# deleted_secret = poller.result()

# print(" done.")
