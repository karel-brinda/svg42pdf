#! /usr/bin/env python3

import argparse
import inspect
import os
import snakemake
import re

def shell(
			cmd,
			remove_spaces=True,
			async=False,
			iterable=False,
			read=False, 
		):
	if remove_spaces:
		#print("removing spaces from command")
		cmd=re.sub(r'[ \t\f\v]+',' ',cmd).strip()

	return snakemake.shell(
			cmd=cmd,
			async=async,
			iterable=iterable,
			read=read,
		)

def report(svg_fn,pdf_fn):
	try:
		fun_name=inspect.stack()[1][3]
	except:
		fun_name='N/A'
	print("'{}' was created from '{}' using function '{}'.".format(pdf_fn,svg_fn,fun_name))


def svg42pdf_cairo(svg_fn,pdf_fn):
	import cairosvg
	cairosvg.svg2pdf(
			file_obj=open(svg_fn, "rb"),
			write_to=pdf_fn,
		)
	report(svg_fn,pdf_fn)

def svg42pdf_reportlab(svg_fn,pdf_fn):
	from .svg2rlg import svg2rlg
	from reportlab.graphics import renderPDF
	drawing = svg2rlg(svg_fn)
	renderPDF.drawToFile(drawing, pdf_fn)
	report(svg_fn,pdf_fn)

def svg42pdf_svg2pdf(svg_fn,pdf_fn):
	shell('svg2pdf "{svg}" "{pdf}"'.format(
			svg_fn,
			pdf_fn,
		))
	report(svg_fn,pdf_fn)

def svg42pdf_imagemagick(svg_fn,pdf_fn,dpi=200):
	shell('convert -density {dpi} "{svg}" "{pdf}"'.format(
			dpi=200,
			svg=svg_fn,
			pdf=pdf_fn,
		))
	report(svg_fn,pdf_fn)

def svg42pdf_inkscape(svg_fn,pdf_fn):
	shell('inkscape -f "{svg}" -A "{pdf}"'.format(
			svg=os.path.abspath(svg_fn),
			pdf=os.path.abspath(pdf_fn),
		))
	report(svg_fn,pdf_fn)

def svg42pdf_wkhtmltopdf(svg_fn,pdf_fn):
	shell('wkhtmltopdf -B 0 -L 0 -R 0 -T 0 "{svg}" "{pdf}"'.format(
			svg=os.path.abspath(svg_fn),
			pdf=os.path.abspath(pdf_fn),
		))
	report(svg_fn,pdf_fn)

def svg42pdf(svg_fn,pdf_fn,method):

	if method=="cairo":
		svg42pdf_cairo(svg_fn,pdf_fn)

	elif method=="reportlab":
		svg42pdf_reportlab(svg_fn,pdf_fn)

	elif method=="imagemagick":
		svg42pdf_imagemagick(svg_fn,pdf_fn)

	elif method=="inkscape":
		svg42pdf_inkscape(svg_fn,pdf_fn)

	elif method=="wkhtmltopdf":
		svg42pdf_wkhtmltopdf(svg_fn,pdf_fn)

	elif method=="any":
		try:
			svg42pdf_cairo(svg_fn,pdf_fn)
		except:
			try:
				svg42pdf_reportlab(svg_fn,pdf_fn)
			except:
				try:
					svg42pdf_wkhtmltopdf(svg_fn,pdf_fn)
				except:
					try:
						svg42pdf_svg2pdf(svg_fn,pdf_fn)
					except:
						svg42pdf_imagemagick(svg_fn,pdf_fn)

	else:
		raise ValueError("Unknown PDF rendering method '{}'.".format(method))


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
			"svg",
			type=str,
			help="SVG file"
		)
	parser.add_argument(
			"pdf",
			type=str,
			help="PDF file"
		)
	parser.add_argument(
			"-m",
			choices=['any', 'cairo', 'reportlab', 'inkscape', 'imagemagick', 'wkhtmltopdf'],
			default='any',
			help="Method"
		)
	args = parser.parse_args()

	svg_fn=args.svg
	pdf_fn=args.pdf
	method=args.m

	svg42pdf(svg_fn,pdf_fn,method)

if __name__ == "__main__":
	main()
