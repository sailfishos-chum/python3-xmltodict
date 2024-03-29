# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       python3-xmltodict

# >> macros
# << macros

Summary:    Makes working with XML feel like you are working with JSON
Version:    0.13.0
Release:    0
Group:      Applications
License:    MIT
BuildArch:  noarch
URL:        https://pypi.org/project/xmltodict/
Source0:    %{name}-%{version}.tar.gz
Source100:  python3-xmltodict.yaml
BuildRequires:  pkgconfig(python)
BuildRequires:  python3-rpm-macros

%description

xmltodict is a Python module that makes working with XML feel like you are
working with JSON

%if "%{?vendor}" == "chum"
PackageName: xmltodict
PackagerName: nephros
Categories:
 - Library
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/python3-xmltodict
  Repo: https://github.com/martinblech/xmltodict
Url:
  Homepage: https://pypi.org/project/xmltodict/
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%{py3_build}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{py3_install}

# >> install post
# << install post

%files
%defattr(-,root,root,-)
# >> files
%license LICENSE
%doc README.md
%{python3_sitelib}/*
# << files
