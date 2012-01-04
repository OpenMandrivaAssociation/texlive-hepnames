# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/hepnames
# catalog-date 2008-08-21 09:38:31 +0200
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-hepnames
Version:	1.4
Release:	2
Summary:	Pre-defined high energy particle names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hepnames
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepnames.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hepnames.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Hepnames provides a pair of LaTeX packages, heppennames and
hepnicenames, providing a large set of pre-defined high energy
physics particle names built with the hepparticles package. The
packages are based on pennames.sty by Michel Goosens and Eric
van Herwijnen. Heppennames re-implements the particle names in
pennames.sty, with some additions and alterations and greater
flexibility and robustness due to the hepparticles structures,
which were written for this purpose. Hepnicenames provides the
main non-resonant particle names from heppennames with more
"friendly" names.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hepnames/hepnames.sty
%{_texmfdistdir}/tex/latex/hepnames/hepnicenames.sty
%{_texmfdistdir}/tex/latex/hepnames/heppennames.sty
%doc %{_texmfdistdir}/doc/latex/hepnames/ChangeLog
%doc %{_texmfdistdir}/doc/latex/hepnames/README
%doc %{_texmfdistdir}/doc/latex/hepnames/hepnames.pdf
%doc %{_texmfdistdir}/doc/latex/hepnames/hepnames.tex
%doc %{_texmfdistdir}/doc/latex/hepnames/hepnicenames-macros.tex
%doc %{_texmfdistdir}/doc/latex/hepnames/hepnicenames.pdf
%doc %{_texmfdistdir}/doc/latex/hepnames/hepnicenames.tex
%doc %{_texmfdistdir}/doc/latex/hepnames/heppennames-macros.tex
%doc %{_texmfdistdir}/doc/latex/hepnames/heppennames.pdf
%doc %{_texmfdistdir}/doc/latex/hepnames/heppennames.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
