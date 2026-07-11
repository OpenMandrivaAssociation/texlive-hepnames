%global tl_name hepnames
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Pre-defined high energy particle names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hepnames
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hepnames.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hepnames.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hepnames provides a pair of LaTeX packages, heppennames and
hepnicenames, providing a large set of pre-defined high energy physics
particle names built with the hepparticles package. The packages are
based on pennames.sty by Michel Goossens and Eric van Herwijnen.
Heppennames re-implements the particle names in pennames.sty, with some
additions and alterations and greater flexibility and robustness due to
the hepparticles structures, which were written for this purpose.
Hepnicenames provides the main non-resonant particle names from
heppennames with more "friendly" names.

