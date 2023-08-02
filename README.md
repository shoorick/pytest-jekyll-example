# pytest-jekyll-example

Example of testing Jekyll static site with pytest

## The goal

[Jekyll](https://jekyllrb.com) is static sites generator.
It is powerful and mature but I don’t know good way to test static sites
made by Jekyll. There are methods of Jekyll related testing (see below)
but there are some troubles:

- Ruby is not my main language, I am more familiar with Perl and Python,
- Python is more popular than Ruby and Perl,
- The most of Ruby related repositories and articles are outdated.

I have an experience with [Pytest](https://pytest.org)
and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
which are used for testing in general and DOM parsing respectively.
They both are written in Python. Tests which written with these tools
for [Flask](https://flask.palletsprojects.com/) web application
are compact, impressive and powerful.

**The goal** of this example is to give power of Pytest and BeautifulSoup
to Jekyll sites.

## Prerequisites

- make
- python3 and venv
- ruby and bundler

## Installation

_Coming soon_

## Usage

Perform all tests

```bash
make test
```

Build Jekyll site without tests and put the result
to `public` folder

```bash
make build
# or
make public
```

Run Jekyll as a server in development mode — `jekyll serve`

```bash
make dev
# or
make serve
```

## See also

- Jekyll testing with Ruby
  - Dean Marano.
    [Testing Your Jekyll Site, The Ruby Way](bit.ly/test-jekyll-rb-way) —
    with Capybara and Selenium.
  - [Jekyll-Test](https://github.com/Floppy/jekyll-test) — test the site
    for HTML validity, internal link correctness, alt tags,
    OpenGraph validity, https usage.
