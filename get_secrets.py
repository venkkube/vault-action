import os
import logging
import hvac
import sys
import time
import subprocess

def vault_client():
    vc = hvac.Client(url=os.environ["INPUT_URL"],namespace=os.environ["INPUT_NAMESPACE"])
    if not vc.is_authenticated():
        vc.auth.approle.login(os.environ["INPUT_APPROLEID"],os.environ["INPUT_SECRETID"])
        logging.info(f"authenticated with vault")
    return vc

def getSecret(vc, secret_path, secret_key):

    # see if the path exists
    if not path_exists(vc, secret_path):
        logging.info(f"secrets path {secret_path} not exist in vault.")
        sys.exit(1)

    list_response = vc.secrets.kv.v2.read_secret(path=secret_path, mount_point=os.environ["MOUNT_POINT"])
    secret = list_response['data']['data'][secret_key]
    
    return secret


def path_exists(vc,path):
    # see if the path exists
    try:
        data = vc.secrets.kv.v2.read_secret_version(
            path=path,mount_point=os.environ["MOUNT_POINT"]
        )
    # if not, it will throw an exception
    except hvac.exceptions.InvalidPath:
        return False
    return True

def parseSecrets(vc, input_secrets):
    sec_list = input_secrets.split(";")
    for secret in sec_list:
        secret_info = secret.split(" ")
        secret_key = secret_info[1].strip()
        secret_path = secret_info[0].strip()
        secret = getSecret(vc,secret_path, secret_key)
        subprocess.run(["echo", "::set-output name="+secret_key+"::"+secret], check=True)

def main(): 
    os.environ["MOUNT_POINT"] = "secrets"
    input_secrets = os.environ["INPUT_SECRETS"]
    vc = vault_client()
    parseSecrets(vc,input_secrets)
   
if __name__ == "__main__":
    start_time = time.time()
    main()
    logging.info(f"Execution time: { time.time() - start_time } secs")