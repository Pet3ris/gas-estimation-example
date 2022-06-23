# Gas estimation example

## :warning: WARNING! :warning:

This code is entirely experimental and un-audited. Please do not use it in production!

## How to install

Dependencies:

- `poetry` (Python package manager)
- Basic cairo system dependencies (see [Setting up the environment](https://www.cairo-lang.org/docs/quickstart.html))

Installation:

```
poetry install
```

## How to use

1) First copy the `.env.example` file to create an `.env` file. For example:

```bash
cp .env.example .env
```
2) Deploy your account contract. (OPTIONAL)

```
make deploy_account
```

The deployed account we are using for reference is this:

```
0x0563489d870f357cd6d509bb0cf04ef335894e908553a638ba3b41191f98668a
```

[Link](https://goerli.voyager.online/contract/0x0563489d870f357cd6d509bb0cf04ef335894e908553a638ba3b41191f98668a)

3) Run estimation

```
make run
```
