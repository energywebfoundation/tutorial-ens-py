# Ethereum ENS tutorial and playground with Python & web3.py

For educational purposes.

Used with [Parity client](https://github.com/paritytech/parity-ethereum) version 1.11.6 Beta and [web3.py](https://github.com/ethereum/web3.py) version 4.5.0.

### Dependencies

- Connection to Tobalaba. For a tutorial on how to set up a local [Parity client](https://github.com/paritytech/parity-ethereum) and connect to the network, check [here](https://energyweb.atlassian.net/wiki/spaces/EWF/pages/72974337/Install+the+Energy-Web+Client).
- [Parity UI](https://github.com/parity-js/shell) (Helps a lot).
- An account with some test Ethers in it. You can use the Parity UI for this purpose, then navigate to the [faucet](http://tobalaba.slock.it/faucet/) to get some ethers.
- Python 3.6, pip, Jupyter notebook

### Setup

You need a [Jupyter notebook](http://jupyter.org/install):
```
pip install jupyter
(or pip3 install jupyter)
```
Then
```
git clone https://github.com/ngyam/tutorial-ens-py.git
cd tutorial-ens-py
pip install -r requirements.txt
(or pip3 install -r requirements.txt)
```

### How to use

 1. Make sure your parity client is running and configured to connect to Tobalaba
 2. Open the Jupyter notebook file and play around.

```
cd tutorial-ens-py
jupyter notebook
```

### Resources

[Energy Web Foundation](http://www.energyweb.org/)

[Parity client](https://github.com/paritytech/parity-ethereum)

[ENS official documentation](https://docs.ens.domains/en/latest/)

[ENS Github Repo](https://github.com/ensdomains/ens)

[web3.py documentation](https://web3py.readthedocs.io/en/stable/)  

