.PHONY: serve build

dev serve:
	( \
		cd jekyll; \
		bundle exec jekyll serve -l \
	)

build public:
	( \
		mkdir -p public; \
		cd jekyll; \
		bundle exec jekyll build -d ../public \
	)
