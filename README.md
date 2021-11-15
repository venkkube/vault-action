# Hashicorp Key vault action

This action pulls the secrets from the enterise key vault server for the namespace. It creates action step outputs for the secrets given in the inputs. The outputs can be 

Currently it supports only approle login mode.

## Inputs
Here are all the inputs available through `with`:

| Input               | Description                                                                                                                                          | Default | Required |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| `url`               | The URL for the vault endpoint                                                                                                                       |         | ✔        |
| `secrets`           | A semicolon-separated list of secrets to retrieve. These will automatically be converted to output variable keys. See README for more details |         | ✔        |
| `namespace`         | The Vault namespace from which to query secrets. Vault Enterprise only, unset by default                                                             |         |     ✔      |
| `approleId`            | The Role Id for App Role authentication                                                                                                       |         |     ✔      |
| `secretId`          | The Secret Id for App Role authentication                                                                                                            |         |      ✔     |


## Outputs

### `Outputs created for all secert keys given in the input `secrets` list`

The time we greeted you.

## Example usage

```yaml
uses: actions/key-vault-action@master
with:
  url: 'http://your-org-vault-server:port'
  namespace: 'namespace'
  approleId: 'role-id'
  secretId: 'secret-id'
  secrets: |
    path-to-secret secret-key1 ;
    path-to-secret secret-key2
```
