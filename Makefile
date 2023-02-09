.PHONY: tango-icons, clean, all

tango-icons:
	./src/tango-icons/generate.py
	./src/package.sh tango-icons

clean-tango-icons:
	rm -rf packages/pdf-tango-icons
	rm -f packages/tango-icons.*
	rm -rf dist/tango-icons
	rm -f dist/tango-icons.zip

clean:
	rm -rf packages
	rm -rf dist

all: clean tango-icons
