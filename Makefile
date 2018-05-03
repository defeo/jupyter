build: notebooks/* build.py
	python build.py

install: requirements.txt
	pip install -r requirements.txt

clean:
	rm -r build

.PHONY: build install clean
