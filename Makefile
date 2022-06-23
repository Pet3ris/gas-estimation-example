install_pre: FORCE
	poetry install --no-root --no-dev
	poetry run pip freeze

install_prod: FORCE
	poetry install --no-dev

run: FORCE
	poetry run python3 -m example.estimate

deploy_account: FORCE
	poetry run nile run scripts/deploy_account.py --network goerli

FORCE:
