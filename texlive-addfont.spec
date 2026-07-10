%global tl_name addfont
%global tl_revision 58559

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Easier use of fonts without LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/addfont
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addfont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is intended for use by users who know about fonts. It is a
quick-fix for fonts which do not have genuine LaTeX support. It is not
meant as a replacement of the LaTeX font definition files. It is meant
as something more useable for LaTeX users than the \newfont command.
With addfont the loaded font scales along with the usual LaTeX size
selection. Using this package still requires some knowledge on how to
use fonts with LaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/addfont
%dir %{_datadir}/texmf-dist/tex/latex/addfont
%doc %{_datadir}/texmf-dist/doc/latex/addfont/README
%doc %{_datadir}/texmf-dist/doc/latex/addfont/addfont.pdf
%doc %{_datadir}/texmf-dist/doc/latex/addfont/addfont.tex
%doc %{_datadir}/texmf-dist/doc/latex/addfont/license
%{_datadir}/texmf-dist/tex/latex/addfont/addfont.sty
