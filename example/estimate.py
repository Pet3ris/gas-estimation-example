"""Main entry point for running keeper service."""

import os
from typing import Union

from dotenv import load_dotenv
import click
from nile.signer import Signer
from starknet_py.contract import Contract
from starknet_py.net.client import Client
from starkware.cairo.common.hash_state import compute_hash_on_elements
from starkware.crypto.signature.signature import private_to_stark_key, sign
from starkware.starknet.public.abi import get_selector_from_name


address = "0x00f585cea0571159106210061b01476890ef741ccd968caf200b31befd7993ec"
keeper_address = "0x03d336d1a5abd534669f995d89c0b9366a8f05e2a63aa6ed114e8b6e45581265"
registry = "0x0140cad60d7be7d1d33bba0206e0b73b6ed805432d15a5bb375e5eec1cdbcea0"


def get_account_message_args_sig(account_contract_address, to, function_name, calldata, nonce, max_fee, key):
    account_contract_address = int(account_contract_address, 16)
    to = int(to, 16)

    calls = [(hex(to), function_name, calldata)]

    call_array, calldata, *signature = Signer(key).sign_transaction(
        hex(account_contract_address),
        calls,
        nonce,
        max_fee
    )

    return [
        [{"to": to, "selector": selector, "data_offset": data_offset, "data_len": data_len} for (to, selector, data_offset, data_len) in call_array],
        calldata,
        nonce,
    ], signature

def get_private_key() -> Union[int, None]:
    load_dotenv()
    key = os.getenv("EXAMPLE_PRIVATE_KEY")
    return int(key)


if __name__ == "__main__":
    client = Client("testnet")
    task_contract = Contract.from_address_sync(address, client)

    keeper_contract = Contract.from_address_sync(keeper_address, client)
    key = get_private_key()

    (nonce,) = keeper_contract.functions["get_nonce"].call_sync()
    task_address_felt = int(address, 16)
    # args, signature = get_account_message_args_sig(keeper_address, registry, "executeTask", [task_address_felt], nonce, 0, key)
    args, signature = get_account_message_args_sig(keeper_address, address, "executeTask", [], nonce, 0, key)
    unsigned_invocation = keeper_contract.functions["__execute__"].prepare(*args)
    try:
        estimation = unsigned_invocation.estimate_fee_sync()
        click.echo(click.style(estimation, fg='blue'))
    except:
        pass
