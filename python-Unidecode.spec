Summary:	ASCII transliterations of Unicode text
Name:		python-Unidecode
Version:	0.04.13
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/U/Unidecode/Unidecode-%{version}.tar.gz
# Source0-md5:	74fabcc0aa3c3b185181df7fce8cab09
URL:		http://pythonhosted.org/blinker/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASCII transliterations of Unicode text.

%prep
%setup -qn Unidecode-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/unidecode
%{py_sitescriptdir}/*.egg-info

