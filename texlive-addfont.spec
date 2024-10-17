Name:		texlive-addfont
Version:	58559
Release:	2
Summary:	Easier use of fonts without LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/addfont
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addfont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addfont.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is intended for use by users who know about fonts.
It is a quick-fix for fonts which do not have genuine LaTeX
support. It is not meant as a replacement of the LaTeX font
definition files. It is meant as something more useable for
LaTeX users than the \newfont command. With addfont the loaded
font scales along with the usual LaTeX size selection. Using
this package still requires some knowledge on how to use fonts
with LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/addfont
%doc %{_texmfdistdir}/doc/latex/addfont

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
