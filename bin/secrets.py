from base64 import b64encode
import sys

from ghapi.all import GhApi
from nacl import encoding, public


# README:
# conda create -n secrets
# conda activate secrets
# pip install pynacl ghapi
#
# This script takes two positional arguments:
# argv[1]: a github access token with perms to set secrets
# argv[2]: a filepath with a csv generated by tokens.py


# ripped straight out of
# https://docs.github.com/en/rest/reference/actions\
#   example-encrypting-a-secret-using-python
def encrypt(public_key: str, secret_value: str) -> str:
    public_key = public.PublicKey(public_key.encode("utf-8"),
                                  encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


def update_secrets(api, tokens):
    for package, token in tokens:
        public_key_payload = api.actions.get_repo_public_key(
            owner='qiime2',
            repo=package,
        )

        encrypted_token = encrypt(public_key_payload['key'], token)

        api.actions.create_or_update_repo_secret(
            owner='qiime2',
            repo=package,
            secret_name='LIBRARY_TOKEN',
            encrypted_value=encrypted_token,
            key_id=public_key_payload['key_id'],
        )


def read_tokens(library_tokens_fp):
    with open(library_tokens_fp) as fh:
        return [t.strip().split(',') for t in fh.readlines()]


if __name__ == '__main__':
    gh_token = sys.argv[1]
    api = GhApi(token=gh_token)

    library_tokens_fp = sys.argv[2]
    tokens = read_tokens(library_tokens_fp)

    update_secrets(api, tokens)
