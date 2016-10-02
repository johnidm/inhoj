install:
	python setup.py install

test:
	pip install -r requirements.txt
	py.test