import os
import cmd
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = "https://" + keyVaultName + ".vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "mySecret"

print("Input the value of your secret > ")
secretValue = input()

print("Create a secret in " + keyVaultName + "called '" + secretName + "' with the value '" + secretValue + "'")
client.set_secret(secretName, secretValue)

print("done.")

print("Forgetting your secret")
secretValue = ""
print("Your secret value is '" + secretValue +"'")

print("Retreving your secret from '" + keyVaultName + "'")

retreived_secret = client.get_secret(secretName)

print("Your retreived secret value is '" + retreived_secret.value + ".")

print("Deleting your secret from '" + keyVaultName + "'")

##client.delete_secret(secretName)
client.begin_delete_secret(secretName)

print("aaila, done.")







