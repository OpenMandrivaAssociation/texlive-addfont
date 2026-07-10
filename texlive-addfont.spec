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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is intended for use by users who know about fonts. It is a
quick-fix for fonts which do not have genuine LaTeX support. It is not
meant as a replacement of the LaTeX font definition files. It is meant
as something more useable for LaTeX users than the \newfont command.
With addfont the loaded font scales along with the usual LaTeX size
selection. Using this package still requires some knowledge on how to
use fonts with LaTeX.

