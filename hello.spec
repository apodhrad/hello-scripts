Summary: Hello script. (apodhrad)
Name: hello
Version: 0.1
Release: 3
URL:     http://apodhrad.org
License: GPL
Group: Development/Tools
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash
Source0: hello-%{version}.tar.gz
BuildArch: noarch

%description
A hello shell script.

%prep
%setup

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
install -m 755 hello.sh ${RPM_BUILD_ROOT}/usr/bin/hello

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/hello

%changelog
* Fri Jan 08 2016 Andrej Podhradsky <apodhrad@redhat.com>
- Test
