"""
Name/label hash functions that can be used with custom (not only .eth, .test and .reverse) TLDs.
Copied from the web3.py repository https://github.com/ethereum/web3.py and modified.
"""

import idna
from web3 import Web3

def normalize_name(name):
    '''
    Clean the fully qualified name, as defined in ENS `EIP-137
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_
    This does *not* enforce whether ``name`` is a label or fully qualified domain.
    :param str name: the dot-separated ENS name
    :raises InvalidName: if ``name`` has invalid syntax
    '''
    if not name:
        return name
    elif isinstance(name, (bytes, bytearray)):
        name = name.decode('utf-8')
    try:
        return idna.decode(name, uts46=True, std3_rules=True)
    except idna.IDNAError as exc:
        raise InvalidName("%s is an invalid name, because %s" % (name, exc)) from exc

def label_to_hash(label):
    """
    Returns the sha3 hash of a label.
    """
    label = normalize_name(label)
    if '.' in label:
        raise ValueError("Cannot generate hash for label %r with a '.'" % label)
    return Web3().sha3(text=label)

def name_to_hash(name):
    """
    Returns the namehash of a name according to `EIP-137 <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md>`_
    """
    node =  b'\0' * 32
    if name:
        labels = name.split(".")
        for label in reversed(labels):
            labelhash = label_to_hash(label)
            assert isinstance(labelhash, bytes)
            assert isinstance(node, bytes)
            node = Web3().sha3(node + labelhash)
    return node