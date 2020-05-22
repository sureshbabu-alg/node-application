.PHONY: clean install test

all: install test package

install:
	pip3 install -t target .

package: install
	# cp scripts/* target/ ; \
	cp scripts/test_function.py target/ ; \
	cd target/ ; \
	zip -r ../lambda.zip * -i "yaml*" "sqlalchemy*" "pymysql*" "test_function.py" ;
	python setup.py bdist_egg
