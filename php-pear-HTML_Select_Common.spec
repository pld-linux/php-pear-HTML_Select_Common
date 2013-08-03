%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	HTML_Select_Common
Summary:	%{_pearname} - small classes to handle common <select> lists
Summary(pl.UTF-8):	%{_pearname} - małe klasy do obsługi list <select>
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c5423721b258a4b10d2bbcd6ebde6d79
URL:		http://pear.php.net/package/HTML_Select_Common/
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-I18N >= 0.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides <select>lists for:
 - Country
 - UK counties
 - US States

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza listy <select> do pytań o:
 - kraj
 - kraje UK
 - stany US

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/HTML/Select
%{php_pear_dir}/HTML/Select/Common

%{_examplesdir}/%{name}-%{version}
