SVG42PDF
========

Converting SVG to PDF might be a complicated task. Various tools exist this purpose,
but many of them create different outputs, they don't work both on Linux and OS X, or
they depend on some heavy libraries.

This program aims at the conversion using *any* available tool.


Installation
------------

From PyPI::

	pip install --upgrade svg42pdf

From Github::

	pip install --upgrade git+https://github.com/karel-brinda/svg42pdf


Examples
--------

Use first working method:

	svg42pdf -m any input.svg output.pdf

Use `Cairo <https://cairographics.org/>`_:

	svg42pdf -m cairo input.svg output.pdf

Use `ReportLab <http://www.reportlab.com/>`_:

	svg42pdf -m reportlab input.svg output.pdf

Use `Inkscape <https://inkscape.org>`_:

	svg42pdf -m inkscape input.svg output.pdf

Use `ImageMagick <https://www.imagemagick.org>`_:

	svg42pdf -m imagemagick input.svg output.pdf

Use `Wkhtmltopdf <https://wkhtmltopdf.org>`_ (using the Qt WebKit):

	svg42pdf -m wkhtmltopdf input.svg output.pdf


FAQ
---

* Why is there 42 in the name?

	There are too many svg2pdf tools.
