%define		module	Unidecode

Summary:	ASCII transliterations of Unicode text
Name:		python-Unidecode
Version:	0.04.14
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/U/Unidecode/Unidecode-%{version}.tar.gz
# Source0-md5:	d4106bcfdef39625944f4294ef4666de
URL:		http://pythonhosted.org/blinker/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASCII transliterations of Unicode text.

%package -n python3-%{module}
Summary:	ASCII transliterations of Unicode text
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
ASCII transliterations of Unicode text.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install	\
	--optimize 2				\
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install	\
	--optimize 2				\
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/unidecode
%{py_sitescriptdir}/*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/unidecode/__pycache__/*.py[co]
%{py3_sitescriptdir}/unidecode/*.py
%{py3_sitescriptdir}/*.egg-info

