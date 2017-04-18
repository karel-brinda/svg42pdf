SVG42PDF
========

.. image:: https://badge.fury.io/py/svg42pdf.svg
    :target: https://badge.fury.io/py/svg42pdf

Unlike other graphic formats, SVG is frequently hard to be converted to PDF. Various tools have been designed for this purpose, but most of them are either OS-specific, have OS-specific interface, create incorrent outputs, or
they heavily depend libraries, which are difficult to install or which are provided only under very restricted licenses.

SVG42PDF is a tool for SVG → PDF conversion using existing tools and libraries. The method of conversion can be either specified by user, or it can be selected automatically.


Installation
------------

From PyPI::

	pip install --upgrade svg42pdf

From Github::

	pip install --upgrade git+https://github.com/karel-brinda/svg42pdf


Examples
--------

Use first working method::

	svg42pdf input.svg output.pdf

Use `Cairo <https://cairographics.org/>`_::

	svg42pdf -m cairo input.svg output.pdf

Use `ReportLab <http://www.reportlab.com/>`_::

	svg42pdf -m reportlab input.svg output.pdf

Use `Inkscape <https://inkscape.org>`_::

	svg42pdf -m inkscape input.svg output.pdf

Use `ImageMagick <https://www.imagemagick.org>`_ (does not keep vector representation)::

	svg42pdf -m imagemagick input.svg output.pdf

Use `Wkhtmltopdf <https://wkhtmltopdf.org>`_ (using the Qt WebKit, creates big white margins)::

	svg42pdf -m wkhtmltopdf input.svg output.pdf


FAQ
---

* Why is there 42 in the name?

	There are already too many svg2pdf tools.
