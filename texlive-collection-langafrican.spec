# revision 21061
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langafrican
Epoch:		1
Version:	20120224
Release:	1
Summary:	African scripts
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langafrican.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-ethiop
Requires:	texlive-ethiop-t1
Requires:	texlive-fc
Requires:	texlive-hyphen-ethiopic
Requires:	texlive-collection-basic

%description
Support for typesetting some African scripts.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780330
- Update to latest release.
- Import texlive-collection-langafrican
- Import texlive-collection-langafrican

