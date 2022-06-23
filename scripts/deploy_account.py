from dotenv import load_dotenv
from nile.signer import Signer
import os


def run(nre):
    load_dotenv()
    private_key = int(os.getenv("EXAMPLE_PRIVATE_KEY"))
    public_key = Signer(private_key).public_key
    address, abi = nre.deploy("Account", arguments=[
        str(public_key)
    ])
    print(abi, address)
